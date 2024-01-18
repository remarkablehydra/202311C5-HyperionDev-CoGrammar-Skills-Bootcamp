'''Python code takes side1, side2 and side3 as user input for sides of the triangle.
Value sval calculated according to formula for area of triangle.
The area of the triangle is calculated and displayed.
Function math.Sqrt() is used.'''

side1 = float(input("Enter side 1 of a triangle: ")) # user enters values for sides of triangle

side2 = float(input("\nEnter side 2 of a triangle: "))

side3 = float(input("\nEnter side 3 of a triangle: "))

sval=(side1+side2+side3)/2

area_Triangle = math.sqrt(sval*(sval-side1)(sval-side2)(sval-side3))# calculating Area

print("Area of triangle: %0.2f" %area_Triangle)