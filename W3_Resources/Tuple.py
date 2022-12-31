# Tuple

# #Create an empty tuple
# x = ()
# print(x)
# #Create an empty tuple with tuple() function built-in Python
# tuplex = tuple()
# print(tuplex)


# #Create a tuple with different data types
# tuplex = ("tuple", False, 3.2, 1)
# print(tuplex)


# #Create a tuple with numbers
# tuplex = 5, 10, 15, 20, 25
# print(tuplex)
# #Create a tuple of one item
# tuplex = 5,
# print(tuplex)


# #create a tuple
# tuplex = 4, 8, 3
# print(tuplex)
# n1, n2, n3 = tuplex
# #unpack a tuple in variables
# print(n1 + n2 + n3)
# #the number of variables must be equal to the number of items of the tuple
# n1, n2, n3, n4= tuplex


#create a tuple
# tuplex = (4, 6, 2, 8, 3, 1)
# print(tuplex)
# #tuples are immutable, so you can not add new elements
# #using merge of tuples with the + operator you can add an element and it will create a new tuple
# tuplex = tuplex + (9,)
# print(tuplex)
# #adding items in a specific index
# tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
# print(tuplex)
# #converting the tuple to list
# listx = list(tuplex)
# #use different ways to add items in list
# listx.append(30)
# tuplex = tuple(listx)
# print(tuplex)


# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# str = "".join(tup)
# print(str)


#Get an item of the tuple
# tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print(tuplex)
# #Get item (4th element)of the tuple by index
# item = tuplex[3]
# print(item)
# #Get item (4th element from last)by index negative
# item1 = tuplex[-4]
# print(item1)


# from copy import deepcopy
# #create a tuple
# tuplex = ("HELLO", 5, [], True)
# print(tuplex)
# #make a copy of a tuple using deepcopy() function
# tuplex_colon = deepcopy(tuplex)
# tuplex_colon[2].append(50)
# print(tuplex_colon)
# print(tuplex)


# create a tuple
# tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
# print(tuplex)
# return the number of times it appears in the tuple.
# count = tuplex.count(4)
# print(count)


# tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print("r" in tuplex)
# print(5 in tuplex)


#Convert list to tuple
# listx = [5, 10, 7, 4, 15, 3]
# print(listx)
#use the tuple() function built-in Python, passing as parameter the list
# tuplex = tuple(listx)
# print(tuplex)


# #create a tuple
# tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
# print(tuplex)
# tuples are immutable, so you can not remove elements
# #using merge of tuples with the + operator you can remove an item and it will create a new tuple
# tuplex = tuplex[:2] + tuplex[3:]
# print(tuplex)
# converting the tuple to list
# listx = list(tuplex)
# use different ways to remove an item of the list
# listx.remove("c")
# converting the tuple to list
# tuplex = tuple(listx)
# print(tuplex)


# #create a tuple
# tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# #used tuple[start:stop] the start index is inclusive and the stop index
# _slice = tuplex[3:5]
# #is exclusive
# print(_slice)
# #if the start index isn't defined, is taken from the beg inning of the tuple
# _slice = tuplex[:6]
# print(_slice)
# #if the end index isn't defined, is taken until the end of the tuple
# _slice = tuplex[5:]
# print(_slice)
# #if neither is defined, returns the full tuple
# _slice = tuplex[:]
# print(_slice)
# #The indexes can be defined with negative values
# _slice = tuplex[-8:-4]
# print(_slice)
# #create another tuple
# tuplex = tuple("HELLO WORLD")
# print(tuplex)
# #step specify an increment between the elements to cut of the tuple
# #tuple[start:stop:step]
# _slice = tuplex[2:9:2]
# print(_slice)
# #returns a tuple with a jump every 3 items
# _slice = tuplex[::4]
# print(_slice)
# #when step is negative the jump is made back
# _slice = tuplex[9:2:-4]
# print(_slice)


#create a tuple
# tuplex = tuple("index tuple")
# print(tuplex)
# #get index of the first item whose value is passed as parameter
# index = tuplex.index("p")
# print(index)
# #define the index from which you want to search
# index = tuplex.index("p", 5)
# print(index)
# #define the segment of the tuple to be searched
# index = tuplex.index("e", 3, 6)
# print(index)
# #if item not exists in the tuple return ValueError Exception
# index = tuplex.index("y")


#create a tuple
# tuplex = tuple("w3resource")
# print(tuplex)
# #use the len() function to known the length of tuple
# print(len(tuplex))


# create a tuple
# tuplex = ((2, "w"),(3, "r"))
# print(dict((y,x) for x, y in tuplex))


#create a tuple
# l = [(1,2), (3,4), (8,9),(6,7)]
# print(list(zip(*l)))


#create a tuple
# x = ("w3resource")
# # Reversed the tuple
# y = reversed(x)
# print(tuple(y))
# #create another tuple
# x = (5, 10, 15, 20)
# # Reversed the tuple
# y = reversed(x)
# print(tuple(y))


#create a list
# l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# d = {}
# for a, b in l:
#     d.setdefault(a, []).append(b)
# print (d)


