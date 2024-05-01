# to find area of circle, triangle, square, rectangle
# calculate average marks scored by a student in 5 subjects
# converting temperature from celcius to farenhite {°F = (9/5 × °C) + 32}
radius = float(input("Enter the radius of circle: "))
areac = 3.14*(radius**2)
print("The area of circle is:",areac)
base = float(input("Enter the base length of triangle: "))
height = float(input("Enter the height of triangle: "))
areat = 0.5*base*height
print("The area of triangle is:",areat)
side = float(input("Enter the side length of square: "))
areas = side**2
print("The area of square is:",areas)
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
arear = 2*(length+breadth)
print("The area of rectangle is:",arear)
print("\n\n")
print("Enter the marks in 5 subjects: ")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
avg = (a+b+c+d+e)/5
print("The average score of the student is: ",avg)
print("\n\n")
celcius = float(input("Enter temperature in celcius: "))
farenhite = ((9/5)*celcius)+32
print("The temperature in farenhite is: ",farenhite)