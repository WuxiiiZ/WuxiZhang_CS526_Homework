import sys
from math import inf

def readfile(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    A = list(map(int,lines[2].strip().split()))
    B = list(map(int,lines[3].strip().split()))
    return A, B

def longest_seq(A, B):
    m, n =len(A),len(B)
    memo = {}

    # position: how many elements in X (if X is empty position = -1)
    # turn: A or B
    def set_position(prev_position,cur_turn):
        key = (prev_position,cur_turn)
        if key in memo:
            return memo[key]

        # starting point is A (previous no num in X)
        if cur_turn == "A": #this time processing xi in A
            if prev_position == -1:
                prev_value = -inf
            else:
                prev_value = B[prev_position]
            max_len = 0     
            for i in range(prev_position+1, m):
                if A[i] > prev_value:
                    num = 1 + set_position(i, 'B') # call function for next choice
                    max_len = max(max_len, num)
        
        else: 
            if prev_position == -1:
                prev_value = -inf
            else:
                prev_value = A[prev_position]
            max_len = 0
            for j in range(prev_position+1, n):
                if B[j] > prev_value:
                    num = 1 + set_position(j, 'A') # call function for next choice
                    max_len = max(max_len, num)

        memo[key] = max_len
        return max_len
    return max(set_position(-1,"A"),set_position(-1,"B"))

# python3 Problem3.py ./longest_seq/longest_seq1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    A, B = readfile(filename)
    ans = longest_seq(A, B)
    print(f"Longest sequence: {ans}")

