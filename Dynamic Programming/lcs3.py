def lcs3(a, b, c):
    # Create a 3d matrix to store the result
    # initializing with None will cause error
    dp_m = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)]for _ in range(len(a)+1)]

    # fill the matrix iteratively
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
            # if find same item, go back diagonally
                if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    dp_m[i][j][k] = dp_m[i - 1][j - 1][k - 1] + 1
            # else check the three neighbors
                else:
                    dp_m[i][j][k] = max(dp_m[i - 1][j][k], dp_m[i][j - 1][k], dp_m[i][j][k-1])

    return dp_m[len(a)][len(b)][len(c)]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
