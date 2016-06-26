def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    #dummy_true, dummy_false = bets['dummy']

    # We can also see how much wealth a player has by querying wealth
    #dummy_wealth = wealth['dummy']

    # If we don't want to accidentally bet on another round without updating our code, we can do something like this:
    #if 0 == round:
    #    return dummy_true + 1.0, dummy_false
    #else:
    #    return 0.0, 0.0

    total_true, total_false = bets['total']

    p = total_true/(total_true+total_false)
    my_wealth = wealth['norman']

    
    if p > 0.75:
            return my_wealth, 0.0

    if p > 0.70:
            return my_wealth/2, 0.0

    if p > 0.65:
            return 0.0, my_wealth/2

    return 0.0, my_wealth

    
    else:
        return 0.0, 0.0
    
