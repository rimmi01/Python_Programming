# # Input string
input_string = input("Enter a string: ")
# # Integer input n
n = int(input("Enter the number of positions to rotate left: "))

# Adjust n if it's greater than the length of the string
n %= len(input_string)

# Perform the rotation without using functions
rotated_string = input_string[n:] + input_string[:n]

print("Rotated string:", rotated_string)


# l = input_string.len()
# d = l-n
# print(input_string[d:])
# print(input_string[0:d])