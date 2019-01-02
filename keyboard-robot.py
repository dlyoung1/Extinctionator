import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
pwm = GPIO.PWM(19, 50)
pwm.start(7)
position = 7

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        
#exit the program
        if char == ord('q'):
            break
        
#move vehicle forward, backward, right, and left
        elif char == curses.KEY_UP:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            
        elif char == curses.KEY_DOWN:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
            
        elif char == curses.KEY_RIGHT:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
            
        elif char == curses.KEY_LEFT:
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)

#operation  of claw            
        elif char == ord('o'):
            position += .1
            pwm.ChangeDutyCycle(position)
            print(position)
            
        elif char == ord('p'):
            position -= .1
            pwm.ChangeDutyCycle(position)
            print(position)
            
#fancy dance move
        elif char == ord('d'):
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            
            time.sleep(.5)
            
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
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
            
            time.sleep(.5)
            
        elif char == 10:
            GPIO.output(7, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
finally:
    # Close down curses properly, inc turn echo back on
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
            




