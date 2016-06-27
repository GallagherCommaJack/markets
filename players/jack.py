kelly = lambda w, r: w - ((1 - w) / r)

def bet(bets,wealth,round):
    total_true, total_false = bets['total']
    me_true, me_false = bets['jack']
    p_true = total_true / (total_true + total_false)
    p_false = 1.0 - p_true

    mw = wealth['jack']

    wr = mw - (me_true + me_false)

    brazil_true = 0.82
    brazil_false = 1.0 - brazil_true
    odds_true = 1.0 / p_true
    odds_false = 1.0 / p_false

    k_true = kelly(odds_true, brazil_true)
    k_false = kelly(odds_false, brazil_false)
    
    true_bet = me_true + wr * k_true
    false_bet = me_false + wr * k_false
    return true_bet, false_bet
