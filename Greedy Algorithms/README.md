# Greedy Algorithm Problems
## 1. Money Change Problem
Compute the minimum number of coins needed to change the given value into coins with denominations 1, 5, and 10.  
- **Input**: An integer money.
- **Output**: The minimum number of coins with denominations 1, 5, and 10 that changes money.
- **Input format**. Integer money.  
- **Output format**. The minimum number of coins with denominations 1, 5, 10 that changes money.  
- **Constraints**. 1 ≤ money ≤ 10**3.  

## 2. Maximizing the Value of the Loot Problem
Find the maximal value of items that fit into the backpack.  
- **Input**: The capacity of a backpack W as well as the weights (w1, . . . ,wn) and costs (c1, . . . , cn) of n different compounds.
- **Output**: The maximum total value of fractions of items that fit into the backpack of the given capacity: i.e., the maximum value of c1 · f1 + · · · + cn · fn such that w1·f1+· · ·+wn·fn ≤W and 0 ≤ fi ≤
1 for all i (fi is the fraction of the i-th item taken to the backpack).
- **Input format**. The first line of the input contains the number n of compounds
and the capacity W of a backpack. The next n lines define
the costs and weights of the compounds. The i-th line contains the
cost ci and the weight wi of the i-th compound.  
- **Output format**. Output the maximum value of compounds that fit into
the backpack.  
- **Constraints**. 1 ≤ n ≤ 10^3, 0 ≤ W ≤ 2 · 10^6; 0 ≤ ci ≤ 2 · 10^6, 0 < wi ≤ 2 · 10^6
for all 1 ≤ i ≤ n. All the numbers are integers.  

## 3. Car Fueling Problem
Compute the minimum number of gas tank refills
to get from one city to another.  
- **Input**: Integers d and m, as well
as a sequence of integers stop1 <
stop2 < · · · < stopn.
- **Output**: The minimum number
of refills to get from one city
to another if a car can travel
at most m miles on a full tank.
The distance between the cities is
d miles and there are gas stations
at distances stop1,stop2, . . . ,stopn
along the way. We assume that
a car starts with a full tank.
- **Input format**. The first line contains an integer d. The second line contains
an integer m. The third line specifies an integer n. Finally, the last
line contains integers stop1,stop2, . . . ,stopn.  
- **Output format**. The minimum number of refills needed. If it is not possible
to reach the destination, output −1.  
- **Constraints**. 1 ≤ d ≤ 10**5. 1 ≤ m ≤ 400. 1 ≤ n ≤ 300. 0 < stop1 < stop2 <
· · · < stopn < d.  

## 4. Maximum Product of Two Sequences Problem
Find the maximum dot product of two sequences
of numbers.  
- **Input**: Two sequences of n positive
integers: price1, . . . ,pricen
and clicks1, . . . , clicksn.
- **Output**: The maximum value
of price1 · c1 + · · · + pricen
· cn,
where c1, . . . , cn is a permutation
of clicks1, . . . , clicksn.
- **Input format**. The first line contains an integer n, the second one contains
a sequence of integers price1, . . . ,pricen, the third one contains
a sequence of integers clicks1, . . . , clicksn.  
- **Output format**. Output the maximum value of (price1 ·c1 +· · ·+pricen
·cn),
where c1, . . . , cn is a permutation of clicks1, . . . , clicksn.  
- **Constraints**. 1 ≤ n ≤ 10** 3; 0 ≤ pricei , clicksi ≤ 10** 5 for all 1 ≤ i ≤ n.

## 5. Covering Segments by Points Problem
Find the minimum number of points needed to
cover all given segments on a line.  
- **Input**: A sequence of n segments
[l1, r1], . . . , [ln, rn] on a line.
- **Output**: A set of points of minimum
size such that each segment
[li , ri ] contains a point, i.e., there
exists a point x from this set such
that li ≤ x ≤ ri .
- **Input format**. The first line of the input contains the number n of segments.
Each of the following n lines contains two integers li and ri
(separated by a space) defining the coordinates of endpoints of the
i-th segment.  
- **Output format**. The minimum number k of points on the first line and the
integer coordinates of k points (separated by spaces) on the second
line. You can output the points in any order. If there are multiple
such sets of points, you can output any of them.  
- **Constraints**. 1 ≤ n ≤ 100; 0 ≤ li ≤ ri ≤ 10** 9 for all i.
