
def run(state, bfs):
	from market import solve
	bets, converged = solve(bfs, dict((name, state.wealth.get(name, state.DEFAULT_WEALTH)) for name in playerNames), state.rounds, 1000)

def main(state, outcome):
	import os

	playerNames = tuple(filename[:-3] for filename in os.listdir('./players') if filename[-3:] == '.py' and filename not in ('__init__.py', 'example.py'))
	assert 'dummy' in playerNames # We always want a dummy player - this is assumed in market.py code.

	def bfForPlayerName(name):
		return getattr(__import__('players.%s' % name), name).bet

	bfs = dict((name, bfForPlayerName(name)) for name in playerNames)

	bets, converged = run(state, bfs)

	return bets, converged, state.advance(bets, outcome)

if __name__ == "__main__":
	from state import State
	state = State.load()

	DEFAULT_OUTCOME = 0.5

	from sys import argv
	if len(argv) > 1:
		try:
			OUTCOME = float(argv[1])
		except:
			OUTCOME = DEFAULT_OUTCOME
	else:
		OUTCOME = DEFAULT_OUTCOME

	bets, converged, newState = main(state, OUTCOME)

	formatBT = lambda bt: '\n'.join('%s: %0.1f, %0.1f' % thing for thing in sorted((k, t, f) for k, (t, f) in bt.items()))
	formatWealth = lambda wealth: '\n'.join('%s: %0.1f' % thing for thing in sorted(wealth.items()))

	print '--- Bets ---------------'
	print formatBT(bets)
	print
	print

	print '--- Wealth -------------'
	print formatWealth(newState.wealth)
	print
	print
	print 'Converged:', 'YES' if converged else 'NO'

	newState.save()
