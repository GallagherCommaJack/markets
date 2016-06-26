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
    p = (0.5 * total_true / (total_true + total_false)) + (0.5 * 0.7)
    b = my_wealth
    q = 1-p
    pos_bet = (b*p-q)/b
    neg_bet = (b*q-p)/b

    return pos_bet, neg_bet
