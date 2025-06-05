# Static Methods : Methods that don't use the self parameter(works at class level)

class Student:
    @staticmethod               #decorator
    def college():
        print("falanaDhimkana")

# Decorators : allows us to wrap another function in order to extend the behaviour of the wrapped function,without permanently modifying it