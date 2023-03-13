def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def last_digit_of_fibonacci_sum(n):
    fibonacci_arr = []
    fibonacci_last_arr = []
    for i in range(61):
        if i <= 1:
            fibonacci_arr.append(i)
            fibonacci_last_arr.append(i)
        else:
            fibonacci_i = fibonacci_arr[i - 1] + fibonacci_arr[i - 2]
            fibonacci_arr.append(fibonacci_i)
            fibonacci_sum = sum(fibonacci_arr)
            fibonacci_last_arr.append(fibonacci_sum%10)
            
            
            
    n_i = n%60
    last_digit=fibonacci_last_arr[n_i]
    return last_digit

if __name__ == '__main__':
    n = int(input())
    print(last_digit_of_fibonacci_sum(n))
