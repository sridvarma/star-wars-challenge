import requests
from pprint import pprint


def inReturnOfJedi(spaceShip): # helper method 
    inJedi  = False
    filmRequestArr = spaceShip["films"]
    for req in filmRequestArr:
        currData = requests.get(req).json()
        if currData["title"] == "Return of the Jedi":
            inJedi = True
    return inJedi
def isValidCrewSize(spaceShip): # helper method 
        currCrewString = spaceShip["crew"]
        if currCrewString == "unknown":
            return False
        if "," in currCrewString: # commas indicate 4 digit numbers, which are greater than a 100
            return False
        if "-" in currCrewString: 
            crewSizes = currCrewString.split("-")
            if int(crewSizes[0]) < 3 or int(crewSizes[1]) > 100: # if lower range is less than 3, or upper range greater than 100, this ship has an invalid crew size 
                return False
        else:
            if int(currCrewString) < 3 or int(currCrewString) > 100:
                return
        return True
def isValidHyperDriveRating(spaceShip): #helper method 
    ratingString = (spaceShip["hyperdrive_rating"])
    if ratingString == "unknown":
        return False
    if float(ratingString) < 1.0:
        return False
    return True



currPageUrl = "https://swapi.dev/api/starships/?page=1"
hasNextPage = True
r = requests.get(currPageUrl)

crewsArr = []
ratingsArr = []
jediArr = []

while hasNextPage:
    currData = requests.get(currPageUrl).json()

    spaceShipArr = currData["results"]
    if currData["next"] == None:
        hasNextPage = False
    else:
        currPageUrl = currData["next"]
    
    for spaceship in spaceShipArr: 
        if isValidCrewSize(spaceship):
            crewsArr.append(spaceship)
        if isValidHyperDriveRating(spaceship):
            ratingsArr.append(spaceship)
        if inReturnOfJedi(spaceship):
            jediArr.append(spaceship)

print("Below are the spaceships that appeared in the Return of the Jedi")
pprint(jediArr)
print("Below are all ships that have a hyperdrive rating >= 1.0")
pprint(ratingsArr)
print("Below are all ships that have crews between 3 and 100 (inclusive)")
pprint(crewsArr)
