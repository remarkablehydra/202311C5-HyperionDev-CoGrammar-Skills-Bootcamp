'''Save variable (sentence) as string 
Assign a new name for the string, use replace function, then substitute new character space for old character exclamation mark
Use print command to obtain output
Assign a new name for the string, use upper function, leave brackets blank
use print command to obtain output
for the same string as line 4 , use slicing to reverse string
use print command to obtain output either as sentence or uppercase sentence 
Methods such as: Using for loop and appending characters in reverse order,
Using while loop to iterate string characters in reverse order and append them,
Using string join() function with reversed() iterator,
Creating a list from the string and then calling its reverse() function,
and Recursion can also be used but slciing is most efficent'''

string = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
new_string = string.replace("!", " ")
print(new_string)

new_stringtwo = new_string.upper()
print(new_stringtwo)

print(new_string[::-1]) #completed as a normal sentence
print(new_stringtwo[::-1]) #completed as uppercase