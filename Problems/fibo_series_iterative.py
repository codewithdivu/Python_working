print('enter a number')
num = int(input())

def fibo(num):
    t1 = 0
    t2 = 1
    for i in range(num):
        print(t1," ")
        nextTerm = t1 + t2
        t1 = t2
        t2 = nextTerm


fibo(num)
        