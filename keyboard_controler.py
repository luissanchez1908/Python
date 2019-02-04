# import curses
import curses
import time
import RPi.GPIO as GPIO
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                GPIO.output(22,GPIO.LOW)
                GPIO.output(27,GPIO.LOW)
                GPIO.output(17,GPIO.LOW)
                GPIO.output(4,GPIO.LOW)
                break
            elif char == ord('a'):
                print("Light On")
                GPIO.output(23,GPIO.HIGH)
                
            elif char == ord('z'):
                print("Light Off")
                GPIO.output(23,GPIO.LOW)
            elif char == curses.KEY_UP:
                print "up"
                GPIO.output(22,GPIO.HIGH)
                GPIO.output(27,GPIO.LOW)
                GPIO.output(17,GPIO.LOW)
                GPIO.output(4,GPIO.HIGH)
            elif char == curses.KEY_DOWN:
                print "down"
                GPIO.output(22,GPIO.LOW)
                GPIO.output(27,GPIO.HIGH)
                GPIO.output(17,GPIO.HIGH)
                GPIO.output(4,GPIO.LOW)
            elif char == curses.KEY_RIGHT:
                print "right"
                GPIO.output(22,GPIO.LOW)
                GPIO.output(27,GPIO.LOW)
                GPIO.output(17,GPIO.LOW)
                GPIO.output(4,GPIO.HIGH)
            elif char == curses.KEY_LEFT:
                print "left"
                GPIO.output(22,GPIO.HIGH)
                GPIO.output(27,GPIO.LOW)
                GPIO.output(17,GPIO.LOW)
                GPIO.output(4,GPIO.LOW)
            if char == ord('w'):
                    print "stop"
                    GPIO.output(22,GPIO.LOW)
                    GPIO.output(27,GPIO.LOW)
                    GPIO.output(17,GPIO.LOW)
                    GPIO.output(4,GPIO.LOW)
                
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

GPIO.cleanup()