from collections import defaultdict
import random

# PARAMS
filename = "e_high_bonus"
input_file = "inputs/"+filename+".in"

# READ INPUT
with open(input_file) as fin:
    R, C, F, N, B, T = [int(x) for x in fin.readline().split()]
    rides = []
    for n in range(N):
        a, b, x, y, s, f = [int(x) for x in fin.readline().split()]
        rides.append((a, b, x, y, s, f))

# COMPUTE SOLUTION
sol = defaultdict(list)
ride_number = 0
for ride in rides:
    x = random.randint(1, F)
    sol[x].append(ride_number)
    ride_number += 1

# WRITE OUTPUT
with open("outputs/"+filename+"-random.out", "w") as fout:
    for f in range(1, F+1):
        output_line = str(len(sol[f]))
        for r in sol[f]:
            output_line += " " + str(r)
        fout.write(output_line + "\n")
