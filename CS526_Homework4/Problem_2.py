import sys

def smallestNumber(input):
    with open(input, 'r') as f:
        lines = f.readlines()

    length = int(lines[0].strip())
    target = int(lines[1].strip())
    arr = [int(element) for element in (lines[2].split())]

    reversed_arr = sorted(arr, reverse=True)

    sum = 0
    count = 0
    for num in reversed_arr:
        sum += num
        count += 1
        if sum > target:
            break
    print(f"For input array, target: {target}, answer: {count}")

# example: python3 Problem_2.py ./Problem2_test/fewest_1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    smallestNumber(filename)

