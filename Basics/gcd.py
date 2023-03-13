# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False

def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    a_1=max(a,b)
    b_1=min(a,b)
    a=a_1
    b=b_1
    gcd=0
    if b==0:
        gcd=0
    else:
        while(b!=0):
            a_new=b
            b= a % b
            a= a_new
        gcd=a
    return gcd

if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
