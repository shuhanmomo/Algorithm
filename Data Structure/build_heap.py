# python3
# Convert array into heap by using O(n) swaps
# use a min-heap

# Input Format: The first line of the input contains single integer 𝑛. The next line contains 𝑛 space-separated
# integers 𝑎𝑖.

# Output Format:The first line of the output should contain single integer 𝑚 — the total number of swaps.
# 𝑚 must satisfy conditions 0 ≤ 𝑚 ≤ 4𝑛. The next 𝑚 lines should contain the swap operations used
# to convert the array 𝑎 into a heap. Each swap is described by a pair of integers 𝑖, 𝑗 — the 0-based
# indices of the elements to be swapped. After applying all the swaps in the specified order the array
# must become a heap, that is, for each 𝑖 where 0 ≤ 𝑖 ≤ 𝑛 − 1 the following conditions must be true:
# 1. If 2𝑖 + 1 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+1.
# 2. If 2𝑖 + 2 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+2.
# Note that all the elements of the input array are distinct. Note that any sequence of swaps that has
# length at most 4𝑛 and after which your initial array becomes a correct heap will be graded as correct.

class Heap:
    
    def __init__(self,data):
        self.data = data
        self.size = len(data)
        self.swaps = []
    # zero-based arrays need to note the index of two children is different from 1-based
    #compute left child index of given ith element
    def left_child(self,i):
        return 2*i+1
    #compute right child index of given ith element
    def right_child(self,i):
        return 2*i+2
    
    # swap the two elements in heap array and store the swap in another array
    def swap(self,i,min_i):
        H = self.data
        self.swaps.append((i,min_i))
        H[i], H[min_i] = H[min_i], H[i]
        return
    
    # compare the ith element with its two child , if larger, sift down
    def sift_down(self,i):
        min_i = i
        l = self.left_child(i)
        H = self.data       
        r = self.right_child(i)
        if r < self.size and H[r] < H[min_i]:
            min_i = r
        if l < self.size and H[l] < H[min_i]:
            min_i = l
        if i != min_i:
            self.swap(i, min_i)
            self.sift_down(min_i)
    
    def build_heap(self):
        n = self.size
        for i in range(n//2,-1,-1):
            self.sift_down(i)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    heap = Heap(data)
    heap.build_heap()
    swaps = heap.swaps   
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
