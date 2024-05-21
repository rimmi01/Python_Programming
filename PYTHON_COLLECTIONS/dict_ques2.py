# given a string and a number N, we need to mirror the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to 'y', and so on. 


input_string = input("Enter string: ")
n = int(input("Enter N: "))

s1 = []
for i in range(ord('a'), ord('z') + 1, 1):
    s1.append(chr(i))
print(s1)

s2 = []
for j in range(ord('z'), ord('a') - 1, -1):
    s2.append(chr(j))
print(s2)

dict1 = dict(zip(s1, s2))
print(dict1)

prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# output_string = prefix + dict1[suffix[j]]
output_string = prefix
for char in suffix:
    output_string += dict1[char]

print(output_string)

