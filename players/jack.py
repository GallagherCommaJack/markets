def kelly(b,p):
    (p * (b + 1) - 1) / b

def bet(bets,wealth,round):
    total_true, total_false = bets['total']
    me_true, me_false = bets['jack']
    p_true = total_true / (total_true + total_false)
    p_false = 1 - p_true

    mw = wealth['jack']
    wr = mw - (me_true + m_false)

    frac = 0.5
    brazil_true = 0.82
    brazil_false = 1 - brazil_true
    odds_true = 1 / p_true
    odds_false = 1 / p_false

    k_true = kelly(odds_true,brazil_true)
    k_false = kelly(odds_false,brazil_false)
    return me_true + wr * k_true, me_false + wr * k_false
