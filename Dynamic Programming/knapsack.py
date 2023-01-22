# Maximum Amount of Gold Problem
#   Given a set of gold bars of various weights and
#   a backpack that can hold at most W pounds,
#   place as much gold as possible into the backpack.

# Input: A set of n gold bars
#   of integer weights w1, . . . ,wn and
#   a backpack that can hold at most
#   W pounds.
# Output: A subset of gold bars
#   of maximum total weight not exceeding W

# use recursive algorithm since not all subproblems need to be solved
# create a dictionary to store calculated results
T=dict()
def maximum_gold(capacity, weights,i):
    if (capacity,i) not in T:
        #base case
        if i == 0:
            T[capacity,i] = 0
        else:
            # if not take the next item
            T[capacity,i] = maximum_gold(capacity, weights,i-1)
            if capacity >= weights[i-1]:
                # compare results of taking next item or not
                T[capacity,i] = max(T[capacity,i],maximum_gold(capacity-weights[i-1], weights, i-1)+weights[i-1])
   
    return T[capacity,i]


if __name__ == '__main__':
    input_capacity = int(input())
    input_weights = list(map(int,input().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights,i=len(input_weights)))
