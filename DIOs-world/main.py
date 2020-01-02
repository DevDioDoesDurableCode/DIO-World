import time
import upgrade
import maps
import leader
import history
import edicts
import factions
from random import randint 
import random
import math


farmers = int(input("How many farmers: "))
miners = int(input("How many miners: "))
hunters = int(input("How many hunters: "))
scientist = int(input("How many scientists: "))
builder = int(input("How many builders: "))

children = 0
childGrowingTimer = [[" "for i in range(3)]for j in range(36)]
childGrowingMarker = 0
pop = farmers + miners + scientist + builder + hunters
popGrowTimer = int(279*float(input("How fast do they reproduce?(i.e .5x, 1x, 1.5x, etc): ")))
adultTimer = int(input("How long does it take to mature?(18 years is normal)"))
maxChildren = int(input("Max ammount of children per person: "))
targetPop = int(input("What is the target population?: "))

maplen = int(input("Size of map (50 is normal): "))
mapping = [(i,j) for i in range(maplen) for j in range(maplen)]
stuffmap = [[" "for i in range(maplen)]for j in range(maplen)]
mapPeekX = 0
mapPeekY = 0

diseaseTime = 365
popHappyness = 100.0

popGrowTimerSeter = popGrowTimer
houseCounter = 2
food = int(input("Starting food: "))
foodPrev = 0
foodChange = 0
foodStorage = 1000
resource = int(input("Starting resources: "))
resourceStorage = 1000
science = 0
edicts.influence = int(input("Starting influence: "))
edicts.influenceStorage = 1000
fStorageLevel = 1
rStorageLevel = 1
day = 0
year = 0
season = "Summer"
farms = farmers

house = int(pop/4)+1
mining = miners
lodge = hunters
FarmProduction = farms
MineProduction = mining
HouseRoom = 4*house
LodgeProduction = lodge
townSize = farms + house + mining+lodge
freeSlots = 0
alive = True
leader.leaderGen(year)
deadPeople = 0

ethicsList = ["Spiritualist","Authoritarian","Egalitarian","Militarist","Pacifist","Materialist"]
for i in range(0, len(ethicsList)):
  print(ethicsList[i])
ethics = str(input("Choose ethic: ")).lower()


