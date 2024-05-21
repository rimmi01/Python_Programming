n = int(input("Enter n: "))

# print(ord('A'))
# print(ord('a'))

start_from = ord('A')

for i in range(0, n):
    for j in range(0, i+1):
        char_to_print = chr(start_from + j)
        print(char_to_print, end="")
    print()