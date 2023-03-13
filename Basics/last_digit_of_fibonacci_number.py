# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    fibonacci_arr = []
    for i in range(61):
        if i <= 1:
            fibonacci_arr.append(i)
        else:
            fibonacci_sum = fibonacci_arr[i - 1] + fibonacci_arr[i - 2]
            sum_str=repr(fibonacci_sum)
            last_digit_sum = int(sum_str[-1])
            fibonacci_arr.append(last_digit_sum)
    n_i = n%60
    last_digit=fibonacci_arr[n_i]
    return last_digit


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
