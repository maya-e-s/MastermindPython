# Maya Stevenson 5/28/22
# Mastermind - 4 spots, 6 color choices = 1296 possible combinations

import numpy as np
from nextGuess import nextGuess 
from elimination import elimination     

def mastermind():
# create set 'A' and 'B'
# set A contains all unused combinations. Every time a code is used as a guess, that code is eliminated from A
# set B contains all possible codes that may match the secret code created by the codemaker 
    A = np.zeros((1296, 4), dtype=int) # all unused guesses
    i=0
    for j in range (1, 7):
        for k in range (1, 7):
            for m in range (1, 7):
                for n in range (1, 7):
                    A[i] = [j, k, m, n]
                    i=i+1
    B = np.copy(A) # possible codes left

    # start game
    print('Think of a 4 digit code containing the numbers 1-6, allowing repeats.\nThe computer will return a guess.\nEnter the number of red pegs (right color and right position)\n   and white pegs (right color wrong position).\nThe computer will guess your code in 5 guesses or less.\n\n')
    tries = 1
    pegs = np.array([0, 0])

    # first guess AABB --> speeds up process
    #guess = np.array([1, 1, 2, 2])
    #print('Computer guessed:', guess)
    #pegs[0] = input('Return pegs [red]: ')
    #pegs[1] = input('Return pegs [white]: ')
    #[A, B] = elimination(pegs, guess, A, B)
    #print(A.shape, B.shape)
    #tries = tries+1

    # the computer will continue making guesses until it guess correctly
    while pegs[0] != 4:
        [guess, A, B] = nextGuess(A, B)
        print("Computer guessed: ", guess)
        #pegs = input('Return pegs [red, white]: ')
        pegs[0] = input('Return pegs [red]: ')
        pegs[1] = input('Return pegs [white]: ')
        [A, B] = elimination(pegs, guess, A, B)
        tries = tries+1

    # computer guessed code; print success
    print('\nYour code is', guess)
    print('Computer guessed it in', tries-1, 'tries\n')

mastermind()