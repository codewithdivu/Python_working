# HERE ALL OF SOLOLEARN'S HARD CATEGORIES CODE COACH


#   Password Validation

word = str(input())
length = len(word)
count = 0
lund = 0
for i in word:
    if (
            i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0"):
        count += 1
    if (i == "!" or i == "@" or i == "#" or i == "$" or i == "%" or i == "&" or i == "*"):
        lund += 1

if (count >= 2 and lund >= 2 and length >= 7):
    print("Strong")
elif (count < 2 or lund < 2 or length < 7):
    print("Weak")
