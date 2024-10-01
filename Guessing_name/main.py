
import random

def get_valid_number():
    while True:
        bottom_of_range = input("Enter a number where the range will start: ")
        top_of_range = input("Enter a number where the range will end: ")
        try:
            bottom_of_range = int(bottom_of_range)
            top_of_range = int(top_of_range)
            if bottom_of_range < top_of_range:
                if top_of_range - bottom_of_range == 2:
                    print("difference should be greater than two")
                else:
                    return bottom_of_range, top_of_range
            else:
                print("The bottom should be lesser than the top of range")
        except ValueError:
          print("Please input a valid number")


def main():
    while True:
      bottom_of_range, top_of_range = get_valid_number()
      random_number = random.randint(bottom_of_range, top_of_range)
      # I've completely forgotten that I created a block of code with this structure. I'm pretty amazed right now
      guesses = 0

      while True:
        user_input = int(input("Enter a number within the range you set: "))
        guesses += 1
        if user_input == random_number:
            print("You're correct")
            break
        elif user_input > random_number:
             print("You're close. Type a lesser number")
        elif user_input < random_number:
             print("You're close. Type a greater number")

      print(f"Congratulations you got it in " + str(guesses) + " guesses")

main()
print("I hope this works now")
print("Doing another edit to be committed")
