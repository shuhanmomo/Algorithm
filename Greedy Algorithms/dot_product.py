'''
Maximum Product of Two Sequences Problem
Find the maximum dot product of two sequences
of numbers.

Input: Two sequences of n positive
integers: price1, . . . ,pricen
and clicks1, . . . , clicksn.

Output: The maximum value
of price1 · c1 + · · · + pricen
· cn,
where c1, . . . , cn is a permutation
of clicks1, . . . , clicksn.

Input format. The first line contains an integer n, the second one contains
a sequence of integers price1, . . . ,pricen, the third one contains
a sequence of integers clicks1, . . . , clicksn.

Output format. Output the maximum value of (price1 ·c1 +· · ·+pricen
·cn),
where c1, . . . , cn is a permutation of clicks1, . . . , clicksn.
Constraints. 1 ≤ n ≤ 103; 0 ≤ pricei , clicksi ≤ 105 for all 1 ≤ i ≤ n.


'''


from itertools import permutations
def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product

def max_dot_product_new(first_sequence, second_sequence):
    max_product = 0
    while first_sequence !=[]:
        max_1 = max(first_sequence)
        max_2 = max(second_sequence)
        first_sequence.remove(max_1)
        second_sequence.remove(max_2)
        max_product += max_1 * max_2
    return max_product




if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product_new (prices, clicks))
    
