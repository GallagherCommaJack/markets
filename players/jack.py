kelly = lambda w, r: w - ((1 - w) / r)
cap = 0.5

def bet(bets,wealth,round):
    total_true, total_false = bets['total']
    me_true, me_false = bets['jack']
    p_true = total_true / (total_true + total_false)
    p_false = 1.0 - p_true

    mw = wealth['jack']

    wr = mw - (me_true + me_false)
    wp = mw * cap

    brazil_true = 0.82
    brazil_false = 1.0 - brazil_true
    odds_true = 1.0 / p_true
    odds_false = 1.0 / p_false

    k_true = kelly(odds_true, brazil_true)
    k_false = kelly(odds_false, brazil_false)

    true_new = me_true +  wr * k_true
    false_new = me_false +  wr * k_false

    if true_new + false_new > wp:
        pt = true_new / (true_new + false_new)
        pf = 1 - pt
        true_bet = wp * pt
        false_bet = wp * pf
    else:
        true_bet = me_true + wr * k_true
        false_bet = me_false + wr * k_false

   return true_bet, false_bet
