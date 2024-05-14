# to use if_elif_else statements using some problems:
# pass or fail program
a = float(input("Enter the marks in Maths: "))
b = float(input("Enter the marks in Science: "))
c = float(input("Enter the marks in English: "))
per = (a+b+c)/3
print("Percentage obatined: ",per)
if(a>33 and b>33 and c>33):
    if per>=40:
        print("Pass ✌️✌️")
else:
    print("Fail")