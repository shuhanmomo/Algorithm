
'''
Sorted Array Search Problem
Search a key in a sorted array of keys.

Input: A sorted array K =
[k0, . . . ,kn−1] of distinct integers
(i.e., k0 < k1 < · · · < kn−1) and an integer
q.

Output: Check whether q occurs
in K.
'''

def binary(keys,q):
    min_i= 0
    max_i = len(keys)-1
    while max_i>=min_i:
        mid_i = (min_i+max_i)//2
        if keys[mid_i]==q:
            return mid_i
        elif keys[mid_i]<q:
            min_i = mid_i+1
        elif keys[mid_i]>q:
            max_i=mid_i-1
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary(input_keys, q), end=' ')
