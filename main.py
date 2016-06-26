
import os
import os.path
from shutil import copyfile

round = 0
value = 0.5

PLAYERS = tuple(filename[:-3] for filename in os.listdir('./players') if filename[-3:] == '.py' and filename not in ('__init__.py', 'example.py'))
assert 'dummy' in PLAYERS # We always want a dummy player - this is assumed in market.py code.

if os.path.isfile("wealth"):
    copyfile("wealth", "wealth.bak")

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
formatWealth = lambda wealth: '\n'.join('%s: %0.1f' % thing for thing in sorted(wealth.items()))

from market import solve
from market import update_wealth
from market import apply_bidding_functions
result, converged = solve(bfs,WEALTH,round,1000)
print '--- Bets ---------------'
print formatBT(result)
print
print
new_wealth = update_wealth(result,WEALTH,value)
print '--- Wealth -------------'
print formatWealth(new_wealth)
handle = open("wealth","wb")
handle.write(str(new_wealth))
handle.close()
handle = open("wealth.log","a")
handle.write(str(new_wealth))
handle.close()
print
print
print 'Converged:', 'YES' if converged else 'NO'

