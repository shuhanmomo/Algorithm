'''
Car Fueling Problem
Compute the minimum number of gas tank refills
to get from one city to another.

Input: Integers d and m, as well
as a sequence of integers stop1 <
stop2 < · · · < stopn.

Output: The minimum number
of refills to get from one city
to another if a car can travel
at most m miles on a full tank.
The distance between the cities is
d miles and there are gas stations
at distances stop1,stop2, . . . ,stopn
along the way. We assume that
a car starts with a full tank.

Try our Car Fueling interactive puzzle before solving this programming
challenge!

Input format. The first line contains an integer d. The second line contains
an integer m. The third line specifies an integer n. Finally, the last
line contains integers stop1,stop2, . . . ,stopn.

Output format. The minimum number of refills needed. If it is not possible
to reach the destination, output −1.

Constraints. 1 ≤ d ≤ 105. 1 ≤ m ≤ 400. 1 ≤ n ≤ 300. 0 < stop1 < stop2 <
· · · < stopn < d.
'''

from sys import stdin
def min_refills(distance, tank, stops):
    if tank>=distance:
        return 0
    elif stops==[] or (stops[0]>tank):
        return -1
    lastStop = 0
    stop_count =0
    remain = tank
    
    while stops !=[]:
        while stops !=[] and (stops[0]-lastStop)<=remain:
            remain -= (stops[0]-lastStop)
            lastStop=stops[0]    
            stops.pop(0)   
        if stops !=[]:  
            stop_count+=1
            remain = tank
            if (stops[0]-lastStop)>remain:
               return -1
        elif stops == [] and distance - lastStop <= tank and distance - lastStop > remain:
            stop_count+=1
        elif stops == [] and distance - lastStop> tank:
            return -1


    return stop_count


if __name__ == '__main__':
   d, m, _, *stops = map(int, stdin.read().split())
   #d, m, _, *stops = map(int, input().split())
   print(min_refills(d, m, stops))
   
