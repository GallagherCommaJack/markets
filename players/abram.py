def bet(bets,wealth,round):
    #dummy_true, dummy_false = bets['dummy']
    #dummy_wealth = wealth['dummy']
    total_true, total_false = bets['total']
    my_true, my_false = bets['abram']
    my_wealth = wealth['abram']

    del bets['dummy']
    #del wealth['dummy']
    del bets['total']
    #del wealth['total']
    del bets['abram']
    #del wealth['abram']

    house = total_true / (total_true + total_false)
    not_house = total_false / (total_true + total_false)

    #near = 0.0
    #far = 0.0
    #g = 0.0
    #bettors = 0.0
    #for bettor in bets:
    #    nearish, farish = bets[bettor]
    #    bettors = bettors+1.0
    #    if nearish > 1.0:
    #        near=near+1.0
    #    if farish > 1.0:
    #        far=far+1.0
    #    if nearish/house > farish/not_house:
    #         g=g+1.0

    #ratio = min((bettors - near - far)/bettors,0.0)

    p = 0.3
    #if g==0.0:
    #    p=0.04
    cap_percent = 1.0 - min(0.8, max(0.0,p-house,house-p))
    q = 1-p
    b_true = (1/house) - 1
    b_false = (1/not_house) - 1
    pos_bet = (p - q/b_true)*my_wealth
    pos_bet = min(1.0*my_wealth,pos_bet)*cap_percent
    neg_bet = (q - p/b_false)*my_wealth
    neg_bet = min(1.0*my_wealth,neg_bet)*cap_percent

    e_pos, e_neg = bets['evan']
    s_pos, s_neg = bets['scott']
    d_pos, d_neg = bets['dan']
    j_pos, j_neg = bets['jack']

    pos_bet = (e_pos + s_pos + d_pos + 4*j_pos + pos_bet) * 0.125
    neg_bet = (e_neg + s_neg + d_neg + 4*j_neg + neg_bet) * 0.125
    return pos_bet, neg_bet
