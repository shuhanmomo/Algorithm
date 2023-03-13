'''
Covering Segments by Points Problem
Find the minimum number of points needed to
cover all given segments on a line.

Input: A sequence of n segments
[l1, r1], . . . , [ln, rn] on a line.

Output: A set of points of minimum
size such that each segment
[li , ri ] contains a point, i.e., there
exists a point x from this set such
that li ≤ x ≤ ri .

Input format. The first line of the input contains the number n of segments.
Each of the following n lines contains two integers li and ri
(separated by a space) defining the coordinates of endpoints of the
i-th segment.

Output format. The minimum number k of points on the first line and the
integer coordinates of k points (separated by spaces) on the second
line. You can output the points in any order. If there are multiple
such sets of points, you can output any of them.

Constraints. 1 ≤ n ≤ 100; 0 ≤ li ≤ ri ≤ 109 for all i.
'''


from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort()
    #print(segments)
    pts=[]
    x=segments[0].start
    pt=x
    while segments != []:   
        a=0        
        while x>=segments[0].start and x<=segments[0].end:
            k=0            
            while len(segments)>k and x>=segments[k].start and x<=segments[k].end:
                k+=1
            if k>=a:
                a=k
                pt=x
                #print("x is "+str(x)+"k is " + str(k) +" pt is"+str(pt)+str(segments[0]))
            if len(segments)==1:
                pt=x
                    
            x+=1
            #print("x is " +str(x))                 
        for num in range(k):
            segments.pop(0)
       # print(segments[0])
        
        if segments != []:
           x=segments[0].start
               # print(x)
               # print(x<segments[0].start or x>segments[0].end)
        if pts == []:           
            pts.append(pt)
        elif pt != pts[-1]:
            pts.append(pt)

  
    return pts


if __name__ == '__main__':
    input = stdin.read()
    #input = input()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

