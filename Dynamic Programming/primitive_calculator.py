# Primitive Calculator Problem
# Find the minimum number of operations needed
# to get a positive integer n from 1 by using only
# three operations: add 1, multiply by 2, and multiply
# by 3.

# Input: An integer n.
# Output: The minimum number
# of operations “+1”, “×2”, and “×3”
# needed to get n from 1.

def compute_operations(n):
    # create an array to store results
    dp_arr = [0] * (n+1)
    seq_id =[0] * (n+1)

    # fill the array iteratively and store the predecessor
    for i in range(2, n+1):
        # for normal case, number should increase by 1
        dp_arr[i] = dp_arr[i-1]+1
        seq_id[i] = i-1

        # if number can be divided by 2 or 3
        # need to compare it with normal case
        if i % 2 == 0:
            if dp_arr[i // 2] + 1 < dp_arr[i]:
                dp_arr[i] = 1 + dp_arr[i // 2]
                seq_id[i] = i // 2
        if i % 3 == 0:
            if dp_arr[i // 3] + 1 < dp_arr[i]:
                dp_arr[i] = 1 + dp_arr[i // 3]
                seq_id[i] = i // 3

    # reconstruct solution by following back the predecessor array
    num=n
    seq=[None]*(dp_arr[n]+1)
    seq[-1]=n
    for i in range(dp_arr[n]-1,-1,-1):
        num=seq_id[num]
        seq[i]=num
    return seq


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
