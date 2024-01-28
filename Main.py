import random
import time
from pynput.keyboard import Key, Controller
 
numList = [1,2,3,4,5,6,7,8,9,10,11,12]
list2 = [5,6,7,8]
keyboard = Controller()

print("Press Enter to begin,")
input()

while True:
    numChoice = random.choice(numList)
    numC2 = random.choice(list2)
    if numChoice == 1:
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        keyboard.press('t')
        time.sleep(0.5)
        keyboard.release('t')
    if numChoice == 2:
        keyboard.press('s')
        time.sleep(0.16)
        keyboard.release('s')
        
    if numChoice == 3:
        keyboard.press('d')
        time.sleep(0.16)
        keyboard.release('d')
    
    if numChoice == 4:
        keyboard.press('f')
        time.sleep(0.16)
        keyboard.release('f')
        
    if numChoice == 5:
        keyboard.press('t')
        time.sleep(0.5)
        keyboard.release('t')
        
    if numChoice == 6:
        keyboard.press('y')
        time.sleep(0.5)
        keyboard.release('y')
        
    if numChoice == 7:
        keyboard.press('u')
        time.sleep(0.5)
        keyboard.release('u')
    
    if numChoice == 8:
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        keyboard.press('i')
        time.sleep(0.5)
        keyboard.release('t')
        #keyboard.press('i')
        #time.sleep(0.5)
        #keyboard.release('i')
        
    if numChoice == 9:
        keyboard.press('o')
        time.sleep(0.16)
        keyboard.release('o')
        
    if numChoice == 10:
        keyboard.press('z')
        time.sleep(0.16)
        keyboard.release('z')
    if numChoice == 11:
        keyboard.press('l')
        time.sleep(0.16)
        keyboard.release('l')
    if numChoice == 12:
        keyboard.press('r')
        time.sleep(0.16)
        keyboard.release('r')