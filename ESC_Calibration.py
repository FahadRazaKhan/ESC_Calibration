import pigpio
import RPi.GPIO as GPIO
import time
import os
os.system('sudo pigpiod')
time.sleep(1)

ESC1 = 23
ESC2 = 27

pi = pigpio.pi()

print('Starting Calibration')

pi.set_servo_pulsewidth(ESC1,1000) # Min. Throttle
pi.set_servo_pulsewidth(ESC2,1000) # Min. Throttle
time.sleep(2)

pi.set_servo_pulsewidth(ESC1,2000) # Max. Throttle
pi.set_servo_pulsewidth(ESC2,2000) # Max. Throttle
time.sleep(2)

pi.set_servo_pulsewidth(ESC1,1100) # Slightly open throttle
pi.set_servo_pulsewidth(ESC2,1100) # Slightly open throttle
time.sleep(2)

pi.set_servo_pulsewidth(ESC1,0)
pi.set_servo_pulsewidth(ESC2,0)


print('E.S.C Calibrated')
time.sleep(1)

print("I'm Starting the motor, I hope it's calibrated and armed, if not restart")
time.sleep(1)
speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
print("Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed")
try:
    while True:
        pi.set_servo_pulsewidth(ESC1, speed)
        pi.set_servo_pulsewidth(ESC2, speed)
        inp = input()
        
        if inp == "q":
            speed -= 100    # decrementing the speed like hell
            print("speed = %d" % speed)
        elif inp == "e":    
            speed += 100    # incrementing the speed like hell
            print("speed = %d" % speed)
        elif inp == "d":
            speed += 10     # incrementing the speed 
            print("speed = %d" % speed)
        elif inp == "a":
            speed -= 10     # decrementing the speed
            print("speed = %d" % speed)
        
        else:
            print("WHAT DID I SAY!! Press a,q,d or e")

except KeyboardInterrupt:

    pi.set_servo_pulsewidth(ESC1,0)
    pi.set_servo_pulsewidth(ESC2,0)
    time.sleep(0.4)
    pi.stop()
    GPIO.cleanup()
    time.sleep(0.5)
    print('Motor Stopped')
    
