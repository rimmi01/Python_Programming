# tuples 
# used to store multiple items in a variable 
colours = ("blue", "green", "red")  # packing of a tuple

fruit = ("apple",)
print(type(fruit))
print(colours[1]) # positive indexing 
print(colours[-1]) # negative indexing 
print(colours[1:3])
print(colours[-2:]) # -ve range indexing 


########to check if an item is present in a list or not #####
# if "green" in colours:
#     print("Green is part of tuple")


# traversing the tuple 
# for i in colours:
#     print(i)


# concatenate 2 tuples 
more_colours = ("blue", "brown")
# colours = colours + more_colours
print(colours)


##### Unpackaging of a tuple 
colour1, colour2, colour3 = colours
print(colour1, colour2, colour3)
