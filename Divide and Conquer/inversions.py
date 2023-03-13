'''
Number of Inversions Problem
Compute the number of inversions in a sequence
of integers.

Input: A sequence of n integers
a1, . . . ,an.

Output: The number of inversions
in the sequence, i.e., the
number of indices i < j such that
ai > aj .
'''

from itertools import combinations
def inversions(a):
    #use merge sort as solution
    n=len(a)
    #base case
    if n==1:
        return a,0
    m=n//2
    # divide into halves, make recursive call
    left,l= inversions(a[:m])
    right,r= inversions(a[m:])
    invert_count=l+r
    a_new,num=merge(left,right)
    invert_count+=num
    
    return a_new,invert_count

def merge(b,c):
    d=[]
    i=0
    j=0
    invert_count=0
    while i<len(b) and j<len(c):
        if b[i] <=c[j]:
            d.append(b[i])
            i+=1
        else:
            d.append(c[j])
            j+=1
            #all after i is larger than c[j]
            invert_count+=len(b)-i
    # i or j may be smaller than len -1   
    d+=b[i:]
    d+=c[j:]
    
    return d,invert_count
    

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    arr,inver =inversions(elements)
    print(inver)
