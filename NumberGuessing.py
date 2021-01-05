import random
import time

randomNumber = random.randint(0,101)
live = 7
print("You have 7 attempts to find the number!")
while True:
    num = int(input("Enter a number between 0 and 100 : "))
    if num < randomNumber:
        print("Checking!")
        time.sleep(1)
        print("Enter a larger number")
        live -= 1
    elif num > randomNumber:
        print("Checking")
        time.sleep(1)
        print("Enter a smaller number")
        live -= 1
    else:
        print("Congratulations :) ")
        print("The number you found : {}".format(randomNumber))
        break        
    if live == 0:
        print("Game Over :( ")
        break