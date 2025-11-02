import sys
import math

def game(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

    n = int(lines[0])
    symbols = set(lines[1].strip().split(','))
    m = int(math.isqrt(n))
    if m*m != n:
        return 'The board is invalid'
    matrix = []
    for line in lines[2:]:
        row = line.strip().split(',')
        if len(row) != n:
            return 'The board is invalid'
        matrix.append(row)
    
    rows = [set() for _ in range(n)] # for each row in matrix
    columns = [set() for _ in range(n)] # for each column in matrix
    sub_matrices = [[set() for _ in range(m)] for _ in range(m)]  # set in form of arr[i][j] 

    for i in range(n):
        for j in range(n):
            e = matrix[i][j]
            if e == '.':
                continue
            if e not in symbols:
                return 'The board is invalid'

            if e in rows[i] or e in columns[j] or e in sub_matrices[i//m][j//m]:
                return 'The board is invalid'
            else:
                rows[i].add(e)
                columns[j].add(e)
                sub_matrices[i//m][j//m].add(e)
    
    return 'The board is valid'
    

# python3 Problem4.py ./spg_input/spg_input1.txt
# python3 Problem4.py ./spg_input/spg_input2.txt
if __name__ ==  "__main__":
    filename = sys.argv[1]
    print(game(filename))