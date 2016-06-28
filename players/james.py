from math import log

def solver_prob_given_bet(true_bet, their_wealth):
	# if they bet epsilon, divide by 4 (trolls)
	if true_bet < 0.5:
		return 0.25
	if true_bet < 1.0:
		return 0.5
	if true_bet / their_wealth < 0.01:
		return 0.75
	if true_bet / their_wealth < 0.05:
		return 0.9
	return 1.0

def bet(bets, wealth, round):
	
	# Ignoring Scott, who isn't in this round.

	# ~95-99%
	sure_p = 0.97
	sure_solvers = [
		'james',
		'harrison',
	]

	# ~80%
	probably_p = 0.8
	probably_solvers = [
		'william',
		'evan',
		'patrick',
	]

	# ~50%
	not_sure_p = 0.5
	not_sure_solvers = [
		'norman', # Can solve it, but slowly.
		'daniel',
		'jessica',
	]

	# ~20%
	probably_not_p = 0.2
	probably_not_solvers = [
		'anna',
		'val',
		'connor',
		'harmanas',
		'mladen',
		'andrew',
	]

	# ~10%
	probably_nope_p = 0.1
	probably_nope_solvers = [
		'corey',
		'izaak',
		'tom',
		'nick',
		'abram',
	]

	# ~0.1%
	nope_p = 0.01
	nope_solvers = [
		'dan',
		'jack',
	]

	solvers = dict(
		[(name, sure_p) for name in sure_solvers] +
		[(name, probably_p) for name in probably_solvers] +
		[(name, not_sure_p) for name in not_sure_solvers] +
		[(name, probably_not_p) for name in probably_not_solvers] +
		[(name, probably_nope_p) for name in probably_nope_solvers] +
		[(name, nope_p) for name in nope_solvers]
	)

	our_solve = solvers['dan'] + solvers['james']


	total_true, total_false = bets['total']
	p = total_true / (total_true + total_false)

	G = [name for name in bets if name not in ('dummy', 'total', 'dan', 'james') and bets[name][0] / p > bets[name][1] / (1. - p)]


	p_solve_without_us = 0.0 if not G else sum(solvers.get(name, 0.0) * solver_prob_given_bet(bets[name][0], wealth[name]) for name in G) * 1. / len(G)
	p_solve_with_us = our_solve if not G else (our_solve * 2. + len(G) * p_solve_without_us) * 1. / (len(G) + 2.)

	payoff_scale_true = p_solve_with_us * 1. / p
	payoff_scale_false = p_solve_without_us * 1. / (1. - p)

	if payoff_scale_true > payoff_scale_false:
		return min(40.0, log(p_solve_with_us / p, 2) * 100.0), 0.0
	else:
		return 0.0, min(40.0, log(p_solve_without_us / (1. - p), 2) * 100.0)
