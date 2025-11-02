import sys
import math

def pandemic(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

    n = int(lines[0])
    matrix = n * n
    infected_areas = set()

    for line in lines[1:]:
        coordinate = line.strip().split()
        x,y = int(coordinate[0]), int(coordinate[1])
        infected_areas.add((x,y))


    def recursion():
        growing_infection = set(infected_areas)
        num = len(infected_areas)
        for a in growing_infection:
            for b in growing_infection:
                if (a != b):
                    if abs(a[0]-b[0]) == 1 and abs(a[1]-b[1]) == 1:
                        new_areas = {(a[0],b[1]),(b[0],a[1])}
                        new_areas = {point for point in new_areas if 0 <= point[0] < n and 0 <= point[1] < n}
                        infected_areas.update(new_areas)
        new_num = len(infected_areas)
        if new_num > num:
            recursion()
        else:
            return None
    
    recursion()
    if len(infected_areas) == matrix:
        print("There are no healthy counties left")
    else:
        print("There are healthy counties left")


# python3 Problem2.py ./pandemic_input/pandemic_input1.txt
# python3 Problem2.py ./pandemic_input/pandemic_input2.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    pandemic(filename)

