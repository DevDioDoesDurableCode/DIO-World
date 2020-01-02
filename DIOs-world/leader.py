from random import randint
import history
leader = ""
leaderFarmEffect = 1
leaderMineEffect = 1
leaderLodgeEffect = 1
leadarBuildEffect = 1
leaderScienceEffect = 1
leaderExperience = 0
leaderLevelUpMod = 0
deathYear = 0

leaderNameListFirst = ["John","Johnne","Sam","Leman","Angus","Mia","Cat","Jim","Rogal","Trey","Chris","Tyler","Caleb","Kal","Leeroy","Kelby"]

leaderNameListLast = ["Smith","Hanson","Kern","McFife","Russ","Dorn","White","Monson","Turner","LeMarr","Swallow","Barkdull","Jenkins"]

goodTraitNameList = ["Farmer Experience","Miner Experience","Hunter Experience","Builder Experience","Scientist Experience"]

goodTraitStatsList = [[2,0,0,0,0],[0,2,0,0,0],[0,0,2,0,0],[0,0,0,2,0],[0,0,0,0,2]]

goodTraitStatsListMarker = 0

def leaderGen(year):
  global leader, leaderFarmEffect, leaderMineEffect, leaderLodgeEffect, leadarBuildEffect, leaderScienceEffect, deathYear
  leader = ""
  leaderFarmEffect = 1
  leaderMineEffect = 1
  leaderLodgeEffect = 1
  leadarBuildEffect = 1
  leaderScienceEffect = 1
  leaderExperience = 0
  deathYear = 0
  leader = leaderNameListFirst[randint(0, len(leaderNameListFirst)-1)]+" "+leaderNameListLast[randint(0, len(leaderNameListLast)-1)]
  if leader == "Leman Russ":
    leaderFarmEffect += 500
    leaderMineEffect += 500
    leaderLodgeEffect += 2000
    leadarBuildEffect += 1000
    leaderScienceEffect += 500
    deathYear = year+1000
    history.addEvents((leader+" arrives to lead us all."),year)
  elif leader == "Rogal Dorn":
    leaderFarmEffect += 500
    leaderMineEffect += 1000
    leaderLodgeEffect += 500
    leadarBuildEffect += 2000
    leaderScienceEffect += 500
    deathYear = year+1000
    history.addEvents((leader+" arrives to lead us all."),year)
  elif leader == "Angus McFife":
    leader = "Angus McFife XIII"
    leaderFarmEffect += 1000
    leaderMineEffect += 1000
    leaderLodgeEffect += 1000
    leadarBuildEffect += 1000
    leaderScienceEffect += 1000
    deathYear = year+1000
    history.addEvents((leader+" arrives to lead us all."),year)
  elif leader == "Leeroy Jenkins":
    leaderFarmEffect -= 1000
    leaderMineEffect -= 1000
    leaderLodgeEffect -= 1000
    leadarBuildEffect -= 1000
    leaderScienceEffect -= 1000
    deathYear = year+1
    history.addEvents(("LEEERRRRRROOOOYYYY JEEEEEENNNNNNKKKKIIIINNNS"),year)
  else:
    goodTraitStatsListMarker = randint(0, len(goodTraitStatsList)-1)
    leaderFarmEffect += goodTraitStatsList[goodTraitStatsListMarker][0]
    leaderMineEffect += goodTraitStatsList[goodTraitStatsListMarker][1]
    leaderLodgeEffect += goodTraitStatsList[goodTraitStatsListMarker][2]
    leadarBuildEffect += goodTraitStatsList[goodTraitStatsListMarker][3]
    leaderScienceEffect += goodTraitStatsList[goodTraitStatsListMarker][4]
    deathYear = year+randint(50,80)
    history.addEvents((leader+" rises to power."),year)
  return

def leaderLevelUp(year):
  global leaderExperience, leaderLevelUpMod,leader, leaderFarmEffect, leaderMineEffect, leaderLodgeEffect, leadarBuildEffect, leaderScienceEffect
  leaderExperience = 0
  leaderLevelUpMod += 1
  goodTraitStatsListMarker = randint(0, len(goodTraitStatsList)-1)
  leaderFarmEffect += goodTraitStatsList[goodTraitStatsListMarker][0]
  leaderMineEffect += goodTraitStatsList[goodTraitStatsListMarker][1]
  leaderLodgeEffect += goodTraitStatsList[goodTraitStatsListMarker][2]
  leadarBuildEffect += goodTraitStatsList[goodTraitStatsListMarker][3]
  leaderScienceEffect += goodTraitStatsList[goodTraitStatsListMarker][4]
  history.addEvents((leader+" gains the "+goodTraitNameList[goodTraitStatsListMarker]+" trait."),year)
  return