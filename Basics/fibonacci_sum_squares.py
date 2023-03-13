def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def last_digit_of_fibonacci_number(n):

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

def fibonacci_sum_squares_eff(n):
    result = last_digit_of_fibonacci_number(n)*last_digit_of_fibonacci_number(n+1)
    return result%10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_eff(n))
