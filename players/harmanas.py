def bet(bets, wealth, round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    total_true, total_false = bets['total']
	players = len(wealth)
	ps = total_true / (total_true + total_false)
	total = (total_true + total_false) / players

    # We can also see how much wealth a player has by querying wealth
	w_list = list(d.items())
	w_sorted = w_list.sort(key= lambda tup: tup[1])
	
	# This is wrong, it's supposed to take an average.
	for w in w_sorted[0:3]:
		t, f = bets[w[0]]
		p = (p + (t / (t+f)))/2
	
	if round > 0:
		return (p * total, (1-p) * total)
	else:
		return 0, 0
		

