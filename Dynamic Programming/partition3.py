# 3-Partition Problem
#   Partition a set of integers into three subsets with
#   equal sums.

# Input : The first line contains an integer n. The second line contains
#         integers v1,v2, . . . ,vn separated by spaces.
# Output: Output 1, if it possible to partition v1,v2, . . . ,vn into three
#          subsets with equal sums, and 0 otherwise

def partition3(values):
    # test if the sum can be equally divided into 3 parts
    if sum(values)%3 != 0:
        return 0
    else:
        target = sum(values)//3
        # create a 3d matrix to store the result
        dp_m = [[[-float("inf")]*(target+1) for _ in range(target+1)]for _ in range(len(values)+1)]
        # base case  
        for j in range(target+1):
            for k in range(target+1):
                dp_m[0][j][k]=0
        
        for i in range(len(values)+1):
           dp_m[i][0][0]=1

        
        #fill the matrix iteratively
        for i in range(1,len(values)+1):
            for j in range(target+1):
                for k in range(target+1):
                    
                    # larger than target, not taken, skip the case
                    if values[i-1]>j and values[i-1]>k:
                        dp_m[i][j][k]=dp_m[i-1][j][k]
                    # otherwise, compare not taken, put in partition1, or put in partition2
                    else:
                        dp_m[i][j][k] = max(dp_m[i-1][j][k],dp_m[i-1][j-values[i-1]][k],dp_m[i-1][j][k-values[i-1]])
                        
    return dp_m[len(values)][target][target]
        


if __name__ == '__main__':
    input_values = list(map(int,input().split()))
    print(partition3(input_values))
