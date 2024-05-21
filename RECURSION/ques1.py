# print from n to 1 


def decreasing(n):
    if n==0:
        return
    decreasing(n-1)
    print(n)


decreasing(5)
