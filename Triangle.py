x = int(input("Enter a valid length"))
y = int(input("Enter a valid length"))
z = int(input("Enter a valid length"))

if x == y == z:
    print("This is a equilateral triangle")

elif x == y or y == z or x == z:
    print("This is a isosceles triangle")

else:
    print("This is scalene triangle") 