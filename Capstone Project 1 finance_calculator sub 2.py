import math  # Import the math module at the beginning of the program

print('''Hello! Thank you for choosing our financial calculator. Your choices are:\n
 Investment - to calculate the amount of interest you'll earn in interest
 Bond - to calculate the amount you'll have to pay on a home loan''')

# Input from user starts conditional statements
choice = input("Please enter 'Investment' or 'Bond' to proceed:\n").lower()

# If the user chooses investment
if choice == "investment":
    # Input amount of money being deposited
    P = float(input("Enter the deposit amount:\n£"))
    
    # Input interest rate
    r = float(input("Enter the interest rate: "))
    r /= 100  # Convert percentage to decimal
    
    # Provide input number of years they plan on investing for
    t = int(input("Enter the number of years: "))
    
    # Choose input simple or compound interest
    interest = input("Enter the type of interest to be applied (simple/compound): ")
    
    # Variable to store the computed total amount
    A = 0
    
    # If the user chooses simple interest
    if interest.lower() == "simple":
        # Compute the simple interest using the given formula
        A = P * (1 + r * t)
    # Else if the user chooses compound interest
    elif interest.lower() == "compound":
        # Compute the compound interest using the given formula
        A = P * math.pow((1 + r), t)
    
    # Print out the computed interest amount
    print(f"Total amount:\n£{A:.2f}")

# Else if the user chooses bond
elif choice == "bond":
    # Input the present value of the house
    P = float(input("Enter the house value:\n£"))
    
    # Input the annual interest rate
    r = float(input("Enter the annual interest rate: "))
    
    # Input the number of months they plan to take to repay the loan
    n = int(input("Enter the number of months: "))
    
    # Calculate monthly interest rate
    i = (r / 100) / 12
    
    # Calculate monthly payment using the given formula
    x = (i * P) / (1 - math.pow((1 + i), -n))
    
    # Print out the computed monthly payment
    print(f"The monthly payment is:\n£{x:.2f}")

else:
    print("Sorry, your entry is invalid. Please try again.")
