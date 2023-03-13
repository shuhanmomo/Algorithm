# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

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
    
    
    
def fibonacci_partial_sum(from_, to): 
    result = last_digit_of_fibonacci_sum(to)-last_digit_of_fibonacci_sum(from_-1)
    return result%10
    
              
            
if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
