# 🌟 Exercise 1: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:
#
# import module_name
#
# OR
#
# from module_name import function_name
#
# OR
#
# from module_name import function_name as fn
#
# OR
#
# import module_name as mn

# Importing the module and calling the function
import func

func.add_numbers(2, 3)


from func import add_numbers

add_numbers(5, 7)


from func import add_numbers as add

add(10, 20)


import func as f

f.add_numbers(3, 4)
