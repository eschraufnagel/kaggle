planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet)
print('\n')

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)
print('\n')

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
for char in s:
    if char.isupper():
        print(char, end='')
print('\n')

for i in range(5):
    print("Doing important work. i =", i)
print("\n")

i = 0
while i < 10:
    print(i, end=' ')
    i += 1
print("\n")

# list comprehensions
squares = [n**2 for n in range(10)]
print(squares)
print("\n")

# SELECT, FROM, WHERE
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)
print("\n")

loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)
print("\n")

print([32 for planet in planets])
print("\n")

def count_negatives1(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negatives2(nums):
    return len([num for num in nums if num < 0])

def count_negatives3(nums):
    return sum([num < 0 for num in nums])

def has_lucky_number1(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False

def has_lucky_number2(nums):
    return any([num % 7 == 0 for num in nums])

def elementwise_greater_than(L, thresh):
    return [i > thresh for i in L]

def menu_is_boring(meals):
    for index, meal in enumerate(meals):
        if(index != 0 and meal == meals[index-1]):
            return True
    return False
    
def menu_is_boring2(meals):
    return any([meal for index, meal in enumerate(meals) if index != 0 and meal == meals[index-1]])
