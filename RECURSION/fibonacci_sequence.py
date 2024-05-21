# Make a function which calculates fibonacci sequence uing recursion 
# n is the nth term of the fibobacci series 
def fibonacci(n):
    if n == 1:
        return 0   # base case 
    elif n==2:
        return 1    # base case 
    else:
        return (fibonacci(n-1) + fibonacci(n-2))  # recursive case 
    

n = int(input("Enter n: "))
for i in range(1, n+1):
    print(fibonacci(i))
# print(fibonacci(n))
