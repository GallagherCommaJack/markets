def bet(t, wealth, round):
  budget = wealth["corey"]
  
  t = dict(t)
  wealth = dict(wealth)
  
  if "dummy" in t:
    del t["dummy"]
  if "example" in t:
    del t["example"]
  if "total" in t:
    del t["total"]
  if "dummy" in wealth:
    del wealth["dummy"]
  if "example" in wealth:
    del wealth["example"]
  if "total" in t:
    del wealth["total"]
  
  numPart = len(t.keys()) - 1
  weights = {} #{"jack": 5, "scott": 2, "jessica": 2, "william": 3, "james": 2, "mladen": 3}
  for k in t.keys():
    if k == "dummy" or k == "total":
      continue
    if not(weights.has_key(k)):
      weights[k] = wealth[k] * wealth[k]

  totalWealth = sum(wealth.values())
  totalWeight = sum(weights.values())
  sumBet = 0
  for k in t.keys():
    if k == "dummy" or k == "total":
      continue
    wealthBet = (t[k][0] - t[k][1])
    sumBet += wealthBet * weights[k]
  if sumBet > 0:
    return (0.3*budget, 0.0)
  elif sumBet < 0:
    return (0.0, 0.3 * budget)
  else:
    return (0.0,0.0)
