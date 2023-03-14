# Dynamic Programming Problems
## 1. Money Change Again Problem
Compute the minimum number of coins needed
to change the given value into coins with denominations
1, 3, and 4.  
- **Input**: An integer money.
- **Output**: The minimum number
of coins with denominations 1, 3,
and 4 that changes money.
- **Input format**. Integer money.  
- **Output format**. The minimum number of coins with denominations 1, 3,
and 4 that changes money.  
- **Constraints**. 1 ≤ money ≤ 10** 3.

## 2. Primitive Calculator Problem
Find the minimum number of operations needed
to get a positive integer n from 1 by using only
three operations: add 1, multiply by 2, and multiply
by 3.  
- **Input**: An integer n.
- **Output**: The minimum number
of operations “+1”, “×2”, and “×3”
needed to get n from 1.
- **Input format**. An integer n.  
- **Output format**. In the first line, output the minimum number k of operations
needed to get n from 1. In the second line, output a sequence of
intermediate numbers. That is, the second line should contain positive
integers a0,a1, . . . ,ak such that a0 = 1, ak = n and for all 1 ≤ i ≤ k,
ai is equal to either ai−1 + 1, 2ai−1, or 3ai−1. If there are many such
sequences, output any one of them.  
- **Constraints**. 1 ≤ n ≤ 10** 6.

## 3. Edit Distance Problem
Compute the edit distance between two strings.  
- **Input**: Two strings.
- **Output**: The minimum number
of single-symbol insertions, deletions,
and substitutions to transform
one string into the other
one.
- **Input format**. Two strings consisting of lower case Latin letters, each
on a separate line.  
- **Output format**. The edit distance between them.  
- **Constraints**. The length of both strings is at least 1 and at most 100.

## 4. Longest Common Subsequence of Two Sequences Problem
Compute the maximum length of a common
subsequence of two sequences.  
- **Input**: Two sequences.
- **Output**: The maximum length of
a common subsequence.
- **Input format**. First line: n. Second line: a1,a2, . . . ,an. Third line: m. Fourth
line: b1,b2, . . . ,bm.  
- **Output format**. p.  
- **Constraints**. 1 ≤ n,m ≤ 100; −10** 9 ≤ ai ,bi ≤ 10** 9 for all i.

## 5. Longest Common Subsequence of Three Sequences Problem
Compute the maximum length of a common
subsequence of three sequences.  
- **Input**: Three sequences.
- **Output**: The maximum length of
a common subsequence.
- **Input format**. First line: n. Second line: a1,a2, . . . ,an. Third line: m. Fourth
line: b1,b2, . . . ,bm. Fifth line: l. Sixth line: c1, c2, . . . , cl .  
- **Output format**. p.  
- **Constraints**. 1 ≤ n,m,l ≤ 100; −10** 9 ≤ ai ,bi , ci ≤ 10** 9.

## 6. Maximum Amount of Gold Problem
Given a set of gold bars of various weights and
a backpack that can hold at most W pounds,
place as much gold as possible into the backpack.  
- **Input**: A set of n gold bars
of integer weights w1, . . . ,wn and
a backpack that can hold at most
W pounds.
- **Output**: A subset of gold bars
of maximum total weight not exceeding
W.
- **Input format**. The first line of the input contains an integer W (capacity
of the backpack) and the number n of gold bars. The next line contains
n integers w1, . . . ,wn defining the weights of the gold bars.  
- **Output format**. The maximum weight of gold bars that fits into a backpack
of capacity W.  
- **Constraints**. 1 ≤W ≤ 10** 4; 1 ≤ n ≤ 300; 0 ≤ w1, . . . ,wn ≤ 10** 5.

## 7. 3-Partition Problem
Partition a set of integers into three subsets with
equal sums. 
- **Input**: A sequence of integers
v1,v2, . . . ,vn.
- **Output**: Check whether it is possible
to partition them into three
subsets with equal sums, i.e.,
check whether there exist three
disjoint sets S1,S2,S3 ⊆ {1,2, . . . ,n}
such that S1∪S2∪S3 = {1,2, . . . ,n}
and sum(S1) = sum(S2) = sum(S3)
- **Input format**. The first line contains an integer n. The second line contains
integers v1,v2, . . . ,vn separated by spaces.  
- **Output format**. Output 1, if it possible to partition v1,v2, . . . ,vn into three
subsets with equal sums, and 0 otherwise.  
- **Constraints**. 1 ≤ n ≤ 20, 1 ≤ vi ≤ 30 for all i.
