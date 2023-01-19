# Money Change Again Problem
# Compute the minimum number of coins needed
# to change the given value into coins with denominations
# 1, 3, and 4.

# Input: An integer money
# Output: The minimum number
# of coins with denominations 1, 3,
# and 4 that changes money.


def change(money):
    # create a 2d matrix to store results
    coin = [1, 3, 4]
    dp_m = [[-float("inf")]*(money+1) for _ in range(len(coin))]
    # base case, fill the column[0] and row[0]
    for i in range(len(coin)):
        dp_m[i][0] = 0
    for j in range(0,money+1):
        dp_m[0][j]= j
    # fill the matrix iteratively
    for i in range(1,len(coin)):
        for j in range(1, money+1):
            if j < coin[i]:
                dp_m[i][j] = dp_m[i-1][j]
            else:
                dp_m[i][j] = min(dp_m[i-1][j], 1+dp_m[i][j-coin[i]])

    times = dp_m[len(coin)-1][money]
    return times


if __name__ == '__main__':
    m = int(input())
    print(change(m))
