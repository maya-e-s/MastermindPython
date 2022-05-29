# function elimination: Takes the returned pegs and eliminates impossible combinations. 
#                       To eliminate impossible solutions from B, the guess is compared to every element in B. 
#                       For every element, if comparing the two codes does not result in the same combination of red and white pegs as the codemaker returned, that code is removed from B. 
# inputs: pegs - the [red, white] pegs returned by player
#         guess - the computers current guess
#         A - matrix holding unused guesses
#         B - matrix holding possible codes left
# outputs:A - matrix holding unused guesses
#         B - matrix holding possible codes left

import numpy as np
from compareCodes import compareCodes

def elimination(pegs, guess, A, B):
    # remove guess from A
    [rA, cA] = A.shape
    for i in range (0,rA): # for every element in A
        if (A[i] == guess).all(axis=0): # if A contains guess
            A = np.delete(A, (i), axis=0) # delete guess
            rA = rA-1 # decrement size of A
            break

    # create new B based on returned rw pegs 
    [rB, cB] = B.shape
    newB = np.empty([0,4], int)
    for i in range (0,rB): 
        rw = compareCodes(guess, B[i])
        if (rw == pegs).all(axis=0):
            newB = np.append(newB, [B[i]], axis=0)
    if 'newB' not in locals(): # one of the red/white pegs returned by the player was incorrect, and the correct code has been eliminated
        print('The pegs you returned are invalid. Please check each of your responses and try again.\n')
        quit()
    B = np.copy(newB)
    return [A, B]