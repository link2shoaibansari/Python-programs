# to use match case in python just like c and c++ has switch

b = float(input("Enter a number: "))
a = float(input("Enter a number: "))
print("1: Sum\n2: Subtract\n3: Multiply\n4: Divide\n")
op = int(input("Enter the options: "))
match op:
    case 1:
        sum = a+b
        print("The sum is: ",sum)
    case 2:
        sub = a-b
        print("The subtraction is: ",sub)
    case 3:
        mul =a*b        
        print("The multiplication is: ",mul)
    case 4:
        div = a/b
        print("The division is: ",div)
    case _:
        print("Enter the correct options:")
        
