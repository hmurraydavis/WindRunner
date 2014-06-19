# First we must import PyBBIO: 
#from bbio import *
import bbio

# Then we can import Servo:
#from Servo import *
import Servo

# Create an instance of the Servo object:
servostear = Servo.Servo(bbio.PWM1A)
servosail=Servo.Servo(bbio.PWM2A)
# We could have left out the PWM pin here and used 
# Servo.attach(PWM1A) in setup() instead.

def setup():
  # Nothing to do here
  pass

def movesail(angle):
	servosail.write(angle)

def movestear(angle):
	servostear.write(angle)

def loop():
	sailang=22
	stearang=22

	movesail(sailang)
	movestear(stearang)

#  for angle in range(180, 0, -1):  # 180-0 degrees
#    servostear.write(angle)
#    bbio.delay(15)

bbio.run(setup, loop)
