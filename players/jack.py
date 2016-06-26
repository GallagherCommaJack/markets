def bet(bets,wealth,round):
    total_true, total_false = bets['total']
    p_true = total_true / (total_true + total_false)
    p_false = 1 - p_true

    mw = wealth['jack']
    frac = 0.5

    if 0 == round:
        return (mw * frac, 0.0) if p_true > 0.5 else (0.0, mw * frac)
