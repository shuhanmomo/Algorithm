'''
Binary Search with Duplicates Problem
Find the index of the first occurrence of a key in
a sorted array.

Input: A sorted array of integers
(possibly with duplicates)
and an integer q.

Output: Index of the first occurrence
of q in the array or “−1”
if q does not appear in the array.
'''

def binary_search(keys, query):
    min_i=0
    max_i=len(keys)-1
    while min_i<=max_i:
        mid_i=(max_i+min_i)//2
        if keys[mid_i]==query:
            return mid_i,min_i
        elif keys[mid_i]<query:
            min_i=mid_i+1
        elif keys[mid_i]>query:
            max_i=mid_i -1
    return -1,-1

def binary_duplicates(keys,query):
    first_id,min_i=binary_search(keys, query)
    max_i=first_id
    #print("\n")
   # print(f"query is {query},first_id is {first_id},min_i is {min_i}")
  
    if first_id != -1:
        while min_i<max_i:
            mid_i=(max_i+min_i)//2
            if keys[mid_i]==query:
                max_i=mid_i
            elif keys[mid_i]<query:
                min_i=mid_i+1
            if keys[min_i]==query and keys[min_i-1]<query:
                return min_i
            if min_i ==0 and keys[min_i]==query:
                return min_i
    return first_id

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_duplicates(input_keys, q), end=' ')
