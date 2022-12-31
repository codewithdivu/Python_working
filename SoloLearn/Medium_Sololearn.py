# HERE ALL OF SOLOLEARN'S MEDIUM CATEGORIES CODE COACH


#   Symbols

word = str(input())

print(word.translate({ord(i): None for i in '!@#$%^&*'}))

#   That's Odd

n = int(input())
sum = 0
for i in range(1, n + 1):
    ins = int(input())
    if ins % 2 == 0:
        sum = sum + ins

print(sum)

#   YouTube Link Finder

n = str(input())
length = len(n)
fund = length - 11
print(n[fund:])

# The Spy Life

word=str(input())
revers=word[::-1]
fuck=revers.split(" ")
duck=""

for i in revers:
    if i=="a":
        duck+="a"
    elif i=="b":
        duck+="b"
    elif i == " ":
        duck += " "
    elif i == "c":
        duck += "c"
    elif i == "d":
        duck += "d"
    elif i == "e":
        duck += "e"
    elif i == "f":
        duck += "f"
    elif i == "g":
        duck += "g"
    elif i == "h":
        duck += "h"
    elif i == "i":
        duck += "i"
    elif i == "j":
        duck += "j"
    elif i == "k":
        duck += "k"
    elif i == "l":
        duck += "l"
    elif i == "m":
        duck += "m"
    elif i == "n":
        duck += "n"
    elif i == "o":
        duck += "o"
    elif i == "p":
        duck += "p"
    elif i == "q":
        duck += "q"
    elif i == "r":
        duck += "r"
    elif i == "s":
        duck += "s"
    elif i == "t":
        duck += "t"
    elif i == "u":
        duck += "u"
    elif i == "v":
        duck += "v"
    elif i == "w":
        duck += "w"
    elif i == "x":
        duck += "x"
    elif i == "y":
        duck += "y"
    elif i == "z":
        duck += "z"
    elif i == "A":
        duck += "A"
    elif i == "B":
        duck += "B"
    elif i == "C":
        duck += "C"
    elif i == "D":
        duck += "D"
    elif i == "E":
        duck += "E"
    elif i == "F":
        duck += "F"
    elif i == "G":
        duck += "G"
    elif i == "H":
        duck += "H"
    elif i == "I":
        duck += "I"
    elif i == "J":
        duck += "J"
    elif i == "K":
        duck += "K"
    elif i == "L":
        duck += "L"
    elif i == "M":
        duck += "M"
    elif i == "N":
        duck += "N"
    elif i == "O":
        duck += "O"
    elif i == "P":
        duck += "P"
    elif i == "Q":
        duck += "Q"
    elif i == "R":
        duck += "R"
    elif i == "S":
        duck += "S"
    elif i == "T":
        duck += "T"
    elif i == "U":
        duck += "U"
    elif i == "V":
        duck += "V"
    elif i == "W":
        duck += "W"
    elif i == "X":
        duck += "X"
    elif i == "Y":
        duck += "Y"
    elif i == "Z":
        duck += "Z"

print(duck)


# Deja Vu

word=input()
count=1
for i in range(0,len(word)):
    for j in range(i+1,len(word)):
        if(word[i]==word[j] and word[i]!=''):
            count=count+1
if count>1:
    print('Deja Vu')
else:
    print('Unique')

# No Numerals

word=input()

dict={
    "10":"Ten",
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"seven",
    "8":"Eight",
    "9":"Nine",
}

for key,value in dict.items():
    word=word.replace(key,value)

print(word)