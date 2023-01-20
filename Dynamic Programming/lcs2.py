# Longest Common Subsequence of Two Sequences Problem
# Compute the maximum length of a common
# subsequence of two sequences.

# Input: Two sequences.
# Output: The maximum length of
# a common subsequence.

def lcs2(a , b):
    # Create a 2d matrix to store the result
    dp_m = [[None]*(len(b)+1) for _ in range(len(a)+1)]

    # base case
    for i in range(len(a)+1):
        dp_m[i][0] = 0
    for j in range(len(b)+1):
        dp_m[0][j] = 0

    # fill the matrix iteratively
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            # if find same item, go back diagonally
            if a[i-1] == b[j-1]:
                dp_m[i][j] = dp_m[i-1][j-1] + 1
            # else check the two neighbors
            else:
                dp_m[i][j] = max(dp_m[i-1][j] , dp_m[i][j-1])

    return dp_m[len(a)][len(b)]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
