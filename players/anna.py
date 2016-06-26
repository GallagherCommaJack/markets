def bet(bets,wealth,round):
    market_prob = bets['total'][0]/sum(bets['total'])

    myest = [4, 4]

    predictors = [myest, bets['jessica'], bets['abram'], bets['dan']]
    true_prediction = sum(p[0] for p in predictors)
    false_prediction = sum(p[1] for p in predictors)

    mytotalprob = true_prediction / (true_prediction + false_prediction)

    if market_prob < mytotalprob:
        return 10., 0.
    else:
        return 0., 10.
