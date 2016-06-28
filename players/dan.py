def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']
    market_prob = total_true / (total_false + total_true)
    
    # We can also see how much wealth a player has by querying wealth
    dummy_wealth = wealth['dummy']
    dan_wealth = wealth['dan']

    james_true, james_false = bets['james']

    return james_true, james_false