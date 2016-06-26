def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']
    market_prob = total_true / (total_false + total_true)
    
    # We can also see how much wealth a player has by querying wealth
    dummy_wealth = wealth['dummy']
    dan_wealth = wealth['dan']

    # If we don't want to accidentally bet on another round without updating our code, we can do something like this:
    if market_prob > .7:
        return 0.2 * dan_wealth, 0
    if market_prob > .75:
        return 0.5 * dan_wealth, 0
    if market_prob < .65:
        return 0, 0.5 * dan_wealth
    else: return 0, 0.2 * dan_wealth
