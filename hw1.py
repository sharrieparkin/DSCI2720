'''
HOMEWORK 1
9/6/22
'''


'''
Have students code up (on paper) the same for finding the thirdMax? Assume the input is an array with 3
or more elements. Do not use the sort function.
'''


def thirdlarg():

    arr = [10, 1, 20, 16]
    x= len(arr)

    max1=arr[0]
    max2=arr[0]
    max3=arr[0]


    for i in range(x):

        if arr[i] > max1:
            max1 = arr[i]

        elif arr[i] > max2 and arr[i] < max1:
            max2 = arr[i]
       
        else:
            arr[i] > max3 and arr[i] < max2
            max3 = arr[i]
       

    print("The largest value is",max1)
    print("The second largest value is",max2)
    print("The third largest value is",max3)

print(thirdlarg())
