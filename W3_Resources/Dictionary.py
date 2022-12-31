def swap_case(s):
    for i in s:
        result=i.isupper()
        if result==True:
            print(i.lower(),end="")
        else :
            print(i.upper(),end="")

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)