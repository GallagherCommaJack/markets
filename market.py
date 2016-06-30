
import math


# A bet table is a dictionary of {'name' : (onfalse, ontrue), 'total': (onfalse, ontrue)}
# A bidding function maps a bet table to (onfalse, ontrue).


def bet_table_to_vec(bt):
  sorted_keys = sorted(bt.keys())
  vec = []
  for k in sorted_keys:
    vec.append(bt[k][0])
    vec.append(bt[k][1])
  return vec

def vec_to_bet_table(sorted_keys, vec):
  bt = {}
  for i,k in enumerate(sorted_keys):
    bt[k] = (vec[2*i], vec[2*i + 1])
  return bt

def map_bet_table(f, bt):
  bt2 = {}
  for key in bt:
    (onfalse, ontrue) = bt[key]
    bt2[key] = (f(onfalse), f(ontrue))
  return bt2


ROUND_PRECISION = 0.0001

def round_low(x, prec):
  return math.floor(x / prec) * prec

def round_high(x, prec):
  return round_low(x, prec) + prec

def order_dimensions(xs):
  return sorted(range(len(xs)), key=lambda d: xs[d])

# Apply a function whose domain is [0, 1]^n. in a piecewise-linear way.  Function is
# extrapolated from the corner points {0, 1}^n.
def apply_01_piecewise_linear(f, xs):
  assert all(-1e-10 <= x <= 1+1e-10 for x in xs)
  xs = [x if 0.0 <= x <= 1.0 else 0.0 if x < 0.0 else 1.0 for x in xs]
  order_dim = order_dimensions(xs)
  verts = []
  vert = [1.0] * len(xs)
  verts.append(vert[:])
  for d in order_dim:
    vert[d] = 0.0
    verts.append(vert[:])
  avg = 0.0
  for i in range(len(xs) + 1):
    if i == 0:
      weight = xs[order_dim[0]]
    elif i == len(xs):
      weight = 1 - xs[order_dim[-1]]
    else:
      weight = xs[order_dim[i]] - xs[order_dim[i-1]]
    avg += weight * f(verts[i])
  return avg

def vec_add(v1, v2):
  return [x+y for x,y in zip(v1, v2)]

def vec_scale(s, v):
  return [s*x for x in v]

# Apply a function in a piecewise-linear way.
def apply_piecewise_linear(f, xs, prec):
  xs_low = [round_low(x, prec) for x in xs]
  xs_high = [round_high(x, prec) for x in xs]
  xs_alongs = [(x - l) / (h - l) for x,l,h in zip(xs, xs_low, xs_high)]
  res_01 = apply_01_piecewise_linear(
      lambda alongs: f(vec_add(xs_low, vec_scale(prec, alongs))),
      xs_alongs)
  normal_res = f(xs)
  return res_01

# Adds summary info to a bet table.
def add_extra_bt_info(bt):
  tot_false = 0.0
  tot_true = 0.0
  for f,t in bt.values():
    tot_false += f
    tot_true += t
  bt['total'] = (tot_false, tot_true)


# Convert a bidding function to a piecewise linear version of it.
def piecewise_linearify_bidding_function(bf, prec):
  def bf2(bt):
    sorted_keys = sorted(bt.keys())
    def of_component(c):
      return apply_piecewise_linear(lambda bt_vec: bf(vec_to_bet_table(sorted_keys, bt_vec))[c],
                                    bet_table_to_vec(bt),
                                    prec)
    return (of_component(0), of_component(1))
  return bf2

# Caps a bidding function at some amount.
def cap_bidding_function(bf, wealth): # wealth here means wealth of the current better, not wealth table
  def bf2(bt):
    onfalse, ontrue = bf(bt)
    ontrue = max(0.0, ontrue)
    onfalse = max(0.0, onfalse)
    tot = onfalse + ontrue
    if tot > wealth:
      scale = wealth / tot
      return (onfalse * scale, ontrue * scale)
    return (onfalse, ontrue)
  return bf2

# Catches errors thrown by a bidding function, and defaults to betting nothing.
def catch_bidding_function_errors(bf, identifier):
  from time import time
  errors_seen = set()
  def bf2(bt):
    try:
      start_time = time()
      result = bf(bt)
      total_time = time() - start_time
      if total_time > 1e-3:
        print 'Warning: %s ran for %.3f seconds.' % (identifier, total_time)
      if result is not None and isinstance(result, tuple) and len(result) == 2:
        return tuple(float(x) for x in result)
      else:
        raise Exception("Bad value returned: %r" % result)
    except Exception as ex:
      if repr(ex) not in errors_seen:
        errors_seen.add(repr(ex))
        print "Exception encountered in bidding function from '%s'." % identifier

        import traceback
        traceback.print_exc()

        print
        print "Carrying on, and ignoring errors like this..."
        print
      return 0.0, 0.0
  return bf2

