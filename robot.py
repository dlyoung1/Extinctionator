import curses
import RPi.GPIO as GPIO
import time
import pigpio

#set GPIO mode
GPIO.setmode(GPIO.BOARD)

#define dc motor output pins
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#pigpio
pi = pigpio.pi()

#claw
pi.set_mode(10, pigpio.OUTPUT)
claw = 1500

#turret servo
pi.set_mode(7, pigpio.OUTPUT)
tilt = 1500

#stepper assignment
ControlPin = [21, 22, 23, 24]
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
seq = [ [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1] ]

#laser pin
GPIO.setup(29, GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        pi.set_servo_pulsewidth(7, tilt)
        pi.set_servo_pulsewidth(10, claw)
        
#exit the program
        if char == ord('q'):
            break
        
#move vehicle forward
        elif char == curses.KEY_UP:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)

#move vehicle backward
        elif char == curses.KEY_DOWN:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)

#move vehicle right
        elif char == curses.KEY_RIGHT:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)

#move vehicle left
        elif char == curses.KEY_LEFT:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)

#stop vehicle                
        elif char == 10:
            GPIO.output(7, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
     
#evasive maneuver
        elif char == ord('d'):
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
            
            time.sleep(.5)
            
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            
            time.sleep(.5)
            
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            
            time.sleep(.5)
            
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
            
            time.sleep(.5)
            
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            
            time.sleep(.5)

#operation  of claw            
        elif char == ord('c'):
            claw += 10
            
        elif char == ord('x'):
            claw -= 10
       
#turret pan
        elif char == ord('p'):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                    print(ControlPin[pin])
                    print(seq[halfstep][pin])
                time.sleep(0.001)
        
        elif char == ord('o'):
            for halfstep in range(8 - 1, -1, -1):
                for pin in range(4 - 1, -1, -1):
                    print(ControlPin[pin])
                    print(seq[halfstep][pin])
                    GPIO.output(ControlPin[pin], seq[halfstep][pin])                   
                time.sleep(0.001)

#turret tilt servo
        elif char == ord('u'):
            tilt -= 1
            
        elif char == ord('i'):
            tilt += 1

#laser on/off
        elif char == ord('l'):
            GPIO.output(29, GPIO.HIGH)
        
        elif char == ord('k'):
            GPIO.output(29, GPIO.LOW)
            
finally:
    # Close down curses, turn echo back on, stop pigpio, cleanup gpio
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    pi.stop()
    GPIO.cleanup()
            