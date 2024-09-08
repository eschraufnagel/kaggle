# x = True
# print(x)
# print(type(x))

# def can_run_for_president(age, is_natural_born_citizen):
#     return is_natural_born_citizen and age >= 35

# # print("Can a 19-year-old run for president?", can_run_for_president(19))
# # print("Can a 45-year-old run for president?", can_run_for_president(45))

# print(3.0 == 3)

# print('3' == 3)

# def is_odd(n):
#     return(n % 2) == 1

# print("Is 100 odd?", is_odd(100))
# print("Is -1 odd?", is_odd(-1))

# print(can_run_for_president(19, True))
# print(can_run_for_president(55, False))
# print(can_run_for_president(55, True))

# print(True or True and False)

# def inspect(x):
#     if x == 0:
#         print(x, "is zero")
#     elif x > 0:
#         print(x, "is positive")
#     elif x < 0:
#         print(x, "is negative")
#     else:
#         print(x, "is unlike anything I've ever seen...")

# inspect(0)
# inspect(-15)

# def f(x):
#     if x > 0:
#         print("Only printed when x is positive; x =", x)
#         print("Also only printed when x is positive; x =", x)
#     print("Always printed, regardless of x's value; x =", x)

# f(1)
# f(0)

# print(bool(1)) # all numbers are treated as true, except 0
# print(bool(0))
# print(bool("asf")) # all strings are treated as true, except the empty string ""
# print(bool(""))
# # Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# # are "falsey" and the rest are "truthy"

# if 0:
#     print(0)
# elif "spam":
#     print("spam")

# def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
#     # Don't change this code. Our goal is just to find the bug, not fix it!
#     return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# # Change the values of these inputs so they represent a case where prepared_for_weather
# # returns the wrong answer.
# have_umbrella = False
# rain_level = 0.0
# have_hood = False
# is_workday = False

# # Check what the function returns given the current values of the variables above
# actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
# print(actual)

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

print(wants_plain_hotdog(False, False, False))