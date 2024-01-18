'''int() is a constructor of the built-in int class. 
The int() accepts a string or a number and converts it to an integer.
When you call the int(), you create a new integer object.
The float() accepts either an integer or a floating-point number, and converts it to a floating-point number
The str() converts a number into a string.'''

num1 = 99.23
num2 = 23
num3 = 150
string1 = '100'

number = int(num1)
print(number) #99

number = float(num2)
print(number) #23.0

number = str(num3)
print(number) #150

number = int(string1)
print(number) #100