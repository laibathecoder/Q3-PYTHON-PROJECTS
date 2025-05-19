# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id
        

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("laiba" , "001")
dept = Department(emp)

print(dept.employee.name)
print(dept.employee.id)