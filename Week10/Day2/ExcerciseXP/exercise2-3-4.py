# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

# import random
#
# def roll_dice(user_input):
#     if user_input < 1 or user_input > 100:
#         print("Number must be between 1 and 100")
#         return
#
#     random_number = random.randint(1, 100)
#     print("The random number is:", random_number)
#
#     if user_input == random_number:
#         print("Congratulations! You guessed the number!")
#     else:
#         print("Sorry, better luck next time.")
#
# roll_dice(50)
# roll_dice(75)
# roll_dice(150)


    # 🌟 Exercise 3: String Module
    # Instructions
    # Generate random String of length 5
    # Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
#     # Hint: use the string module
#
# import string
# import random
#
# def generate_random_string(length):
#    # characters to choose from
#     chars = string.ascii_letters
#
#     # Generate a random string of the specified length
#     random_string = ''.join(random.choice(chars) for i in range(length))
#
#     return random_string
#
# random_string = generate_random_string(5)
# print(random_string)


# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime

def current_date():
    today = datetime.date.today()
    print("Today's date:", today)

current_date()