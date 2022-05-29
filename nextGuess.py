# function nextGuess: returns next guess computer should make by using the minimax technique (minimizes maximum loss)
# inputs: A - set containing all unused guesses. Every time a code is used as a guess, that code is eliminated from A
#                note: even if we know a guess is incorrect, it mihght provide us with valuable information 
#         B - set containing all possible codes remaining. These may match the secret code created by the codemaker 
# outputs: guess - four numbers representing the next guess the computer should make
#         A - updated set A
#         B - updated set B

import numpy as np
from compareCodes import compareCodes

def nextGuess(A, B):
    print("thinking of next guess...")

    # find worst case scenario of remaining possible codes for each guess in A
    [rA, cA] = A.shape
    maxScore = np.zeros(rA, dtype=int) # worst case scenario of number of codes remaining for every guess in A
    pegCount = {} # create a dictionary to store rw counts 
    # compare every guess in A to those remaining in B
    i = 0
    for rowA in A: # for each unused guess in A
        pegCount.clear() # clear dictionary for each rowA 
        for rowB in B: # for each possible code left (B)
            rw = compareCodes(rowA, rowB) # pegs returned for guess A on code B
            rw_key = np.array2string(rw)
            pegCount[rw_key] = pegCount.get(rw_key,0) + 1 # sum rw counts per guess A
        maxScore[i] = max(pegCount.values()) # save the worst case scenario (max number of codes that could remain in B after guessing A)
        i = i+1

    # The minimum element of maxScore shows the best of the worst case scenarios 
    minScore = np.amin(maxScore) # minimum worst case scenario (number of codes that will remain)
    nextGuess = np.array(A[np.where(maxScore == minScore)]) # actual guesses (rows of A) with minimum maxScore
    #print(minScore)

    # If an element of nextGuess also exists in B, that guess is played. 
    # If none of the elements of nextGuess exist in B, then the first element in nextGuess is played
    nextGuessInB = nextGuess[(nextGuess[:,:] == B[:, None]).all(axis=-1).any(axis=0)]  # array of nextGuess that are also in B
    if np.size(nextGuessInB) > 0:
        guess = nextGuessInB[0]
    else:
        guess = nextGuess[0]
    return [guess, A, B]