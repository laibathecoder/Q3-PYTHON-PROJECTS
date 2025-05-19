#  20. **Creating a Custom Exception**
# **Assignment:**  
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass


def age_check(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("You are eligible!")


try:
    user_age = int(input("Enter your age: "))
    age_check(user_age)
except InvalidAgeError as e:
    print(f"Custom Exception Caught: {e}")
except ValueError:
    print("Please enter a valid number.")
