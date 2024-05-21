# what and why functions? 
# user defined funtions 

# def sum (num1, num2=0):
#     answer = num1+num2
#     return answer

# x=2
# y=3
# a=56
# b=1
# print("The sum is ", sum(x, y)) # here x, and, y, would be called as positional arguments, means ye postion ke according call honge, jo, function mein pehle declared hoga, and, pehle call kiya hoga uske saath hoga... 
# print("The sum is ", sum(a, b)) 




# Keyword argument (named arguments) 
# print("The sum is ", sum(num2=2, num1=3))


# default arguments 
# print("The sum is ", sum(3))


# to pass any number of arguments 
# def addAllNumbers(*args):
#     sumof = 0
#     for i in args:
#         sumof += i
#     return sumof

# output = addAllNumbers(1, 2, 34, 45, 23)
# print("The sum is: ", output)



# def studentInfo(**kwargs):
#     for x, y in kwargs.items():
#         print(x, "is", y)

# studentInfo(name="Urvi", age=27, city="Delhi")
# studentInfo(name="Rimmi", Age=28, city="Bangalore", Fullname= "Rimmi Goyal")





# writing a function for calculating sum from 1 to n 
def sumOneToN(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum


n = int(input("Enter n: "))
output = sumOneToN(n)
print("Sum of all numbers till n is", output)

n1 = int(input("Enter n1: "))
output1 = sumOneToN(n1)
print("The sum of all numbers till n1 is: ", output1)
