# Write a Python function to calculate the factorial of a number( a non-negative integer). The function accepts the number as an argument. 


# # function for calculating the factorial of a number 
def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for i in range(1, n+1):
            ans *= i

        return ans

n = int(input("Enter a number: "))

output = factorial(n)
print("The factorial is: ", output)


# for i in range (1, n+1):
#     n = n * i
    # print("The factorial of the number is: ", n)
    # return n