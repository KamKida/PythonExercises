from rocket import Rocket, RocketBoard
from random import randint

rocket1 = Rocket(altitude= 4)
rocket2 = Rocket()

print(RocketBoard.getDistance(rocket1, rocket2))

