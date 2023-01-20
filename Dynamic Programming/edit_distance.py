# Edit Distance Problem
# Compute the edit distance between two strings

# Input: Two strings
# Output: The minimum number
# of single-symbol insertions, deletions,
# and substitutions to transform
# one string into the other one.

def edit_distance(a, b):
    # create a 2d matrix
    dp_m = [[float("inf")]*(len(b)+1) for _ in range(len(a)+1)]
    # base case
    for i in range(len(a)+1):
        dp_m[i][0] = i
    for j in range(len(b)+1):
        dp_m[0][j] = j
    # start to iteratively fill the matrix
    # 4 conditions: deletion +1, insertion +1, mismatch +1, match +0
    for i in range(1,len(a)+1):
        for j in range(1,len(b) + 1):
            # operations when previous letter is match or not
            diff = 0 if a[i-1] == b[j-1] else 1
            # evaluate the minimum operations depending on previous letter condition
            dp_m[i][j] = min(dp_m[i-1][j]+1, dp_m[i][j-1]+1, dp_m[i-1][j-1]+diff)

    return dp_m[len(a)][len(b)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
