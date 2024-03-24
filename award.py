# Welcome message and request inputs from the user
print('Welcome to the Annual HD Triathlon! \n To qualify for the leaderboard, please provide your individual times in minutes for each event: ')
swimtime = int(input('Swimming: '))
cycletime = int(input('Cycling: '))
runtime = int(input('Running: '))

# Calculating the total time taken to complete the triathlon
totduration = swimtime + cycletime + runtime

# Displaying the total time taken
print('Total time taken to complete marathon:', totduration, 'minutes')

# Matching time range with appropriate award and printing outputs
qualifying_time = 100
if totduration <= qualifying_time:
    print('You are awarded Provincial Colours!')

elif totduration <= (qualifying_time + 5):
    print('You are awarded Provincial Half Colours!')

elif totduration <= (qualifying_time + 10):
    print('You are awarded Provincial Scroll!')

else:
    print('No award. Commiserations')
