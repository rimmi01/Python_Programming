# sum of numbers from 1 to n 

def summ(n):
    if n == 1:
        return 1
    output = n + summ(n-1)
    return output

n = int(input("Enter a number: "))
print(summ(n))

