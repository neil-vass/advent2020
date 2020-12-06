
def test_first_group():
    data = [
        'abcx',
        'abcy',
        'abcz'
    ]
    assert group_answer(data) == set('abc')

def test_example_five_answers():
    with open('day-6-example-five.txt', 'r') as f:
        assert multi_group_answers(f) == [
            {'a', 'b', 'c'},
            set(),
            {'a'},
            {'a'},
            {'b'}
        ]

def test_example_five_sum():
    with open('day-6-example-five.txt', 'r') as f:
        assert sum_of_counts(f) == 6


#===============================================≠#

def group_answer(data):
    answer = None
    for ln in data:
        if answer is None:
            answer = set(ln.rstrip())
        else:
            answer = answer & set(ln.rstrip())
    return answer

def multi_group_answers(data):
    answers = []
    next_group = []
    for ln in data:
        if ln.rstrip():
            next_group.append(ln)
        else:
            answers.append(group_answer(next_group))
            next_group = []
    # If the last group didn't have a blank line after it (likely)
    if next_group:
        answers.append(group_answer(next_group))
    return answers

def sum_of_counts(data):
    return sum(len(s) for s in multi_group_answers(data))

if __name__ == "__main__":
    with open('day-6-input.txt', 'r') as f:
        print(sum_of_counts(f))