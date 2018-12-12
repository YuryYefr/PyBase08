import math


class Calculator:
    def __init__(self, a, b):
        self.add(a, b)
        self.minus(a, b)
        self.division(a, b)
        self.multiply(a, b)
        self.sqrt(a)

    result_num = []

    def add(self, a, b):
        print(sum(a, b))

    def minus(self, a, b):
        print(a - b)
        print("unknown operation")

    def division(self, a, b):
        try:
            print(a / b)
        except ZeroDivisionError:
            print("You cannot divide on zero")

    def multiply(self, a, b):
        print(a * b)

    def sqrt(self, a):
        print(math.sqrt(a))

    def logic(self, a, user_operations, b):

        user_choice = f"{a} {b}"

        a = float(input("Number?: "))
        user_choice = a
        b = float(input("What is second number?: "))
        user_choice = b
        print("\n1.if you want to add"
              "\n2.if you want to minus"
              "\n3. if you want to divide"
              "\n4. if you want to multiply")
        user_operations = input("you choose what?:")
        while user_operations.isspace() or user_operations.isalpha():
            print("there is something wrong with your input, please try again")
            user_operations = input("you choose what?: ")
            if user_operations == "1":
                res = user_choice.add

    if __name__ == "__main__":
        userName = " "
        print("You must be logged on to use the application\nWould you like to register?")
        user_entry = input("Y/N:")
        if user_entry.lower() == "n" or user_entry.isspace():
            print("program is shutting down")
            exit()
        elif user_entry.lower() == "y":
            userName = input("what is your name?:")
        print(f"Welcome {userName.capitalize()}\tlet's do some calculate")


zaga = Calculator()
