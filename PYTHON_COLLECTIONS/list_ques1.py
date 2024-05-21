# swap of two elements of a list 

# list1 = [23, 65, 19, 90]
# print(list1)

# temp[x] = list1[0]
# print(x)
# list1[2] = list1[0]
# print(list1)
# list1[0] = list1[2]
# print(list1)


n = int(input("Enter size of list: "))

list1 = []
for _ in range(n):
    num = int(input())
    list1.append(num)

idx1 = int(input("Enter index1: "))
idx2 = int(input("Enter index2: "))
print(list1)
temp = list1[idx1]
list1[idx1] = list1[idx2]
list1[idx2] = temp
print(list1)

