"""
Random password creater
"""
import time
import random
from tqdm import tqdm
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{},.-*&+-/?!;"

all = lower+upper+numbers+symbols
while True:
   print("1)Create a password\n2)Quit")
   choice = int(input("Choice :"))
   if choice == 2:
       time.sleep(1)
       break
   elif choice == 1:
        length = int(input("Password length :"))
        for i in tqdm(range(10)):
            time.sleep(.4)
        password = "".join(random.sample(all,length))
        print("***PASSWORD***")
        print(password)
        time.sleep(2)
