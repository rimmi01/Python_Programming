# factorial(n)
# factorial(n-1)
############## factorial calculation function recurrsion approach 

def factorial(n):
    if n==0:
        return 1
    output = n * factorial(n-1)
    return output


n = int(input("Enter a number: "))
print(factorial(n))
