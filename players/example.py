def bet(bets, wealth, round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    anna_true, anna_false = bets['anna']
    dummy_true, dummy_false = bets['dummy']

    # We can also see how much wealth a player has by querying wealth
    dummy_wealth = wealth['dummy']
    scott_wealth = wealth['scott']

    # Here are the total amounts the market has put on true and false
    market_true, market_false = bets['total']
    market_probability = market_true / (market_true + market_false)

    # If we don't want to accidentally bet on another round without updating our code, we can do something like this:
    if 0 == round:
        return dummy_true + 1.0, dummy_false
    else:
        return 0.0, 0.0
