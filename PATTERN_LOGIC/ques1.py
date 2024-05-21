# for i in range(0, 11):
#     print(i)

# print("hello", end=" ")
# print("hi")
# print("something")


num = int(input("Enter the number: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

