from random import randint
from math import sqrt

class Rocket:
   

    def __init__(self, speed = 1, altitude = 0, x = 0) :
        self.altitude = altitude

        self.speed = speed
        self.x = x

    def moveUp(self):
        """Porusza się do góry (altitude) o prędkość (speed)
        """
        self.altitude += self.speed
    
    def __str__(self) :
        return "Rakieta jest na wysokości: " + str(self.altitude)
    
    

class RocketBoard:

    def __init__(self, amountOFrockets = 5) :
        self.rockets = [Rocket(randint(1,6)) for _ in range(amountOFrockets) ]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()


        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]
    
    def __setitem__(self,key,value):
        self.rockets[key].altitude = value

    
    @staticmethod
    def getDistance( rocket1: Rocket, rocket2: Rocket ) -> float:
    

        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2

        return sqrt(ab + bc)
    def __len__(self):
        return len(self.rockets)
        