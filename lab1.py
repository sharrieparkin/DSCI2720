print("leap year check")

def leapyear(year:int):


    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 400 ==0) and (year % 100 == 0):
        return True
    else:
        return False

print(leapyear(2000))
print(leapyear(2009))
print(leapyear(1900))
print(leapyear(1992))

print("\n")

print("fib recursive")

def recursiveFib(x:int):
    if x==0:
        return 0
    elif x==1:
        return 1
    else: 
        return recursiveFib(x-1) + recursiveFib(x-2)   

print(recursiveFib(4)) 
print(recursiveFib(10))

print("\n")

print("fib iterative")
def iterativeFib(n:int):
    x=0
    y=1

    for i in range(n-1):
        z=x+y
        x=y
        y=z
    return z

print(iterativeFib(4))
print(iterativeFib(10))

'''
The iterative code for Fibonacci is faster running the code while recursive can run slower if the value is too large. 
'''