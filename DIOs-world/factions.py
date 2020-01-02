from random import randint
from random import random

factionNames = [[""],[""],[""],[""],[""],[""]]
factionNameFirstPart = [["The"],["The"],["The"],["The"],["Peace"],["Reality"]]
factionNameLastPart = [["Mathmatists"],["Imperialists"],["Unifiers"],["Dominators"],["Corp"],["Anchors"]]
factionTypes = ["spirtualist","authoritarian","egalitarian","militarist","pacifist","materialist"]
factionPop = [1,1,1,1,1,1]
factionAttraction = [1,1,1,1,1,1]
factionChance = [0,0,0,0,0,0]
factionPercent = [0,0,0,0,0,0]
factionTotal = 0

def factionGen():
  global factionNames, factionNameFirstPart, factionNameLastPart, factionAttraction
  switch = False
  select = 0
  for i in range(0, len(factionNames)):
    if factionNames[i] == "":
      switch = True
  while switch == True:
    select = randint(0, len(factionNames))
    if factionNames[select] == "":
      switch = False
      factionNames[select] = factionNameFirstPart[select][randint(0,len(factionNameFirstPart[select])-1)]+" "+factionNameLastPart[select][randint(0,len(factionNameLastPart[select])-1)]    
  return

def factionSupport(pop,ethics):
  global factionPop, factionTotal, factionAttraction, factionChance, factionPercent
  tempFactionTotal = 0
  choose = 0.0
  for i in range(0,len(factionAttraction)):
    factionAttraction[i] = 1
    if factionAttraction[i] is ethics:
      factionAttraction[i] = 2
  for i in range(0,len(factionPop)):
    factionChance[i] = factionPop[i]*factionAttraction[i]
  tempFactionTotal = factionChance[0]+factionChance[1]+factionChance[2]+factionChance[3]+factionChance[4]+factionChance[5]
  for i in range(0, len(factionPercent)):
    factionPercent[i] = factionChance[i]/tempFactionTotal
    factionChance[i] = int(factionPercent[i]*10)
  factionChance.sort()
  if (pop-factionTotal)>0:
    choose = randint(0,100)
    if choose >= 0 and choose < factionChance[0]:
      factionTotal += 1
      factionPop[0] += 1
    if choose >= factionChance[0] and choose < factionChance[0]+factionChance[1]:
      factionTotal += 1
      factionPop[1] += 1
    if choose >= factionChance[0]+factionChance[1] and choose < factionChance[0]+factionChance[1]+factionChance[2]:
      factionTotal += 1
      factionPop[2] += 1
    if choose >= factionChance[0]+factionChance[1]+factionChance[2] and choose < factionChance[0]+factionChance[1]+factionChance[2]+factionChance[3]:
      factionTotal += 1
      factionPop[3] += 1
    if choose >= factionChance[0]+factionChance[1]+factionChance[2]+factionChance[3] and choose < factionChance[0]+factionChance[1]+factionChance[2]+factionChance[3]+factionChance[4]:
      factionTotal += 1
      factionPop[4] += 1
    if choose >= factionChance[0]+factionChance[1]+factionChance[2]+factionChance[3]+factionChance[4] and choose < factionChance[0]+factionChance[1]+factionChance[2]+factionChance[3]+factionChance[4]+factionChance[5]:
      factionTotal += 1
      factionPop[5] += 1

    # for i in range(0, (pop-factionTotal)):
    #   factionPop[randint(0,len(factionPop)-1)] += 1
    #   factionTotal += 1
  return