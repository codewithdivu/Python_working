print("please enter number")
num = int(input())

def factorial(num):
    if(num==0 or num==1):
        return num
    return num*factorial(num-1)

print('factorial is ',factorial(num))