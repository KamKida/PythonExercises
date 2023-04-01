import random

from enum import Enum

def findApproximateValue(value, percentRange):
    lowestValue = value - ((percentRange / 100) * value)
    highestValue = value + ((percentRange / 100) * value)
    return random.randint(lowestValue, highestValue)

Event = Enum("Event", ["Chest", "Empty"])

eventDictionary ={
                Event.Chest: 0.6,
                Event.Empty: 0.4}
                
eventList = tuple(eventDictionary. keys())
eventProbability = tuple(eventDictionary.values())

Colors = Enum("Colors", {"Green" : "zielona",
                        "Orange" : "pomarańczowy",
                        "Purple" : "fioletowy",
                        "Gold": "złoty"
                        }
              )

chestColorsDictionary = {
                            Colors.Green: 0.75,
                            Colors.Orange: 0.2,
                            Colors.Purple : 0.04,
                            Colors.Gold : 0.01
                            }

chestColorList = tuple(chestColorsDictionary.keys())
chestColorProbability = tuple(chestColorsDictionary.values())

rewardsForChests= {
                    chestColorList[reward]:(reward + 1) * (reward + 1) * 1000
                    for reward in range(len(chestColorList))
                    }

gameLength = 5
goldAcquired  = 0

print("Welcome to my game called 'UNDERGROUND'.\n"
      "Your goal is to get as much gold as possible\n")
print("You have only 5 steps to make\n"
      "!!!CHOICE WISELY!!!\n")

while gameLength >0:
    gamerAnswer = input("Do you wanna go forward: ")
    
    if (gamerAnswer == "yes"):
        print("Great lets see what you got... ")
        drawnEvent = random.choices(eventList, eventProbability)[0]
        

        if (drawnEvent == Event.Chest):
            print("You have drawn a CHEST")
            drawnColor = random.choices(chestColorList, chestColorProbability)[0]
            print("The chest color is ",drawnColor.value)
            
            gamerReward = findApproximateValue(rewardsForChests[drawnColor], 10)
            goldAcquired = goldAcquired + gamerReward
        
        elif (drawnEvent == Event.Empty):
            print("You have drawn NOTHING")

    else:
        print("You can only MOVE FORWARD!")
        continue
    gameLength -= 1

print("Congratulation,you acquired  ",goldAcquired," of gold")