# program to swap two numbers
print("Enter two numbers: ")
a = float(input())
b = float(input())
print("Before swapping: ")
print("a =",a,",b =",b)
a = a+b
b = a-b
a = a-b
print("After swapping: ")
print("a =",a,",b =",b)