def bet(bets,wealth,round):
    total_true, total_false = bets['total']
    market_prob = total_true / (total_false + total_true)
    
    dummy_wealth = wealth['dummy']
    dan_wealth = wealth['dan']

    if market_prob > .5:
        return 0.0, 0.5 * dan_wealth
    if market_prob > .45:
        return 0.0, 0.4 * dan_wealth
    if market_prob > .4:
        return 0.0, 0.2 * dan_wealth
    if market_prob < .25:
        return 0.45 * dan_wealth, 0.0
    if market_prob < .28:
        return 0.3 * dan_wealth, 0.0
    if market_prob < .33:
        return 0.15 * dan_wealth, 0.0
    else: return 0.0, 0.0