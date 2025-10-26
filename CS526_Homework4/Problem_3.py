import sys
import time
import math
from math import gcd
from collections import defaultdict


def countTriangles(filename):
    start = time.time() 
    with open(filename, 'r') as f:
        lines = f.read().strip().splitlines()

    n = int(lines[0])
    points = [list(map(int, line.split())) for line in lines[1:n+1]]

    count = 0
    eps = 1e-6  # To avoid float error

    for i in range(n):
        x0, y0 = points[i]
        freq = defaultdict(int)    # Store the frequency of vectors starting from the vertex

        for j in range(n):
            if j == i:
                continue
            dx = points[j][0] - x0
            dy = points[j][1] - y0
            if dx == 0 and dy == 0:
                continue

            g = gcd(abs(dx), abs(dy))      # simplify the vector
            dx //= g
            dy //= g

            # Vectors in opposite directions are simplified to be in the same direction
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy

            freq[(dx, dy)] += 1

        if not freq:
            continue

        pairs = 0
        for (dx, dy), c in freq.items():
            px, py = dy, -dx   # Set the perpendicular vector
            # # Vectors in opposite directions are simplified to be in the same direction
            if px < 0 or (px == 0 and py < 0):
                px, py = -px, -py
            pairs += c * freq.get((px, py), 0)

        # Each pair of perpendicular directions is counted twice (A->B and B->A)
        count += pairs // 2


    end = time.time()
    print(f"Used time: {end-start}")
    print(f"Number of right triangles: {count}")
    return count


           
# example: python3 Problem_3.py ./Problem3_test/righttangles_1.txt
# example: python3 Problem_3.py ./Problem3_test/rightangles_2.txt
# example: python3 Problem_3.py ./Problem3_test/rightangles_3.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    countTriangles(filename)