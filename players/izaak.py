def bet(bets, wealth, n):
  if n == 0:
    p = bets['total'][0] / float(sum(bets['total']))
    w = wealth['izaak'] / 2.0
    if p > 0.7:
      return (w, 0.0)
    else:
      return (0.0, w)
