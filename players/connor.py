def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    # dummy_true, dummy_false = bets['dummy']
    # We can also see how much wealth a player has by querying wealth
    # dummy_wealth = wealth['dummy']

    total_true, total_false = bets['total']
    p_house = total_true / (total_true + total_false)

    my_wealth = wealth['connor']

    true_cap = .5 * my_wealth
    false_cap = .3 * my_wealth
    
    p_mine = .726

    if p_house < p_mine:
        my_true = min(true_cap, true_cap * (p_mine - p_house)/.45)
        my_false = 0
    else:
        my_true = 0
        my_false = min(false_cap, false_cap * (p_house - p_mine)/.15)

    return (my_true, my_false)
