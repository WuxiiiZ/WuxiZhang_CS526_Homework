import sys

def readFile(filename):
    with open (filename,'r') as f:
        lines = f.readlines()

    streams = []
    n = int(lines[0].strip())
    for line in lines[1:n+1]:
        num = line.strip().split()  # deal with input（e.g, B 20 -875 G 3 -93)
        bx,by = int(num[1]),int(num[2])
        gx,gy = int(num[4]),int(num[5])
        streams.append([bx,by,gx,gy])
    return streams

def slope(bx,by,gx,gy):
    if (gx-bx) == 0:
        return None
    return (gy-by)/(gx-bx)

def checkEliminate(filename):
    streams = readFile(filename)
    slope_set = set()
    for i in range(len(streams)):
        bx, by, gx, gy = streams[i]
        rate = slope(bx,by,gx,gy)
       
        slope_set.add(rate)
        if len(slope_set) > 1:
            return "All Ghosts: were not eliminated"
    return "All Ghosts: were eliminated"

# example: python3 Problem4.py ./Test_4/ghostbusters_input_0.txt RETURN result of checkEliminate("./Test_4/ghostbusters_input_0.txt")
if __name__ == '__main__':
    filename = sys.argv[1]
    print(checkEliminate(filename))