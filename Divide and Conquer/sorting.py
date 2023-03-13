'''
Speeding-up RandomizedQuickSort Problem
Sort a given sequence of numbers (that
may contain duplicates) using a modification
of RandomizedQuickSort that works in
O(nlogn) expected time.

Input: An integer array with
n elements that may contain
duplicates.

Output: Sorted array (generated
using a modification
of RandomizedQuickSort) that
works in O(nlogn) expected
time.
'''

from random import randint
def partition3(array, left, right):
    pivot=array[left]
    m1=left
    m2=left
    larger=right
    # keep increasing m2 until it meets bounds
    while m2<=larger:
        if array[m2]<pivot:
            array[m1],array[m2]=array[m2],array[m1]
            m1+=1
            m2+=1
        elif array[m2]>pivot:
            array[m2],array[larger]=array[larger],array[m2]
            larger-=1
        else:
            m2+=1
    return m1,m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    #random number between left and right
    k = randint(left, right)
    #swap left and k to make inner partition3 function code easy
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    #make recursive call till left>=right
    randomized_quick_sort(array, left, m1-1 )
    randomized_quick_sort(array, m2, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
