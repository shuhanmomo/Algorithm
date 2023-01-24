
# Input Format:Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
#              marks and brackets from the set []{}().

# Output Format: If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
#                output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
#                brackets, output the 1-based index of the first unmatched opening bracket.

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_id = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(next)
            opening_id.append(i)

        if next in ")]}":
            # Process closing bracket
            if opening_brackets_stack == []:
                return i+1
            top = opening_brackets_stack.pop()
            opening_id.pop()
            if not are_matching(top, next):
                return i+1
    
    if opening_brackets_stack == []:   
        return 'Success'
    else:
        return opening_id[-1]+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
