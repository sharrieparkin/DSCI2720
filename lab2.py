
def squareRootFinder():
    number= int(input("Enter a number: "))
    sr= number ** (1/2)
    print(round(sr,5))
squareRootFinder()

print("\n")

def nthRootFinder():
    number=int(input("Enter a number: "))
    root=int(input("Enter root: "))
    nr = number ** (1/root)
    print(round(nr, 5))
nthRootFinder()    

'''
def squareRootFinder(number:int,iterations:int)->str:
    number=int(input("Enter a number:"))
    sqroot = number ** (1/2)
    print(str(sqroot))
squareRootFinder(number, iteration)



def nthRootFinder(number:int,iterations:int,n:int)->str
'''

print("\n")


def squareRoot(number, precision):
 
    start = 0
    end, ans = number, 1
 
   
    while (start <= end):
        mid = int((start + end) / 2)
 
        if (mid * mid == number):
            ans = mid
            break
 

        if (mid * mid < number):
            start = mid + 1
            ans = mid
 
    
        else:
            end = mid - 1
 
    
    increment = 0.1
    for i in range(0, precision):
        while (ans * ans <= number):
            ans += increment
 
    
        ans = ans - increment
        increment = increment / 10
 
    return ans

print(round(squareRoot(9, 2), 5))
print(round(squareRoot(20, 9), 5))


