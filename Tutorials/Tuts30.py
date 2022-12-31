 f = open("myfile.txt", "r")
print(f.readline() )
print(f.tell())


f = open("myfile.txt", "r")
f.seek(5)
print( f.readline() )


 f = open("harry.txt")
 f.seek(11)
 print(f.tell())
 print(f.readline())
 # print(f.tell())

 print(f.readline())
 # print(f.tell())
 f.close()

