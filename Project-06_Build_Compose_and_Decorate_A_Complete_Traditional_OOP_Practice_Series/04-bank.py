# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name :str = "default Bank"

    def __init__(self , name):
        self.name = name

    @classmethod
    def change_bank_name(cls , name):
        cls.bank_name = name



bank = Bank("JS")
bank1 = Bank("HBL")

print("Before Change: ")
print(f"Bank name: {bank.name}, Bank Branch: {bank.bank_name}")
print(f"Bank1 name: {bank1.name} , Bank Branch: {bank1.bank_name}")

Bank.change_bank_name("National Bank")

print("After Change: ")
print(f"Bank name: {bank.name}, Bank Branch: {bank.bank_name}")
print(f"Bank1 name: {bank1.name}, Bank Branch: {bank1.bank_name}")


        