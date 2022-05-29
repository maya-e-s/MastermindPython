# function compareCodes: compares sets A and B using the the number of red and white pegs that would be returned if the codebreaker guessed ‘b’ while the secret code was code ‘a’ 
# inputs: a - a four number code representing the secret code
#         b - a four number code representing a guess
# output: rw - set containing [red, white] peg combo corresponing with guesses 'a' and 'b'

import numpy as np

def compareCodes(a, b):
    rw = np.zeros(2, dtype=int)

    # check red pegs
    rw[0] = np.sum(np.equal(a,b))
    
    # check white pegs
    rw[1] = np.amin(np.array([np.sum(np.isin(a,b)) - rw[0], np.sum(np.isin(b,a)) - rw[0]]))
    return rw