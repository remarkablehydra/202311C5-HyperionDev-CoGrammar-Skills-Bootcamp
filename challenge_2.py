
# Write Python code to take the name of a user's favourite restaurant and store it in a variable called string_fav.
string_fav = input('Please enter your favourite restaurant: ')

# Write a statement to take in the user's favourite number. Use casting to store it in an integer variable called int_fav.
int_fav = int(input('Please enter your favourite number: '))

# Print out both of these using two separate print statements below what you have written.
print('Your favourite restaurant is: ', string_fav)
print('Your favourite number is: ', int_fav)

# Try to cast string_fav to an integer. What happens?
'''int(string_fav)''' # This will raise a ValueError because Python cannot convert a string that does not represent a number into an integer.
