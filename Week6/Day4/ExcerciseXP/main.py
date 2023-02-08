# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# # Create a set called friend_fav_numbers with your friend’s favorites numbers.
# # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
#
# my_fav_numbers = {7, 3, 5, 8}
# my_fav_numbers.add(99)
# my_fav_numbers.add(11)
# print(my_fav_numbers)
# my_fav_numbers = set(list(my_fav_numbers)[:-1])
# print(my_fav_numbers)
#
# friend_fav_numbers = {11, 22, 33, 21}
#
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#
# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
#
# No, you can't because tuples are immutable

# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
#
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# del basket[-1]
# print(basket)
# basket.append("kiwi")
# basket.insert(0, "Apples")
# count_apples = basket.count("Apples")
# basket.clear()
# print(basket)

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float? a float is a number with a decimals, an integer is a number alone
# Can you think of another way to generate a sequence of floats? with a range
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# sequence = []
# for i in range(1, 6):
#     sequence.append(i + 0.5)
#     sequence.append(i)
#
# print(sequence)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
#
# for i in range(1, 21):
#     print(i)
#
#  for i in range(1, 21):
#    if i % 2 == 0:
#      print(i)
#
# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# name = "David"
# while True:
#     user_name = input("What's your name my friend?")
#     if user_name == name:
#         break
#
# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
#
# favorite_f = input("Enter your favorite fruits separated by a space: ").split()
#
# while True:
#     chosen_fruit = input("Enter a fruit: ")
#     if chosen_fruit in favorite_f:
#         print("You chose one of your favorite fruits! Enjoy!")
#     else:
#         print("You chose a new fruit. I hope you enjoy")