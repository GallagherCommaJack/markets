def bet(bets,wealth,round):
    market_prob = bets['total'][0]/sum(bets['total'])

    if market_prob < 0.5447:
        return 23, 0
    else:
        return 0, 23
