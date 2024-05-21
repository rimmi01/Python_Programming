# Make a function which calculates 'a' raised to the power 'b' using recursion. 


def power_calculation(a, b):
    if b == 0:
        return 1
    output = a * power_calculation(a, b-1)
    return output


# a = 2
# b = 3

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(power_calculation(a, b))

