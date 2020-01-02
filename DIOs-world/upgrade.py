
upgradeCap = 9
farmLevel = 0
resource = 0
science = 0
farmUpgrade = 10
mineLevel = 0
mineUpgrade = 10
houseUpgrade = 50
houseLevel = 0
lodgeLevel = 0
lodgeUpgrade = 10
fStorageUpgrade = 0
fStorageLevel = 0
rStorageUpgrade = 0
rStorageLevel = 0

farmLevelNames = ["Primitive Garden","Small Berry Bush", "Berry Bushes","Berry Plantation", "Wheat Crop", "Wheat Farm", "Wheat Plantation", "Potato Crop", "Potato Farm", "Potato Plantation"]
farmLevelStats = [4,8,12,16,20,24,28,32,36,40]

mineLevelNames = ["Ore filled rock","Small Copper Mine","Copper Mine","Large Copper Mine","Small Iron Mine", "Iron Mine", "Large Iron Mine", "Small Gold Mine", "Gold Mine","Large Gold Mine"]
mineLevelStats = [1,2,4,6,8,10,12,14,16,20]

houseLevelNames = ["Small hut","Hut","Large Hut","Small Longhouse","Longhouse","Large Longhouse","Small House","House","Large House","Apartment"]
houseLevelStats = [4,8,12,16,20,24,28,32,36,40]

lodgeLevelNames = ["Lean-To","Small Hunting Tent","Hunting Tent","Large Hunting Tent", "Small Hunter's Cabin", "Hunter's Cabin", "Large Hunting Cabin","Small Lodge", "Lodge","Large lodge"]
lodgeLevelStats = [1,2,4,6,8,10,12,14,16,20]

farmOutdatedList = {}
mineOutdatedList = {}
lodgeOutdatedList = {}
houseOutdatedList = {}


def upgradePlaces(science, resource):
  global farmLevel,farmUpgrade,mineLevel,mineUpgrade,houseUpgrade,houseLevel,fStorageUpgrade,fStorageLevel,rStorageUpgrade,rStorageLevel, upgradeCap,lodgeLevel, lodgeUpgrade
  if science >= farmUpgrade and resource >= farmUpgrade and upgradeCap > farmLevel:
    farmLevel += 1
    resource -= farmUpgrade
    science -= farmUpgrade
    farmUpgrade += 10
    farmOutdatedList[len(farmOutdatedList)] = str(farmLevelNames[farmLevel-1])
  elif science >= mineUpgrade and resource >= mineUpgrade and upgradeCap > mineLevel:
    mineLevel += 1
    resource -= mineUpgrade
    science -= mineUpgrade
    mineUpgrade += 10
    mineOutdatedList[len(mineOutdatedList)] = str(mineLevelNames[mineLevel-1])
  elif science >= lodgeUpgrade and resource >= lodgeUpgrade and upgradeCap > lodgeLevel:
    lodgeLevel += 1
    resource -= lodgeUpgrade
    science -= lodgeUpgrade
    lodgeUpgrade += 10
    lodgeOutdatedList[len(lodgeOutdatedList)] = str(lodgeLevelNames[lodgeLevel-1])
  elif science >= houseUpgrade and resource >= houseUpgrade and upgradeCap > houseLevel:
    houseLevel += 1
    resource -= houseUpgrade
    science -= houseUpgrade
    houseUpgrade += 100
    houseOutdatedList[len(houseOutdatedList)] = str(houseLevelNames[houseLevel-1])
  elif science >= fStorageUpgrade and resource >= fStorageUpgrade and upgradeCap >    fStorageLevel:
    fStorageLevel += 1
    resource -= fStorageUpgrade
    science -= fStorageUpgrade
    fStorageUpgrade += 10
  elif science >= rStorageUpgrade and resource >= rStorageUpgrade and upgradeCap > rStorageLevel:
    rStorageLevel += 1
    resource -= rStorageUpgrade
    science -= rStorageUpgrade
    rStorageUpgrade += 10

