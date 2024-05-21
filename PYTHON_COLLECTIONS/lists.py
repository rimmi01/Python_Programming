fruits = ["apples", "mango", "cherry", "banana"]

# list = [1, 2, 3, 4]
# list1 = [1, 2.4, False, "john"]

print(fruits)
print(type(fruits))
print(len(fruits))

# checking if an item is present in the list 
if "banana" in fruits:
    print("Banana is part of the list")
if "kiwi" not in fruits:
    print("Kiwi is not part of the list")

# list = [10, 20, 30, 40]
# -4, -3, -2, -1  -ve indexing starts from the end of the list and starts with -1
# list[2]
# list[-2]

print(fruits[1])
print(fruits[-3])
print(fruits[1:3])
print(fruits[-3:-1]) # -3 represents the last 3rd item of the list and included, -1 represents last item of the list and not included 

list = [10, 20, 30, 40]
list.append(50)
print(list)

list.insert(2, 60)
print(list)


list2 = [100, 200]
list.extend(list2)
print(list)

# remove function
list.remove(20)
print(list)

# changing items in a list  # overriding a value 
list[1]=40
print(list)

list[1:3]= ["papaya"]
print(list)

# sorting a list 

print(fruits)
fruits.sort()
print(fruits)

fruits.sort(reverse=True) # list will be printed in reverse order 
print(fruits)

fruits.reverse()
print(fruits)

# list comprehension 
some_list = [40, 20, 30, 10]   # a tip:- don't use list as a list name, as, it is a builtin keyword in python, so, it will generate error 
######## traversing a list ##########
newlist = [i for i in some_list if i>25]
print(newlist)

newlist = some_list.copy()
print(newlist)

newlist = some_list + newlist # concatination of two lists 
print(newlist)

# Nested Lists 
nested_list = [10, 20, [30, 40], 50]
print(nested_list[2])
print(nested_list[2][0])

