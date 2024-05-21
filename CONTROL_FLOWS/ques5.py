# Take a positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15. 
num = int(input("Enter a positive integer: "))

if num % 5 == 0 or num % 3 == 0:
    if num % 15 != 0:
        print("This is the required number by the user")
    else:
        print("This number is the not the number which user wants.")
else:
    pass