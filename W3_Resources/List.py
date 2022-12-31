# a = [1,2,3,4,5,5,6,6,7,8]
# print(sum(a))

# a = [1,2,-8]
# mul=1
# for i in a:
#     mul=mul*i
# print(mul)

# a = [1,2,3,4,5,5,6,6,0,7,8]
# print(max(a))
# print(min(a))

# def count(word):
#     ct=0
#     for i in word:
#         if len(i) > 1 and i[0]==i[-1]:
#             ct+=1
#     return ct
#
# print(count(['abc', 'xyz', 'aba', '1221']))

# def last(n):
#     return n[-1]
# def sort_list_last(s):
#     return sorted(s,key=last)
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# l=["hello"]
# if len(l)==0:
#     print("empty")

# old = [1,2,3,4,5,6,7,8,9,10,11]
# new = list(old)
# print(old)
# print(new)


# def check(n,str):
#     new=[]
#     txt=str.split()
#     for i in txt:
#         if len(i)>n:
#             new.append(i)
#     return new
# print(check(4, "The quick brown fox jumps over the lazy dog"))


# def common(a,b):
#     result = False
#     for i in a:
#         for j in b:
#             if i==j:
#                 result = True
#                 return result
#
# print(common([1,2,3,4,5],[5,6,7,8,9]))


# def rem(a):
#     a.pop(0,4)
#     a.pop(4)    #skipping this exercises
#     a.pop(5)
#     return a
# print(rem(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))


# array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)

# num = [7,8, 120, 25, 44, 20, 27]
# num = [x for x in num if x%2!=0]
# print(num)

# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)


# def List_Square():
#     a=[]
#     for i in range(1,30):
#         a.append(i**2)
#     print(a[:5])
#     print(a[-5:])
# List_Square()


# def List_Square():
#     a=[]
#     for i in range(1,31):
#         a.append(i**2)
#     print(a[5:])
# List_Square()


# import itertools
# print(list(itertools.permutations([1,2,3])))

# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
# first = list(set(list1)-set(list2))
# second = list(set(list2)-set(list1))
# total=first+second
# print(total)


# s = ['a', 'b', 'c', 'd']
# str = "".join(s)
# print(str)


# num =[10, 30, 4, -6]
# print(num.index(-6))

# import itertools
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new_list = list(itertools.chain(*original_list))
# print(new_list)


# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# total = list1+list2
# print(total)

# import random
# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(random.choice(color_list))


# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
#
# print('Compare list1 and list2')
# print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# print('Compare list1 and list3')
# print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


# def second_smallest(num):
#     if len(num)<2:
#         return
#     if len(num)==2 and num[0]==num[1]:
#         return
#     dep = set()
#     new = []
#     for x in num:
#         if x not in dep:
#             new.append(x)
#             dep.add(x)
#     new.sort()
#     return new[1]
#
#
# print(second_smallest([1, 2, -8, -2, 0, -2]))
# print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_smallest([2,2]))
# print(second_smallest([2]))


# def second_largest(numbers):
#   if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()
#   return  uniq_items[-2]
# print(second_largest([1,2,3,4,4]))
# print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_largest([2,2]))
# print(second_largest([1]))


# my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# print("Original List : ",my_list)
# my_set = set(my_list)
# my_new_list = list(my_set)
# print("List of unique numbers : ",my_new_list)

# import collections
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List : ",my_list)
# ctr = collections.Counter(my_list)
# print(ctr)