def compute_prob(totals):
  if sum(totals) == 0.0:
    return 0.5
  else:
    return totals[1] / sum(totals)

# Find a betting table that is a fixed point of the bidding functions.
def resolve_bidding_functions2(bfs, n_iters):
  # todo: change weights over time? at time t it's sqrt(t)
  bt = {}
  for k in bfs:
    bt[k] = (0.0, 0.0)
  add_extra_bt_info(bt)
  sorted_keys = sorted(bt.keys())
  bt_sum_vec = bet_table_to_vec(bt)
  for i in range(n_iters):
    bt_average_vec = vec_scale(1.0 / (i + 1), bt_sum_vec)
    bt_average = vec_to_bet_table(sorted_keys, bt_average_vec)
    bt2 = {}
    for k in bfs:
      bt2[k] = bfs[k](bt_average)
    add_extra_bt_info(bt2)
    bt_sum_vec = vec_add(bt_sum_vec, bet_table_to_vec(bt2))
    bt = bt2
  return bt

def apply_bidding_functions(bfs, bt):
  bt2 = {}
  for k in bfs:
    bt2[k] = bfs[k](bt)
  add_extra_bt_info(bt2)
  return bt2

# Find a betting table that is a fixed point of the bidding functions.
def resolve_bidding_functions(bfs, max_iterations):
  # todo: change weights over time? at time t it's sqrt(t)
  # James: Need to think about weight schedule.
  
  # Initial bets. Zero for everyone except the dummy player.
  bt = dict((name, (0.0, 0.0) if name != 'dummy' else (10.0, 10.0)) for name in bfs)
  add_extra_bt_info(bt)

  sorted_keys = sorted(bt.keys())
  bt_current_vec = bet_table_to_vec(bt)

  probable_convergence_vec = bt_current_vec
  probable_convergence_steps = 0
  converged = False

  for i in xrange(max_iterations):

    if i > 10 and i % 100 == 0:
      print "Resolve bidding functions still hasn't converged. Iteration %d / %d" % (i, max_iterations)

    weight_scale_factor = (i * 1. / max_iterations) ** 2
    weight = 0.8 * (1. - weight_scale_factor) + 0.999 * weight_scale_factor

    bt_next = apply_bidding_functions(bfs, vec_to_bet_table(sorted_keys, bt_current_vec))
    add_extra_bt_info(bt_next)
    bt_current_vec = [x * weight + y * (1. - weight) for x,y in zip(bt_current_vec, bet_table_to_vec(bt_next))]

    if all(abs(x - y) < 1e-2 for x, y in zip(probable_convergence_vec, bt_current_vec)):
      probable_convergence_steps += 1
      if probable_convergence_steps >= 5:
        converged = True
        break
    else:
      probable_convergence_vec = bt_current_vec
      probable_convergence_steps = 0

  return bt_next, converged

def mk_gamblers(bfs, wealth, prec, round):
  from collections import defaultdict
  def gambler_from_name(name):
    bf = bfs[name]
    f = piecewise_linearify_bidding_function(
        cap_bidding_function(
          catch_bidding_function_errors(lambda bets: bf(defaultdict(lambda: (0.0, 0.0), bets.items()), dict(wealth.items()), round), bf.__module__),
          wealth[name]),
        prec)
    return f
  return dict((name, gambler_from_name(name)) for name in bfs)

# Returns (bets, converged), where `bets` is a map from names to (true bet, false bet)
# and `converged` is a boolean indicating whether the fixed-point computation converged.
def solve(bfs, wealth, round, max_iterations=10000, precision=0.001):
  bfs = mk_gamblers(bfs, wealth, precision, round)
  return resolve_bidding_functions(bfs, max_iterations)

def test1():
  def bf1(bt, wealth, round):
    p = compute_prob(bt['total'])
    if p < 0.7:
      return (0.0, 1.0)
    else:
      return (1.0, 0.0)
  def bf2(bt, wealth, round):
    p = compute_prob(bt['total'])
    return (3 - p, 0.0)
  bfs = {'first': bf1, 'second': bf2}
  wealth = {'first': 100.0, 'second': 100.0}
  bfs = mk_gamblers(bfs,wealth,0.01)
  print resolve_bidding_functions(bfs, 10000)

def test2():
  def bf1(bt, wealth, round):
    p = compute_prob(bt['total'])
    if p < 0.7:
      return (0.0, 1.0)
    else:
      return (1.0, 0.0)
  def bf2(bt, wealth, round):
    p = compute_prob(bt['total'])
    return (3 - p, 0.0)
  bfs = {'first': bf1, 'second': bf2}
  wealth = {'first': 100.0, 'second': 100.0}
  print solve(bfs, wealth, 0)


if __name__ == '__main__':
  test1()
  test2()
  print 'done!'

