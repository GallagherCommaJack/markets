def bet(bets,wealth,round):
    dummy_true, dummy_false = bets['dummy']
    dummy_wealth = wealth['dummy']
    total_true, total_false = bets['total']
    total_wealth = wealth['total']
    my_true, my_false = bets['abram']
    my_wealth = wealth['abram']

    del bets['dummy']
    del wealth['dummy']
    del bets['total']
    del wealth['total']
    del bets['abram']
    del wealth['abram']

    house = total_true / (total_true + total_false)
    not_house = total_false / (total_true + total_false)
    p = 0.85
    q = 1-p
    b_true = (1/house) - 1
    b_false = (1/not_house) - 1
    pos_bet = p - q/b_true
    neg_bet = q - p/b_false

    return pos_bet, neg_bet
