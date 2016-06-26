def bet(bets, wealth, n):
  w = wealth / 2.0
  p = bets['total'][0] / float(sum(bets['total']))

  if p > 0.85:
    return (0.0, w)
  else:
    return (w, 0.0)
