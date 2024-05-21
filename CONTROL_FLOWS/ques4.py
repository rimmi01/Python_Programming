# Take 3 positive integers input and print the greatest of them. 


########************Method 1 ************##############

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

# if num1 > num2 and num1 > num3:
#     print("Number 1 is the greatest")
# elif num2 > num3 and num2 > num1:
#     print("Number 2 is the greatest")
# elif num3 > num1 and num3 > num2:
#     print("Number 3 is the greatest")
# else:
#     print("Either all numbers are equal or any of the two numbers are equal and greater.")




########************Method 2 ************##############

if num1 > num2:
    if num1 > num3:
        print("Number 1 is the greatest")
    else:
        print("Number 3 is the greatest")
else:
    if num2 > num3:
        print("Number 2 is the greatest")
    else:
        print("Number 3 is the greatest")
        