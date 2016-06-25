
import os.path
from shutil import copyfile

round = 0
value = 0.5

if os.path.isfile("wealth"):
    copyfile("wealth", "wealth.bak")

PLAYERS = []
if os.path.isfile("players"):
    handle = open("players","rb")
    PLAYERS = eval(handle.read())
    handle.close()
# PLAYERS = ('jack', 'james', 'scott', 'dan', 'dummy', 'mladen', 'jordan', 'norman', 'daniel', 'abram', 'patrick')
PLAYERS = ('dummy')

WEALTH = {}
if os.path.isfile("wealth"):
    handle = open("wealth")
    WEALTH = eval(handle.read())
    handle.close()
else:
    WEALTH = dict((name, 100.0) for name in PLAYERS)
    handle = open("wealth.log","a")
    handle.write(str(WEALTH))

functions = [getattr(__import__('players.%s' % name), name).bet for name in PLAYERS]

bfs = dict(zip(PLAYERS, functions))

formatBT = lambda bt: '\n'.join('%s: %0.1f, %0.1f' % thing for thing in sorted((k, t, f) for k, (t, f) in bt.items()))

from market import solve
from market import update_wealth
from market import apply_bidding_functions
result = solve(bfs,WEALTH,round,1000)
print 'Bets:\n'
print formatBT(result)
print
print
new_wealth = update_wealth(result,WEALTH,value)
print 'Wealth:\n'
print new_wealth
handle = open("wealth","wb")
handle.write(str(new_wealth))
handle.close()
handle = open("wealth.log","a")
handle.write(str(new_wealth))
handle.close()
print
print
print 'Converged?\n'
next_res = apply_bidding_functions(bfs,result)
print all(abs(next_res[name][0] - result[name][0]) + abs(next_res[name][1] - result[name][1]) < 1e-2 for name in result)
# results, last = solve(bfs, WEALTH, round)ag
# lastResult = results[-1]
# print '\n\n'.join(map(formatBT, results))
# print
# print formatBT(last)
# print

