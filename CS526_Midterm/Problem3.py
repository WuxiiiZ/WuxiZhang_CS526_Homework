from collections import defaultdict
import sys

def shopingCart(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

    arr = list(lines[1].strip().split(','))

    left = 0    # left indicator
    num_item = 0    # maximum amount of items that can take
    categories = 0      # total categories selected between left and right pointer
    d = defaultdict(int)

    for right,food_type in enumerate(arr):    # food_type: breakfast, lunch, dinner...
        if d[food_type] == 0:
            categories += 1    # category: num of tags
        d[food_type] += 1

        while categories > 2:
            left_item = arr[left]
            d[left_item] -= 1
            if d[left_item] == 0:
                categories -= 1
            left += 1

        num_item = max(right - left + 1, num_item)
        
    return num_item


# python3 Problem3.py ./sc_input/sc_input3.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    num = shopingCart(filename)
    print(f"{num} items were selected")