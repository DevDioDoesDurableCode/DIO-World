import history
import leader

influence = 0
influenceStorage = 1000
foodConsumption = 1.0
edictEndYear = 0
edictInEffect = False
currentEdict = ""

def edictNeed(year,foodChange):
  global influence, foodConsumption, edictEndYear, edictInEffect, currentEdict, childRestrict
  if foodChange < 0 and influence >= 500 and edictInEffect == False:
    influence -= 500
    foodConsumption = foodConsumption/2
    edictEndYear = year+10
    edictInEffect = True
    history.addEvents(leader.leader+" enacts the food rationing edict",year)
    currentEdict = "food rationing"
  return

def edictEnd(year):
  global influence, foodConsumption, edictEndYear, edictInEffect, currentEdict
  edictInEffect = False
  foodConsumption = 1.0
  edictEndYear = 0
  history.addEvents(leader.leader+" ends "+currentEdict+" edict",year)
  return