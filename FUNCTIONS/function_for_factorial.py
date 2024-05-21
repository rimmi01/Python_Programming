def factorial(n):
    answer = 1
    if n == 0:
        answer = 1
    else:
        for i in range(1, n+1):
            answer *= i
        return answer

n = int(input("Enter n: "))

output = factorial(n)
print("The factorial of the given number is: ", output)
