# Countdown Timer by Python

# import time

# minutes = int(input("Kitne minutes ka countdown chahiye? "))
# seconds = minutes * 60

# while seconds:
#     mins = seconds // 60
#     secs = seconds % 60
#     timer = f'{mins:02d}:{secs:02d}'
#     print(timer, end='\r')
#     time.sleep(1)
#     seconds -= 1

# print("⏰ Time's up!")
  

import time

seconds = int(input("Kitne seconds ka countdown chahiye? "))

while seconds:
    print(f"{seconds} seconds remaining", end='\r')
    time.sleep(1)
    seconds -= 1

print("⏰ Time's up!")
