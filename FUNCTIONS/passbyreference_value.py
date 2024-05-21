'''
Pass by value(Immutable object = strings, integers, float, tuples)
--> When passed to function, a cop of the object is created and assigned to local variable in function 
--> Any change made to them inside function, do not affect the original variable outside function 
'''

def addOne(x):
    x = x + 1
    print("Inside function: ", x)

x = 5 
addOne(x)
print("Outside function: ", x)


# pass by reference 
# in this we pass mutable object = like, list, dictionaries 
# reference to actual object is passes to function 
# changes inside the function will affect the original object 
def modifyList(lst):
    lst = [4, 5, 6]
    # lst.append(4)
    print("Inside function: ", lst)

lst = [1, 2, 3]
modifyList(lst)
print("Outside function: ", lst)



