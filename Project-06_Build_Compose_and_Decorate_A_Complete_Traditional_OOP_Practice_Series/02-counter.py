# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    @classmethod
    def show_count(cls):
        print("Count: " , cls.count)


    def __init__(self):
        Counter.count += 1
        print("Object created. Total now:" , Counter.count)

    
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.show_count()

 