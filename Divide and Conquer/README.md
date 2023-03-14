# Divide-and-Conquer Problems
## 1. Sorted Array Multiple Search Problem
Search multiple keys in a sorted sequence of keys.  
- **Input**: A sorted array K of distinct integers and an array Q =
[q0, . . . ,qm−1] of integers.
- **Output**: For each qi , check whether it occurs in K.
- **Input format**. The first two lines of the input contain an integer n and a sequence
k0 < k1 < . . . < kn−1 of n distinct positive integers in increasing
order. The next two lines contain an integer m and m positive integers
q0,q1, . . . ,qm−1.  
- **Output format**. For all i from 0 to m−1, output an index 0 ≤ j ≤ n−1 such
that kj = qi , or −1, if there is no such index.  
- **Constraints**. 1 ≤ n ≤ 3 · 10** 4; 1 ≤ m ≤ 10** 5; 1 ≤ ki ≤ 10** 9 for all 0 ≤ i < n;
1 ≤ qj ≤ 10** 9 for all 0 ≤ j < m.

## 2. Binary Search with Duplicates Problem
Find the index of the first occurrence of a key in
a sorted array.  
- **Input**: A sorted array of integers
(possibly with duplicates)
and an integer q.
- **Output**: Index of the first occurrence
of q in the array or “−1”
if q does not appear in the array.
- **Input format**. The first two lines of the input contain an integer n and
a sequence k0 ≤ k1 ≤ · · · ≤ kn−1 of n positive integers in non-decreasing
order. The next two lines contain an integer m and m positive integers
q0,q1, . . . ,qm−1.  
- **Output format**. For all i from 0 to m− 1, output the index 0 ≤ j ≤ n − 1 of
the first occurrence of qi (i.e., kj = qi ) or −1, if there is no such index.  
- **Constraints**. 1 ≤ n ≤ 3 · 10** 4; 1 ≤ m ≤ 10** 5; 1 ≤ ki ≤ 10** 9 for all 0 ≤ i < n;
1 ≤ qj ≤ 10** 9 for all 0 ≤ j < m.

## 3. Majority Element Problem
Check whether a given sequence of numbers contains
an element that appears more than half of
the times.  
- **Input**: A sequence of n integers.
- **Output**: 1, if there is an element
that is repeated more than n/2
times, and 0 otherwise.
- **Input format**. The first line contains an integer n, the next one contains
a sequence of n non-negative integers. a0, . . . ,an−1.  
- **Output format**. Output 1 if the sequence contains an element that appears
more than n/2 times, and 0 otherwise.  
- **Constraints**. 1 ≤ n ≤ 10** 5; 0 ≤ ai ≤ 10** 9 for all 0 ≤ i < n.

## 4. Speeding-up Randomized QuickSort Problem
Sort a given sequence of numbers (that
may contain duplicates) using a modification
of RandomizedQuickSort that works in
O(nlogn) expected time.  
- **Input**: An integer array with
n elements that may contain
duplicates.
- **Output**: Sorted array (generated
using a modification
of RandomizedQuickSort) that
works in O(nlogn) expected
time.
- **Input format**. The first line of the input contains an integer n. The next
line contains a sequence of n integers a0,a1, . . . ,an−1.  
- **Output format**. Output this sequence sorted in non-decreasing order.  
- **Constraints**. 1 ≤ n ≤ 10** 5; 0 ≤ ai ≤ 10** 9 for all 0 ≤ i < n.

## 5. Number of Inversions Problem
Compute the number of inversions in a sequence of integers.  
- **Input**: A sequence of n integers a1, . . . ,an.
- **Output**: The number of inversions
in the sequence, i.e., the
number of indices i < j such that
ai > aj .
- **Input format**. The first line contains an integer n, the next one contains
a sequence of integers a1, . . . ,an.  
- **Output format**. The number of inversions in the sequence.  
- **Constraints**. ≤ n ≤ 30000, 1 ≤ ai ≤ 10** 9 for all 1 ≤ i ≤ n.
