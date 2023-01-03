print('enter a number')
num = int(input())

def fibo(num):
    if num==0 or num==1:
        return num
    return fibo(num-1)+fibo(num-2)

print("nth fibo term is ",fibo(num))