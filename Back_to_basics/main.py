
def enter_name():
    while True:
        user_input = input("Enter your name: ").strip()  # Remove leading and trailing whitespace
        if not user_input:  # Check if the input is empty
            print("Enter a valid name.")
        elif any(char.isdigit() for char in user_input):  # Check if there are any digits in the input
            print("Enter a valid name (letters and spaces only).")
        else:
            break

    if user_input:
        user_input = user_input.title()
        return user_input


def enter_age():
    while True:
        user_input = int(input("Enter your age: "))
        if  0 < user_input < 18:
            print("You can't play the game")
        elif user_input < 0:
            print("You can't have such age")
        elif user_input == 0:
            print("You cant have a zero age")
        else:
            break

    return user_input

def intro():
    name = enter_name()
    age_unconverted = enter_age()
    new_age = str(age_unconverted)

    print(f"Name: {name}", f"Age: {new_age}", sep=" | ")

intro()