def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    # dummy_true, dummy_false = bets['dummy']
    # We can also see how much wealth a player has by querying wealth
    # dummy_wealth = wealth['dummy']

	total_true, total_false = bets['total']
	prob = total_true / (total_true + total_false)

	my_wealth = wealth['connor']

	true_cap = .7
	false_cap = .7
	my_true = true_cap * my_wealth * (prob - .71)^(2/3) / ((1 - .71)^(2/3)) if prob > .71
	my_false = false_cap * my_wealth * (.69 - prob)^(2/3) / ((.69 - 0)^(2/3) if prob < .69

    # If we don't want to accidentally bet on another round without updating our code, we can do something like this:
    if 0 == round:
        return tuple(my_true, my_false)
    else:
        return 0.0, 0.0