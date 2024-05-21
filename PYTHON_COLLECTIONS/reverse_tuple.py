input_tuple = (1, 2, 3, 4, 5, 6)
print(input_tuple)
list1 = []

for x in reversed(input_tuple):
    list1.append(x)

output_tuple = tuple(list1)
print(output_tuple)

