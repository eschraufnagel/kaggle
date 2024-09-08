spam_amount = 0
print(spam_amount)

spam_amount = spam_amount + 4

if spam_amount  > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song) 

print(type(spam_amount))
print(type(19.95))

print(5 / 2)
print(6 / 2)

print(5 // 2)
print(6 // 2)

print(8 - 3 + 2)
print(-3 + 4 * 2)

hat_height_cm = 25
my_height_cm = 190
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
print(int('887') + 1)

color = "blue"

pi = 3.14159
diameter = 3
radius = diameter / 2
area = pi * (radius ** 2)

a = [1, 2, 3]
b = [3, 2, 1]
a, b = b, a

alice_candies = 121
bob_candies = 77
carol_candies = 109
to_smash = (alice_candies + bob_candies + carol_candies) % 3
print(to_smash)