# Program to generate random numbers the input wil be the number of digit

# we will use random module to generate number
from random import randint

# this function will generate random number
def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


if __name__ == '__main__':
    print("Enter a number how many digits of number you need!!")
    num = int(input())
    print(random_with_N_digits(num))
