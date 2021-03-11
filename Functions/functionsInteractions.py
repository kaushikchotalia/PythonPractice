from random import shuffle
# example = [1,2,3,4,5,6,7]
# result = shuffle(example)
# print(result)

#example = [1,2,3,4,5,6,7]
def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    shuffle(mylist)
    return mylist

#result = shuffle_list(example)
#print(result)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        # Recall input() returns a string
        guess = input("Pick a number:0,1 or 2:    ")
    return int(guess)

#my_index = player_guess()

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct Guess!")
    else:
        print('Wronng Guess! Better Luck Next time')
        print(mylist)

# Initial List
mylist = ['O',' ',' ']
# Shuffle List
mixedup_list = shuffle_list(mylist)
# User Guess
guess = player_guess()
# Check Guess
check_guess(mixedup_list,guess)