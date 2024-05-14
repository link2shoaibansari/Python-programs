# # defining a function in python and returning it using return keyword and calling it outside the defined function

def Mean1(a,b):
     print("The mean is: ",(a+b)/2)

Mean1(4,4)

def Mean2(*num):
    sum1 = 0
    for i in num:
        sum1 = sum1+i
    print("The mean is: ",sum1/len(num))

Mean2(4,4,4,4,4)


def Mean3(*number):
    sum2 = 0
    for i in number:
        sum2 = sum2+i
    return sum2/len(number)

c = Mean3(6,6,6)
print("The mean is: ",c)