#Exercise 1 : Hello World
#Instructions
#Print the following output in one line of code:
#
# Hello world
# # Hello world
# # Hello world
# # Hello world
#
# print("Hello world\nHello world\nHello world\nHello world")

# 🌟 Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# # Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
#
# computer_brand = "HP"
# print("I have a " + computer_brand + " computer")

# 🌟 Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# # Have your code print the info message.
# # Run your code
# name = 'David'
# age = '38'
# shoe_size = '41'
# info = f'my name is {name}, Im {age} and my shoe size is {shoe_size}'
# print((info))

# 🌟 Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.
#
# a = 201
# b = 200
# if a > b:
#     print("Hello World")

# 🌟 Exercise 8 : What’s Your Name ?
# # Instructions
# # Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
#
# ask = input('Whats your name?')
#
# if ask == 'david':
#     print("The best name")
# elif ask == 'john':
#     print("what kind of name is that??")
# elif ask == 'peter':
#     print("Really you name is peter?")


# 🌟 Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

ask_height = int(input('Whats your height in inches?'))

if ask_height >= 145:
    print("tall enough to ride")
elif ask_height <= 144:
    print("need to grow some more to ride")
