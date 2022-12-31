# HERE ALL OF SOLOLEARN'S EASY CATEGORIES CODE COACH


#   Popsicles

siblings = int(input())
popsicles = int(input())

s = "give away"
t = "eat them yourself"
if popsicles % siblings == 0:
    print(s)
else:
    print(t)

#   Fruit Bowl

fruits = int(input())
apple = int(fruits / 2)
pie = int(apple / 3)
print(pie)

#   Cheer Creator

yard = int(input())

if yard > 10:
    print("High Five")
elif yard < 1:
    print("shh")
elif yard >= 1 and yard <= 10:
    for i in range(0, yard):
        print("Ra!")

#   Argentina

peso = int(input())
dolla = int(input())
peso = peso * 2
dolla = dolla * 100

if dolla > peso:
    print("Pesos")
elif peso > dolla:
    print("Dollars")

#   Gotham City

criminals = int(input())
if criminals < 5:
    print("I got this!")
elif criminals < 11:
    print("Help me Batman")
else:
    print("Good Luck out there!")

#   Extra-Terrestrials

n1 = input()
print(n1[::-1])

#   Halloween Candy

import math

houses = int(input())
print(math.ceil((100 / houses) * 2))

#   Paint costs

import math

canvas = 40
n_paint = int(input())
paint = n_paint * 5
lund = paint + canvas
intrest = math.ceil(lund / 10)
money = intrest + lund
print(money)

#   Skee-Ball


import math
score=int(input())
ticket=int(input())

lund=math.ceil(score/12)

if lund<ticket:
    print("Try again")
elif lund>=ticket:
    print("Buy it!")

#   Jungle Camping


what_animal = input().split(" ")
animals = ""

for noise in what_animal:
    if noise == "Grr":
        animals += "Lion "
    if noise == "Rawr":
        animals += "Tiger "
    if noise == "Ssss":
        animals += "Snake "
    if noise == "Chirp":
        animals += "Bird "

print(animals)

#   Hovercraft

cost=21000000
price=3000000
sales =int(input())

if sales*price>cost:
    print("Profit")
elif sales*price==cost:
    print("Broke Even")
else:
    print("Loss")
