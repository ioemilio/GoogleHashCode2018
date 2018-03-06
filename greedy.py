from collections import defaultdict
import random

# PARAMS
def main():
    filename = "a_example"
    # filename = "b_should_be_easy"
    # filename = "c_no_hurry"
    # filename = "d_metropolis"
    # filename = "e_high_bonus"
    input_file = "inputs/"+filename+".in"

    # READ INPUT
    with open(input_file) as fin:
        R, C, F, N, B, T = [int(x) for x in fin.readline().split()]
        rides = defaultdict(tuple)
        ride_number = 0
        for n in range(N):
            a, b, x, y, s, f = [int(x) for x in fin.readline().split()]
            rides[ride_number] = (a, b, x, y, s, f)
            ride_number += 1


    # COMPUTE SOLUTION
    free = defaultdict(int)
    pos = defaultdict(tuple)
    sol = defaultdict(list)
    for c in range(F):
        free[c] = 0
        pos[c] = (0, 0)
        sol[c] = []

    for t in range(T):
        print(t, "/", T)
        for c in range(F):
            if free[c] == t:
                if len(rides) != 0:
                    ride_number = assignToRide(rides, free, pos, c, t)
                    del rides[ride_number]
                    sol[c].append(ride_number)


    # WRITE OUTPUT
    with open("outputs/"+filename+"-greedy.out", "w") as fout:
        for c in range(F):
            output_line = str(len(sol[c]))
            for r in sol[c]:
                output_line += " " + str(r)
            fout.write(output_line + "\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def distance(a, b, x, y):
    return abs(a - x) + abs(b - y)

def assignToRide(rides, free, pos, c, t):
    max_ride, max_value, max_arrival_time = -1, -1, -1
    for ride_number in rides.keys():
        a, b, x, y, s, f = rides[ride_number]
        ride_dist = distance(a, b, x, y)
        goto_dist = distance(pos[c][0], pos[c][1], a, b)
        arrival_time_s = t + goto_dist
        arrival_time_f = t + ride_dist + goto_dist
        waiting_time = 0 if arrival_time_s > s else s - arrival_time_s

        if goto_dist + waiting_time == 0:
            value = float("Inf")
        else:
            value = 0 if arrival_time_f > f else ride_dist/(goto_dist + waiting_time)

        if value > max_value:
            max_value = value
            max_ride = ride_number
            max_arrival_time = arrival_time_f

    pos[c] = (rides[max_ride][2], rides[max_ride][3])
    free[c] = max_arrival_time

    return max_ride

if __name__ == '__main__':
    main()
