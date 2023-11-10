print('please enter a number')
num = int(input())

def prime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    
    return True

if(prime(num)):
    print('number is PRIME')
else:
    print('number is NOT PRIME')