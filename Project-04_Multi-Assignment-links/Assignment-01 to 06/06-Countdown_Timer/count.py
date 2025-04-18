# Countdown Timer by Python
  

import time

seconds = int(input("Kitne seconds ka countdown chahiye? "))

while seconds:
    print(f"{seconds} seconds remaining", end='\r')
    time.sleep(1)
    seconds -= 1

print("⏰ Time's up!")
