def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

8

def lcm(a, b):
    if(a!=0 and b!=0):
        lcm=a*b/gcd(a,b)
    else:
        lcm=0
    return int(lcm)
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
    a, b = map(int, input().split())
    print(lcm(a, b))

