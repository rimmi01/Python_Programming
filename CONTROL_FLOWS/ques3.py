# Take positive integer input and tell if it is a four digit number or not. 
num = int(input("Enter a positive integer: "))

if num < 10000 and num > 999:
     print("The number is a four digit number.")
else:
     print("The number is not a four digit number.")
     