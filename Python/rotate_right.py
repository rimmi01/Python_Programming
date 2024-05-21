# Input string
input_string = input("Enter a string: ")
# Integer input n
n = int(input("Enter the number of positions to rotate right: "))

# Adjust n if it's greater than the length of the string
n %= len(input_string)

# Perform the rotation without using functions
rotated_string = input_string[-n:] + input_string[:-n]

print("Rotated string:", rotated_string)
