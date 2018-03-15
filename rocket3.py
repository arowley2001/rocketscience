from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer

earth = Planet(planetmass=0)  # no gravity to simplify things

RocketStarted = False
StartTime = None    # to keep track of when burn started
BurnTime = 0        # keep track of how much time the burn has lasted

# Falcon F9R specifications
me = 25600          # Empty mass
mp =  395700        # Propellent mass
F1D = 716000        # Single engine thrust (Newtons)
N1D = 9             # Number of rocket engines