def buildingFarmName():
  global farmLevel, farmLevelNames
  return farmLevelNames[farmLevel]

def buildingFarmStats():
  global farmLevel, farmLevelStats
  return farmLevelStats[farmLevel]

def buildingMineName():
  global mineLevel, mineLevelNames
  return mineLevelNames[mineLevel]

def buildingMineStats():
  global mineLevel, mineLevelStats
  return mineLevelStats[mineLevel]

def buildingHouseName():
  global houseLevel, houseLevelNames
  return houseLevelNames[houseLevel]

def buildingHouseStats():
  global houseLevel, houseLevelStats
  return houseLevelStats[houseLevel]

def buildingLodgeName():
  global lodgeLevel, lodgeLevelNames
  return lodgeLevelNames[lodgeLevel]

def buildingLodgeStats():
  global lodgeLevel, lodgeLevelStats
  return lodgeLevelStats[lodgeLevel]

def rStoragePull():
  global rStorageLevel
  return rStorageLevel

def fStoragePull():
  global fStorageLevel
  return fStorageLevel

def farmScanUpgrade(stuffmap, maplen):
  global farmLevelNames, farmOutdatedList, farmLevel
  addedProduction = 0
  mapPeekX = 0
  mapPeekY = 0
  while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
    for i in range(0, len(farmOutdatedList)):
      if stuffmap[mapPeekY][mapPeekX] == farmOutdatedList[i]:
        stuffmap[mapPeekY][mapPeekX] = farmLevelNames[farmLevel]
        addedProduction += farmLevelStats[farmLevel] - farmLevelStats[i]
    mapPeekX += 1
    if mapPeekX >= maplen:
      mapPeekX = 0
      mapPeekY += 1
  return addedProduction

def mineScanUpgrade(stuffmap, maplen):
  global mineLevelNames, mineOutdatedList, mineLevel
  addedProduction = 0
  mapPeekX = 0
  mapPeekY = 0
  while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
    for i in range(0, len(mineOutdatedList)):
      if stuffmap[mapPeekY][mapPeekX] == mineOutdatedList[i]:
        stuffmap[mapPeekY][mapPeekX] = mineLevelNames[mineLevel]
        addedProduction += mineLevelStats[mineLevel] - mineLevelStats[i]
    mapPeekX += 1
    if mapPeekX >= maplen:
      mapPeekX = 0
      mapPeekY += 1
  return addedProduction

def houseScanUpgrade(stuffmap, maplen):
  global houseLevelNames, houseOutdatedList, houseLevel
  addedProduction = 0
  mapPeekX = 0
  mapPeekY = 0
  while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
    for i in range(0, len(houseOutdatedList)):
      if stuffmap[mapPeekY][mapPeekX] == houseOutdatedList[i]:
        stuffmap[mapPeekY][mapPeekX] = houseLevelNames[houseLevel]
        addedProduction += houseLevelStats[houseLevel] - houseLevelStats[i]
    mapPeekX += 1
    if mapPeekX >= maplen:
      mapPeekX = 0
      mapPeekY += 1
  return addedProduction

def lodgeScanUpgrade(stuffmap, maplen):
  global lodgeLevelNames, lodgeOutdatedList, lodgeLevel
  addedProduction = 0
  mapPeekX = 0
  mapPeekY = 0
  while stuffmap[mapPeekY][mapPeekX] is not " " and mapPeekX*mapPeekY is not maplen*maplen:
    for i in range(0, len(lodgeOutdatedList)):
      if stuffmap[mapPeekY][mapPeekX] == lodgeOutdatedList[i]:
        stuffmap[mapPeekY][mapPeekX] = lodgeLevelNames[lodgeLevel]
        addedProduction += lodgeLevelStats[lodgeLevel] - lodgeLevelStats[i]
    mapPeekX += 1
    if mapPeekX >= maplen:
      mapPeekX = 0
      mapPeekY += 1
  return addedProduction
