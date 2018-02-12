from digitalio import DigitalInOut, Direction, Pull
import board
import time

motor = DigitalInOut(board.D3)
motor.direction = Direction.OUTPUT

syringe1 = DigitalInOut(board.D4)
syringe1.direction = Direction.INPUT
syringe1.pull = Pull.DOWN

syringe2 = DigitalInOut(board.D2)
syringe2.direction = Direction.INPUT
syringe2.pull = Pull.DOWN

syringe3 = DigitalInOut(board.D1)
syringe3.direction = Direction.INPUT
syringe3.pull = Pull.DOWN

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
while True:
    
    #print ("Syringe 1: " + str(syringe1.value) + " Syringe 2: " + str(syringe2.value) + " Syringe 3: " + str(syringe3.value))
    motor.value = True
    time.sleep(0.1)
    
    if syringe2.value == True:
        print("syringe 1")
        
        if syringe1.value == True:
            print("syringe 2")
            if syringe3.value == True:
                motor.value = False
                while True:
                    if syringe1.value == False:
                        if syringe2.value == False:
                            if syringe3.value == False:
                                print("continue")
                                break
    
print("broke")