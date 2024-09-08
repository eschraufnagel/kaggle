print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

# Indexing
planet = 'Pluto'
print(planet[0])

# all caps
claim = 'Pluto is a planet!'
print(claim.upper())

# all lower
print(claim.lower())

print(claim.index('plan'))

# Slicing
print(planet[-3:])

# How long is this string?
print(len(planet))

print([char+'! ' for char in planet])

print(claim.startswith(planet))

print(claim.endswith('planet'))

words = claim.split()
print(words)

datestr = '1983-06-06'
year, month, day = datestr.split('-')
print(year, month, day)

print('/'.join([year, month, day]))

print(' 👏 '.join([word.upper() for word in words]))

print(planet + ', we miss you.')

position = 9
print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])

numbers['eleven'] = 11
print(numbers)

numbers['one'] = 'Pluto'
print(numbers)

for k in numbers:
    print('{} = {}'.format(k, numbers[k]))

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}

print('Neptune' in planet_to_initial)
print('Luna' in planet_to_initial)

print(' '.join(sorted(planet_to_initial.values())))
print(planet_to_initial)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

print(len(""))

def is_valid_zip(zip_code):
    return zip_code.isdigit() and len(zip_code) == 5
print(is_valid_zip('802132'))
print("\n")

def word_search(doc_list, keyword):
    doc_list_index = {k: v for k, v in enumerate(doc_list)}
    output = []
    for index, value in doc_list_index.items():
        for word in value.split():
            if keyword.lower() == word.lower().replace('.', '').replace(',',''):
                output.append(index)
    return list(set(output))

doc_list = ['The Learn Python Challenge Casino has a big casino full of casino games', 'They bought a car', 'Casinoville']
print(word_search(doc_list, 'casino'))
print("\n")

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
def multi_word_search(doc_list, keywords):
    doc_list_index = {k: v for k, v in enumerate(doc_list)}
    output = {keyword: [] for keyword in keywords}
    for index, value in doc_list_index.items():
        words = value.lower().replace('.', '').replace(',','').split()
        for word in words:
            if(word in keywords):
                output[word].append(index)
    return output
print(multi_word_search(doc_list, keywords))