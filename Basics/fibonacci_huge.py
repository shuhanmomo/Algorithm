def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_number(n):
    fibonacci_arr=[]
    for i in range(n+1):
        if i<=1:
            fibonacci_arr.append(i)
        else:
            fibonacci_sum = fibonacci_arr[i-1]+fibonacci_arr[i-2]
            fibonacci_arr.append(fibonacci_sum)
    return fibonacci_arr[-1]

def fibonacci_huge(n,m):
  
    num =1
    a = 0
    b = 1
    c = a + b
    for i in range(m*m) :
        c = (a + b) % m
        a = b
        b = c
        if (a == 0 and b == 1):
            num=i+1
            break
               
    fibonacci_modulo = []
    for j in range(num):
        modulo= fibonacci_number(j)% m
        fibonacci_modulo.append(modulo)
    modulo_i = n%num
    return fibonacci_modulo[modulo_i]

if __name__ == '__main__':
    n, m = map(int, input().split())
   # print(fibonacci_huge_naive(n, m))
    print(fibonacci_huge(n, m))
