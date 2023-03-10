# David Rapaport
# 🌟 Exercise 2: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
#
#     #Your code starts HERE
#
# #
# # Using the code above, implement the relevant methods and dunder methods which will output the results below.
# # Hint : When adding 2 currencies which don’t share the same label you should raise an error.
>>> c1 = Currency('dollar', 5)
>>> c2 = Currency('dollar', 10)
>>> c3 = Currency('shekel', 1)
>>> c4 = Currency('shekel', 10)

>>> str(c1)
'5 dollar'

>>> int(c1)
5

>>> repr(c1)
'5 dollar'

>>> c1 + 5
10

>>> c1 + c2
15

>>> c1
'5 dollar'

>>> c1 += 5
>>> c1
'10 dollar'

>>> c1 += c2
>>> c1
'20 dollar'

>>> c1 + c3
TypeError: Cannot add between Currency type <dollar> and <shekel>'#
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
#
#     def __str__(self):
#         return f"{self.amount} {self.currency}"
#
#     def __int__(self):
#         return self.amount
#
#     def __repr__(self):
#         return f"{self.amount} {self.currency}"
#
#     def __add__(self, other):
#         if isinstance(other, Currency) and self.currency != other.currency:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         elif isinstance(other, Currency):
#             return Currency(self.currency, self.amount + other.amount)
#         else:
#             return Currency(self.currency, self.amount + other)
#
#     def __iadd__(self, other):
#         if isinstance(other, Currency) and self.currency != other.currency:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         elif isinstance(other, Currency):
#             self.amount += other.amount
#         else:
#             self.amount += other
#         return self
