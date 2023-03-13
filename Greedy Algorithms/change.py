'''
Money Change Problem
Compute the minimum number of coins needed
to change the given value into coins with denominations
1, 5, and 10.
Input: An integer money.
Output: The minimum number
of coins with denominations 1, 5,
and 10 that changes money.
'''

def change(money):
    money=money//10+(money%10)//5+money%5

    return money


if __name__ == '__main__':
    m = int(input())
    print(change(m))
