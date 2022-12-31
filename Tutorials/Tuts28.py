# f = open("harry.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
# f = open("harry2.txt", "r+")
# print(f.read())
# f.write("thank you")



a=[]
for i in range(1,3):
    item=int(input())
    a.append(item)

k=a[0]
m=a[1]

for i in range(1,k+1):
    l=int(input())
    # for j in range(1,l+1):
    a=list(map(int,input().strip().split()))[:l]
print(a)




