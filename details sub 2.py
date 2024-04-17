'''store name as an input command
store age as an integer using the input command
store house number as an input command
store street name as an input command
use print command as output for sentence with all input commands'''

name = input('Please enter your name: ')
age = input('Please enter your age: ')
housenumber = input('Please enter your house number: ')
streetname = input('Please enter your street name: ')
roadtype = input('Please confirm the type of road you live on: ')
sentence = (f'This is {name}.They are {age} years old. They live at {housenumber} {streetname} {roadtype}.')
print(sentence)
