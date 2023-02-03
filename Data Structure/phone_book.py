# python3
'''
Task: In this task your goal is to implement a simple phone book manager. It should be able to process the
following types of user’s queries:
∙ add number name. It means that the user adds a person with name name and phone number
number to the phone book. If there exists a user with such number already, then your manager
has to overwrite the corresponding name.
∙ del number. It means that the manager should erase a person with number number from the phone
book. If there is no such person, then it should just ignore the query.
∙ find number. It means that the user looks for a person with phone number number. The manager
should reply with the appropriate name, or with string “not found" (without quotes) if there is
no such person in the book.

Input Format: There is a single integer 𝑁 in the first line — the number of queries. It’s followed by 𝑁
lines, each of them contains one query in the format described above.

Constraints: 1 ≤ 𝑁 ≤ 105. All phone numbers consist of decimal digits, they don’t have leading zeros, and
each of them has no more than 7 digits. All names are non-empty strings of latin letters, and each of
them has length at most 15. It’s guaranteed that there is no person with name “not found".

Output Format: Print the result of each find query — the name corresponding to the phone number or
“not found" (without quotes) if there is no person in the phone book with such phone number. Output
one result per line in the same order as the find queries are given in the input.
'''
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = dict()
    for cur_query in queries:
        # key number is found, write the value name
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        # if key is in dictionary, del the item
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        # get the value by key, set default value is 'not found'
        else:
            response = contacts.get(cur_query.number,'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

