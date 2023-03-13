# python3


def fibonacci_number_naive(n):
    # print("Compute F sub", n)
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    fibonacci_arr=[]
    for i in range(n+1):
        if i<=1:
            fibonacci_arr.append(i)
        else:
            fibonacci_sum = fibonacci_arr[i-1]+fibonacci_arr[i-2]
            fibonacci_arr.append(fibonacci_sum)
    return fibonacci_arr[-1]



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
