
def loadBettingFunctions():
	import os

	playerNames = tuple(filename[:-3] for filename in os.listdir('./players') if filename[-3:] == '.py' and filename not in ('__init__.py', 'example.py'))
	assert 'dummy' in playerNames # We always want a dummy player - this is assumed in market.py code.

	def bfForPlayerName(name):
		return getattr(__import__('players.%s' % name), name).bet

	return dict((name, bfForPlayerName(name)) for name in playerNames)

def run(state, bfs, max_iterations = 10000):
	from market import solve
	return solve(bfs, dict((name, state.wealth.get(name, state.DEFAULT_WEALTH)) for name in bfs), state.rounds, max_iterations)

def main(state, outcome):
	bets, converged = run(state, loadBettingFunctions())
	return bets, converged, state.advance(bets, outcome)

if __name__ == "__main__":
	from state import State
	state = State.load()

	outcome_exists = False
	outcome = 0.5

	from sys import argv
	if len(argv) > 1:
		try:
			outcome = float(argv[1])
			outcome_exists = True
		except:
			pass

	bets, converged, newState = main(state, outcome)

	formatBT = lambda bt: '\n'.join('%s: %0.1f, %0.1f' % thing for thing in sorted((k, t, f) for k, (t, f) in bt.items()))
	formatWealth = lambda wealth: '\n'.join('%s: %0.1f' % thing for thing in sorted(wealth.items()))

	print '--- Bets ---------------'
	print formatBT(bets)
	print
	print

	if outcome_exists:

		print '--- Wealth -------------'
		print formatWealth(newState.wealth)
		print
		print
		print 'Converged:', 'YES' if converged else 'NO'

		newState.save()
