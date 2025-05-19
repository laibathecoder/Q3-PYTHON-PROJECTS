# 7. **Access Modifiers: Public, Private, and Protected**
# **Assignment:**  
# Create a class Employee with:

# -   a public variable name,
# -   a protected variable _salary, and
# -   a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name , _salary , __ssn):
        self.name = name
        self._salary = _salary
        self.__ssn = __ssn

    
emp = Employee("Jhon" , "20,000$" , "123-45-6789")    
print(emp.name)  
print(emp._salary)
print(emp._Employee__ssn)