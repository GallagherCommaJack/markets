def bet(bets, wealth, round):


    my_wealth = wealth['tom']
    best_player = max(wealth, key=wealth.get)
    best_wealth = wealth[best_player]

    total_true, total_false = bets['total']
    total = total_true + total_false

    best_true, best_false = bets[best_player]

    n = my_wealth * 0.5 / best_wealth

    return best_true/n, best_false/n

    p = total_true/total

    if p > 0.7:
        return my_wealth/2, my_wealth/2
    else:
        return my_wealth/2, my_wealth/2

    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']

    # We can also see how much wealth a player has by querying wealth
    dummy_wealth = wealth['dummy']

    # If we don't want to accidentally bet on another round without updating our code, we can do something like this:
    if 0 == round:
        return dummy_true + 1.0, dummy_false
    else:
        return 0.0, 0.0