while alive == True:
  day += 1
  if day >= 365:
    day = 1
    year += 1
    leader.leaderExperience += int(pop/10)
    if deadPeople >= 1:
      history.addEvents(str(deadPeople)+" died this year.",year)
    deadPeople = 0
    print("Year: "+str(year)+" | Population: "+str(pop)+"| Children: "+str(children)+" | Happiness: "+str(popHappyness)+"%")
    time.sleep(.1)
  if season == "Spring":
    if food+(FarmProduction * 2) <= foodStorage*upgrade.fStorageLevel and farmers > 0:
      food -= food-foodStorage
    if farmers > 0:
      food += int((FarmProduction * 2)*(farmers/farms))*leader.leaderFarmEffect+int(children/10)
    food += LodgeProduction
  if season == "Summer":
    if food+(FarmProduction * 3) <= foodStorage*upgrade.fStorageLevel and farmers > 0:
      food -= food-foodStorage
    if farmers > 0:
      food += int((FarmProduction * 3)*(farmers/farms))*leader.leaderFarmEffect+int(children/10)
    food += LodgeProduction*2
  if season == "Fall":
    if food+(farms*(FarmProduction * 2)) >= foodStorage*upgrade.fStorageLevel and farmers > 0:
      food -= food-foodStorage
    if farmers > 0:
      food += int((FarmProduction * 2)*(farmers/farms))*leader.leaderFarmEffect+int(children/10)
    food += LodgeProduction
  if season == "Winter":
    food = food
    food += hunters*leader.leaderLodgeEffect
  if day >= 1 and day <= 91:
    season = "Summer"
  if day >= 92 and day <= 182:
    season = "Fall"
  if day >= 183 and day <= 273:
    season = "Winter"
  if day >= 274 and day <= 364:
    season = "Spring"
  if resource+MineProduction <= resourceStorage*upgrade.rStoragePull() and miners > 0:
    resource += MineProduction*leader.leaderMineEffect
    resource += 1
  science += scientist*leader.leaderScienceEffect
  popGrowTimer -= 1
  choose = randint(0,15)
  if popGrowTimer <= 0 and childGrowingMarker is not len(childGrowingTimer) and int((pop*maxChildren)-(int(pop/2)+children))>0:
    if choose == 0:
      popGrowTimer = popGrowTimerSeter
      children += int(pop/2)
      childGrowingTimer[childGrowingMarker] = [year+adultTimer,day,int(pop/2)]
      childGrowingMarker += 1
    else:
      popGrowTimer = popGrowTimerSeter
    
  for i in range(0, len(childGrowingTimer)-1):
    if childGrowingTimer[i][0] == year and childGrowingTimer[i][1] == day:
      for j in range(0, childGrowingTimer[i][2]):
        if farmers > miners:
          choose = randint(0,4)
          if  choose == 0:
            miners += 1
          elif choose == 1:
            farmers += 1
          elif choose == 2:
            scientist += 1
          elif choose == 3:
            builder += 1
          else:
            hunters += 1
        else:
          farmers += 1 
        if popHappyness < 100.0:
          popHappyness += .1
        children -= 1
      del childGrowingTimer[i]
      for y in range(0,len(childGrowingTimer)-(i+1)):
        childGrowingTimer[i+y] = childGrowingTimer[i+y+1]
      childGrowingMarker -= 1
      pop = farmers + miners + scientist + builder + hunters

  foodPrev = food
  food -= int((pop + int(children/4))*edicts.foodConsumption)
  foodChange = food-foodPrev
  if food < 0:
    choose = randint(0,8)
    if choose == 0 and miners > 0 and pop > 0:
      miners -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died of starvation.",year)
        leader.leaderGen(year)
    elif choose == 1 and farmers > 0 and pop > 0:
      farmers -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died of starvation.",year)
        leader.leaderGen(year)
    elif choose == 2 and scientist > 0 and pop > 0:
      scientist -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died of starvation.",year)
        leader.leaderGen(year)
    elif choose == 3 and builder > 0 and pop > 0:
      builder -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died of starvation.",year)
        leader.leaderGen(year)
    elif choose == 4 and hunters > 0 and pop > 0:
      hunters -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died of starvation.",year)
        leader.leaderGen(year)
    if randint(0,10) == 0:      
      choose = randint(0,8)
      for i in range(0, int(pop/10)):
        if choose == 0  and miners > 0 and pop > 0:
          miners -= 1
          pop -= 1
          deadPeople += 1
          if pop > 0:
            popHappyness -= .1/pop
          if randint(0,pop) == 0:
            history.addEvents((leader.leader)+" has died of starvation.",year)
            leader.leaderGen(year)
        elif choose == 1  and farmers > 0 and pop > 0:
          farmers -= 1
          pop -= 1
          deadPeople += 1
          if pop > 0:
            popHappyness -= .1/pop
          if randint(0,pop) == 0:
            history.addEvents((leader.leader)+" has died of starvation.",year)
            leader.leaderGen(year)
        elif choose == 2  and scientist > 0 and pop > 0:
          scientist -= 1
          pop -= 1
          deadPeople += 1
          if pop > 0:
            popHappyness -= .1/pop
          if randint(0,pop) == 0:
            history.addEvents((leader.leader)+" has died of starvation.",year)
            leader.leaderGen(year)
        elif choose == 3  and builder > 0 and pop > 0:
          builder -= 1
          pop -= 1
          deadPeople += 1
          if pop > 0:
            popHappyness -= .1/pop
          if randint(0,pop) == 0:
            history.addEvents((leader.leader)+" has died of starvation.",year)
            leader.leaderGen(year)
        elif choose == 4 and hunters > 0 and pop > 0:
          hunters -= 1
          pop -= 1
          deadPeople += 1
          if pop > 0:
            popHappyness -= .1/pop
          if randint(0,pop) == 0:
            history.addEvents((leader.leader)+" has died of starvation.",year)
            leader.leaderGen(year)
        if pop <= 10:
          food += 20
    if pop <= 10:
      food += 20
  if pop-(HouseRoom) > 0 and season == "Winter":
    choose = randint(0,8)
    if choose == 0  and miners > 0 and pop > 0:
      miners -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died due to the elements.",year)
        leader.leaderGen(year)
    elif choose == 1  and farmers > 0 and pop > 0:
      farmers -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died due to the elements.",year)
        leader.leaderGen(year)
    elif choose == 2  and scientist > 0 and pop > 0:
      scientist -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died due to the elements.",year)
        leader.leaderGen(year)
    elif choose == 3  and builder > 0 and pop > 0:
      builder -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died due to the elements.",year)
        leader.leaderGen(year)
    elif choose == 4 and hunters > 0 and pop > 0:
      hunters -= 1
      pop -= 1
      deadPeople += 1
      if pop > 0:
        popHappyness -= .1/pop
      if randint(0,pop) == 0:
        history.addEvents((leader.leader)+" has died due to the elements.",year)
        leader.leaderGen(year)
    if pop <= 10:
      food += 20
    popHappyness -= .1/pop
  
  upgrade.upgradePlaces(science, resource)
  FarmProduction += upgrade.farmScanUpgrade(stuffmap, maplen)
  HouseRoom += upgrade.houseScanUpgrade(stuffmap, maplen)
  MineProduction += upgrade.mineScanUpgrade(stuffmap, maplen)
  LodgeProduction += upgrade.lodgeScanUpgrade(stuffmap, maplen)


  for i in range(0, (builder+1)*leader.leadarBuildEffect):
    freeSlots = townSize - (farms+mining+house+lodge)
    if freeSlots is 0 and resource >= 100:
      resource -= 100
      townSize += 1
      freeSlots += 1
    elif resource >= 200 and farms < farmers and freeSlots  is not 0:
      while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
        mapPeekX += 1
        if mapPeekX >= maplen:
          mapPeekX = 0
          mapPeekY += 1
      stuffmap[mapPeekY][mapPeekX] = str(upgrade.buildingFarmName())
      FarmProduction += int(upgrade.buildingFarmStats())
      mapPeekX = 0
      mapPeekY = 0
      resource -= 200
      farms += 1
      freeSlots -= 1
    elif resource >= 300 and pop > HouseRoom and freeSlots  is not 0: 
      while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
        mapPeekX += 1
        if mapPeekX >= maplen:
          mapPeekX = 0
          mapPeekY += 1
      stuffmap[mapPeekY][mapPeekX] = str(upgrade.buildingHouseName())
      HouseRoom += int(upgrade.buildingHouseStats())
      mapPeekX = 0
      mapPeekY = 0
      resource -= 300
      house += 1
      freeSlots -= 1
    elif resource >= 100 and lodge < hunters and freeSlots is not 0:
      while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
        mapPeekX += 1
        if mapPeekX >= maplen:
          mapPeekX = 0
          mapPeekY += 1
      stuffmap[mapPeekY][mapPeekX] = str(upgrade.buildingLodgeName())
      LodgeProduction += int(upgrade.buildingLodgeStats())
      mapPeekX = 0
      mapPeekY = 0
      resource -= 100
      lodge += 1
      freeSlots -= 1
    elif resource >= 400 and mining < miners+1 and freeSlots  is not 0:
      while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
        mapPeekX += 1
        if mapPeekX >= maplen:
          mapPeekX = 0
          mapPeekY += 1
      stuffmap[mapPeekY][mapPeekX] = str(upgrade.buildingMineName())
      MineProduction += int(upgrade.buildingMineStats())
      mapPeekX = 0
      mapPeekY = 0
      resource -= 40
      mining += 1
      freeSlots -= 1
  if leader.leaderExperience*leader.leaderLevelUpMod >= 100*leader.leaderLevelUpMod:
    leader.leaderLevelUp(year)
  if leader.deathYear == year:
    history.addEvents((leader.leader)+" has died due to old age.",year)
    leader.leaderGen(year)
  edicts.influence += int(pop/10)
  edicts.edictNeed(year, foodChange)
  if edicts.edictEndYear == year:
    edicts.edictEnd(year)
  if pop >= 100:
    factions.factionGen()
    factions.factionSupport(pop,ethics)
  #print("Year: "+str(year)+" Day: "+str(day)+" Season: "+season+" Food: "+str(food)+" Resources "+str(resource)+" Town Size: "+str(townSize)+" Population: "+str(pop)+" Miners: "+str(miners)+" Farmers: "+str(farmers)+" Scientists: "+str(scientist)+" Builders: "+str(builder)+" Hunters: "+str(hunters))
  if pop <= 0:
    alive = False
    
    print("Year: "+str(year)+" Day: "+str(day)+" Season: "+season+" Food: "+str(food)+" Resources "+str(resource)+" Town Size: "+str(townSize)+" Population: "+str(pop)+" Miners: "+str(miners)+" Farmers: "+str(farmers)+" Scientists: "+str(scientist)+" Builders: "+str(builder))
    for i in range(0, maplen):
      print(stuffmap[i])
    print("Houses: "+str(house))
    print("Mines: "+str(mining))
    print("Farms: "+str(farms))
    print("Everyone is dead")
    for i in range(0, len(history.events)):
      print(history.events[i])
    for i in range(0, len(factions.factionPop)):
      print(factions.factionTypes[i]+": "+str(factions.factionPop[i]))
    print(factions.factionTotal)  
  if pop >= targetPop:
    alive = False
    print("The population has reached the target")
    print("Year: "+str(year)+" Day: "+str(day)+" Season: "+season+" Food: "+str(food)+" Resources "+str(resource)+" Town Size: "+str(townSize)+" Population: "+str(pop)+" Miners: "+str(miners)+" Farmers: "+str(farmers)+" Scientists: "+str(scientist)+" Builders: "+str(builder))
    for i in range(0, maplen):
      print(stuffmap[i])
    print("Houses: "+str(house))
    print("Mines: "+str(mining))
    print("Farms: "+str(farms))
    for i in range(0, len(history.events)):
      print(history.events[i])
    for i in range(0, len(factions.factionPop)):
      print(factions.factionTypes[i]+": "+str(factions.factionPop[i]))
    print(ethics)
    print(factions.factionTotal)  
    if str(input("Do you want to continue? ")).lower() == "yes":
      targetPop = int(input("Set new population limit: "))
      alive = True
  #time.sleep(.1)
  