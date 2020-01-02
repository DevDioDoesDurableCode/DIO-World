import history
import random

firstNamePart = ["Black","Yellow","Red"]
lastNamePart = ["Plague","Fever","Flu"]
diseaseName = ""

deadlyness = 0
infectivity = 0

def diseaseGenerate(year):
  global firstNamePart, lastNamePart, diseaseName, deadlyness, infectivity
  diseaseName = firstNamePart[random.randint(0,len(firstNamePart))]+" "+lastNamePart[random.randint(0,len(lastNamePart))]
  history.addEvents("The "+diseaseName+" as appeared", year)
  deadlyness = random.randint(0,100)
  return