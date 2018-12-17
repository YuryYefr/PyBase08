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


def user_numbers():
    a = input("Number?: ")
    while a.isspace() or a.isalpha() or a == "":
        print("there is something wrong with your input, please try again")
        a = input("Number?: ")
    b = input("What is second number?: ")
    while b.isspace() or b.isalpha() or b == "":
        print("there is something wrong with your input, please try again")
        b = input("What is second number?: ")
    user_number = float(a), float(b)
    return user_number


def user_oper():
    user_operations = input("you choose what?:")
    while user_operations.isspace() or user_operations.isalpha():
        print("there is something wrong with your input, please try again")
        user_operations = input("you choose what?: ")
    return user_operations


def logic():
    result = 0
    a, b = user_numbers()
    print("\n1.if you want to add"
          "\n2.if you want to minus"
          "\n3. if you want to divide"
          "\n4. if you want to multiply"
          )
    choice = user_oper()
    user_numbersDict = {"1": add,
                        "2": minus,
                        "3": division,
                        "4": multiply,
                        }
    if choice in user_numbersDict:
        return user_numbersDict[choice](a, b)
    return result


def erase(res):
    res = 0
    return res


if __name__ == "__main__":
    userName = " "
    print("You must be logged on to use the application\nWould you like to register?")
    user_entry = input("Y/N:")
    while user_entry.lower() != "y" and user_entry.lower() != "n":
        print("You must be logged on to use the application\nWould you like to register?")
        user_entry = input("Y/N:")
    if user_entry.lower() == "n" or user_entry.isspace():
        print("program is shutting down")
        exit()
    elif user_entry.lower() == "y":
        userName = input("what is your name?:")
        while userName.isdigit() or userName.isspace() or userName == "":
            print("strange name, repeat please")
            userName = input("what is your name?:")
    else:
        print("check your input")
        exit()
    print(f"Welcome {userName.capitalize()}\tlet's do some calculate")
    result = logic()
    print(result)
    print("do you want to erase your result?")
    user_input1 = input("Y/N").lower()
    if user_input1 == "y":
        result = erase(result)
    print("do you want to continue your calculations? ")
    user_input = input("Y/N: ").lower()
    while user_input == "y":
        result += logic()
        print(result)
        print("do you want to continue your calculations? ")
        user_input = input("Y/N: ").lower()
    if user_input == "n":
        print("shutting down the program")
        exit()
    else:
        print("something wrong")
