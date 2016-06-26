def bet(t, wealth, round):
  budget = wealth["corey"]
  
  numPart = len(t.keys()) - 1
  weights = {"jack": 2, "scott": 2, "jessica": 2, "william": 2}
  for k in t.keys():
    if k == "dummy" or k == "total":
      continue
    if not(weights.has_key(k)) and not(wealth[k] < 1):
      weights[k] = 1      

  totalWealth = sum(wealth.values())
  totalWeight = sum(weights.values())
  sumBet = 0
  for k in t.keys():
    if k == "dummy" or k == "total":
      continue
    if (wealth[k] < 1):
      continue
    ratioWealthBet = (t[k][0] - t[k][1]) / wealth[k]
    sumBet += ratioWealthBet * weights[k] * wealth[k]
  sumBet /= (totalWeight * totalWealth)
  if sumBet > 0:
    return (max(0.0, min(0.1, sumBet)) * budget, 0.0)
  elif sumBet < 0:
    return (0.0, max(0.0, min(0.1, -sumBet)) * budget)
  else:
    return (0.0,0.0)