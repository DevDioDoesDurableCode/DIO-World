maplen = 50
mapping = [(i,j) for i in range(maplen) for j in range(maplen)]
stuffmap = [[" "for i in range(maplen)]for j in range(maplen)]
foodmap = [[" "for i in range(maplen)]for j in range(maplen)]
minemap = [[" "for i in range(maplen)]for j in range(maplen)]
housemap = [[" "for i in range(maplen)]for j in range(maplen)]
lodgemap = [[" "for i in range(maplen)]for j in range(maplen)]
extramap = [[" "for i in range(maplen)]for j in range(maplen)]


landFeatures = ["Ore Deposit","Fertile Land","Dirt"]

def generateWhiteNoise(width,height):
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
          choose = random.randint(0,2)
          if choose == 0:
            noise[i][j] = "Ore Deposit"
          if choose == 1:
            noise[i][j] = "Fertile Land"
          if choose == 2:
            noise[i][j] = "Dirt"

    return noise

def genMapContent():
  return