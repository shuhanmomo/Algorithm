'''
Majority Element Problem
Check whether a given sequence of numbers contains
an element that appears more than half of
the times.

Input: A sequence of n integers.

Output: 1, if there is an element
that is repeated more than n/2
times, and 0 otherwise.
'''


def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1
    return 0

#need to clarify the start and end for later recursive calls
def majority_element(elements,s,e):
    #if array contain just one element, return it
    if s==e:
        return elements[s]
    #define the mid point
    m=(s+e)//2
    #divide the array into two halves and make recursive calls 
    left=majority_element(elements,s,m)
    right=majority_element(elements,m+1,e)
    #start comparison
    #1. two half return the same
    if (left==right):
        return left
    #2. two half return differently, calculate the counts
    elif count_maj(left,elements,s,m)>count_maj(right,elements,m+1,e):
        return left
    else:
        return right
        
# function to calculate occurence 
def count_maj(i,elements,s,e):
    count = 0
    for item in elements[s:e+1]:
        if i== item:
            count +=1
    return count
# function to go thru array once again to check the major element occurence
def majority_check(elements,s,e):
    num=majority_element(elements,s,e)
    count=count_maj(num,elements,s,e)
    if count>len(elements)/2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_check(input_elements,0,input_n-1))
  
        
