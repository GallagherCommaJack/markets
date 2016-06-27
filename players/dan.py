def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']
    market_prob = total_true / (total_false + total_true)
    
    # We can also see how much wealth a player has by querying wealth
    dummy_wealth = wealth['dummy']
    dan_wealth = wealth['dan']

    if market_prob > .84:
        return 0.0, 0.3 * dan_wealth
    if market_prob > .835:
        return 0.0, 0.2 * dan_wealth
    if market_prob > .831:
        return 0.0, 0.1 * dan_wealth
    if market_prob < .82:
        return 0.3 * dan_wealth, 0.0
    if market_prob < .825:
        return 0.2 * dan_wealth, 0.0
    if market_prob < .829:
        return 0.1 * dan_wealth, 0.0
    else: return 0.0, 0.0
