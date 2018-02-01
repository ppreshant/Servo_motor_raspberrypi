#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

PWMFreq = 50    # # Set frequency to 50 Hz ¬ 20 msec pulse
##servoMin = 4095 * PWMFreq/1000  # Min pulse length out of 4096 ¬ 1 msec
servoMin = 100
##servoMax = 2*servoMin  # Max pulse length out of 4096 ¬ 2 msec
servoMax = 800
pulse_increment = 5                      # 20 => increment in 9 degrees angle every iteration


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= PWMFreq                  # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(PWMFreq)                        # Set frequency to 50 Hz ¬ 10 msec pulse
##setServoPulse(0,2)
##setServoPulse(3,2)

##pwm.setPWM(0, 0, servoMax)                 # set angle at zero - pulse width = 1 msec
##pwm.setPWM(2, 0, servoMax)


##time.sleep(1)
tinit = time.time()

i = 0
servoset1 = servoMax
servoset2 = servoMax

while (max(servoset1,servoset2) > servoMin):
  # Change speed of continuous servo on channel O
  servoset1 = servoMax - i * pulse_increment/2
  servoset2 = servoMax - i * pulse_increment/2 
  
  pwm.setPWM(0, 0, servoset1)
  pwm.setPWM(2, 0, servoset2)
  
  time.sleep(.02)
  i = i + 1


tfinal = time.time()
print tfinal - tinit


