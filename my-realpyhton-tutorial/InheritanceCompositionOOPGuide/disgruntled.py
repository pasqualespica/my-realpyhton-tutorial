

# In Python, you don’t have to explicitly declare an interface. 
# Any object that implements the desired interface can be used in place of another object.
#  This is known as duck typing. 
# Duck typing is usually explained as “if it behaves like a duck, then it’s a duck.”

# https://realpython.com/python-type-checking/#duck-typing


class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000
