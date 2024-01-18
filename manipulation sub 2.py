'''reads user input string
finds the length of the input sentence
prints length of the sentence
prints the last character 
replaces all instances of last character with the'@''
the variable last stores the last three characters from backward 
The variable five stores first three characters, length-2, and length-1
divided the given sentence into words
display each word in new line'''

str_manip = input("Enter the sentence: ")

setLength = len(str_manip)

print("\nSentence length: ", setLength)
 
print("\nLast character: ", str_manip[setLength-1])

new_char = '@'

new_string = str_manip.replace(str_manip[-1], new_char)

print("\nAfter replacing last character: ", (new_string))

lastThreeChar = str_manip[::-1][:3]

print("\nLast three characters in backward: ", lastThreeChar)

fiveChar = str_manip[:3]+str_manip[setLength-2]+str_manip[setLength-1]

print("\nFive characters: ",fiveChar)

setWord=str_manip.split()

print("\nDisplay each word in a newline: ")

for word in setWord:

    print(word)

