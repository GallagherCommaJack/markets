
class State(object):

	DEFAULT_WEALTH = 100.0

	def __init__(self, wealths, bets, outcomes, rounds):
		self.previousWealth = tuple(dict(wealth.items()) for wealth in wealths)
		self.previousBets = tuple(dict(bet.items()) for bet in bets)
		self.previousOutcomes = tuple(outcomes)
		self.rounds = rounds
		assert len(wealths) > 0
		assert len(bets) > 0
		assert len(outcomes) > 0
		self.wealth = wealths[-1]
		self.bets = bets[-1]
		self.outcome = bets[-1]


	def save(self, path='state.pickle'):
		from cPickle import dump
		with open(path, 'wb') as f:
			dump(self, f, protocol=2)

	@classmethod
	def load(cls, path='state.pickle'):
		try:
			from cPickle import load
			with open(path, 'rb') as f:
				return load(f)
		except Exception as ex:
			print "Error occurred loading state:", ex
			print "Proceeding to create initial state instead."
			return cls.fromInitial()


	@classmethod
	def resolveMarket(cls, bets, outcome):
		assert 'total' in bets
		assert bets['total'][0] > 0.0 and bets['total'][1] > 0.0
		assert 0. <= outcome <= 1.
		marketProbability = bets['total'][0] / (bets['total'][0] + bets['total'][1])
		truth = (outcome, 1. - outcome)
		scale = (1. / marketProbability, 1. / (1. - marketProbability))
		
		# Note: assumes that all the players of interest placed bets.
		return dict(
			(name, sum(truth[i] * scale[i] * amt for i, amt in enumerate(amounts)))
			for name, amounts in bets.items() if name != 'total'
		)
	
	@classmethod
	def fromPrevious(cls, state, bets, outcome):
		winnings = cls.resolveMarket(bets, outcome)
		return cls(
			state.previousWealth + [dict((name, winnings[name] + state.wealth.get(name, cls.DEFAULT_WEALTH)) for name in winnings)],
			state.previousBets + [bets],
			state.previousOutcomes + [outcome],
			state.rounds + 1
		)

	def advance(self, bets, truth):
		return self.fromPrevious(self, bets, truth)

	@classmethod
	def fromInitial(cls):
		return cls([{'dummy': 100.0}], [{'total': (10.0, 10.0), 'dummy': (10.0, 10.0)}], [0.5], 1)


if __name__ == "__main__":
	state = State.load()
	print 'Wealth:'
	print state.wealth
	print
	print 'Last bets:'
	print state.bets

