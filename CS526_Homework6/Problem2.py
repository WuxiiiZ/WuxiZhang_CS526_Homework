import sys

def readfile(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    arr = list(map(int, lines[1].strip().split(" ")))
    return arr

def sort(arr,digit):
    radixArray = [[] for _ in range(10)]    # create [] containing 10 empty [] to store from 0 to 9
    output = []
    for n in arr:
        remainder = (n // (10 ** (digit - 1))) % 10  # calculate the value of the current number on the specified digit bit
        radixArray[remainder].append(n) # put n into the [] corresponding to the digit
    for each_digit in radixArray:
        for element in each_digit:
            output.append(element)  
    return output
     
def radixSort(arr): 
    if not arr:
        return arr
    max_num = max(arr)
    digit = 1

    # while loop continues until all digits of max_num have been processed
    while max_num // (10 ** (digit - 1)) > 0:
        arr = sort(arr, digit)
        digit += 1
    return arr

# python3 Problem2.py ./sort_array/sort_array1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    arr = readfile(filename)
    print(radixSort(arr))

