from digitalio import DigitalInOut, Direction, Pull
import board
import time

motor = DigitalInOut(board.D3)
motor.direction = Direction.OUTPUT

while True:
  motor.value = True
  time.sleep(1)
  motor.value = False
  time.sleep(1)
