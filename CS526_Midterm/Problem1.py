import sys

arr = []
days = 0
def snowfall(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    arr = list(map(int,lines[1].strip().split()))
    days = int(lines[0].strip())
    if days < 3:
        return "No"
    else:
        max_snow = arr[2]
        for i in range(1,days-2):
            max_snow = max(max_snow, arr[i+2]-arr[i-1])
        if max_snow > arr[days-1]/2:
            return "YES"
        else:
            return "NO"



#   python3 Problem1.py ./snowfall_input/snowfall_input1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    print(snowfall(filename))