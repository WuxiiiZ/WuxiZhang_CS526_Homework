import sys

VOWELS = {
    'A': '.-',
    'E': '.',
    'I': '..',
    'O': '---',
    'U': '..-',
}


def readfile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    arr = lines[1].strip()
    return arr
# arr = readfile(filename)

def letter_sequence(arr):
    memo = {} #memo[(1, i)] memo[(2, i)] memo[(3, i)]
    n = len(arr)
    if n == 0:
        return 0

    def get_combinations(i):
        '''
        one_char = arr[i]
        two_chars = arr[i:i+2]
        three_chars = arr[i:i+3]
        '''
        #base case
        if i == 0:
            for row in [1, 2, 3]:
                piece = arr[0:row]
                if piece in VOWELS.values():
                    memo[(row, 0)] = 1
                else:
                    memo[(row, 0)] = 0
            return get_combinations(i + 1)

        if i < n:  
        #recursion
            for length in [1, 2, 3]:
                piece = arr[i:i+length]
                if len(piece) < length:
                    memo[(length,i)] = 0    # Here in fact is None, but for algorithm we set it as 0
                elif piece in VOWELS.values():
                    for index in [1, 2, 3]:
                        if i-index < 0:
                            memo[(index,i-index)] = 0
                    memo[(length,i)] = memo[(1,i-1)] + memo[(2,i-2)] + memo[(3,i-3)]
                else:
                    memo[(length,i)] = 0
            return get_combinations(i+1)
        
        elif i == n:
            return memo[(1,i-1)]+ memo[(2,i-2)] + memo[(3,i-3)]

    return get_combinations(0)

# python3 Problem2.py ./vowel_input/vowel_input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    arr = readfile(filename)
    if (len(arr) == 0):
        print("The Number of Vowel combinations is: 0")
    else:
        num = letter_sequence(arr)
        print(f"The Number of Vowel combinations is: {num}")

