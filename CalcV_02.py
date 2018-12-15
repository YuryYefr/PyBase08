import math


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide on zero")


def multiply(a, b):
    return a * b


def sqrt(a):
    return math.sqrt(a)


def logic():
    result = 0
    print("\n1.if you want to add"
          "\n2.if you want to minus"
          "\n3. if you want to divide"
          "\n4. if you want to multiply")
    user_operations = input("you choose what?:")
    while user_operations.isspace() or user_operations.isalpha():
        print("there is something wrong with your input, please try again")
        user_operations = input("you choose what?: ")
    if user_operations == "1":
        result += add(user_choice1, user_choice2)
        return add(user_choice1, user_choice2)
    elif user_operations == "2":
        result += minus(user_choice1, user_choice2)
        return minus(user_choice1, user_choice2)
    elif user_operations == "4":
        result += multiply(user_choice1, user_choice2)
        return multiply(user_choice1, user_choice2)
    elif user_operations == "3":
        result += division(user_choice1, user_choice2)
        return division(user_choice1, user_choice2)
    else:
        print("something wrong with your choice")


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
    a = input("Number?: ")
    while a.isspace() or a.isalpha():
        print("there is something wrong with your input, please try again")
        a = input("Number?: ")
    user_choice1 = float(a)
    b = input("What is second number?: ")
    while a.isspace() or a.isalpha():
        print("there is something wrong with your input, please try again")
        b = input("What is second number?: ")
    user_choice2 = float(b)


    def log_result(res):
        print(res)

print(logic())
