import re

example_lines = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

def test_line_to_dict():
    assert line_to_dict(example_lines[0]) == {
        'first_pos': 1,
        'second_pos': 3,
        'given_char': 'a',
        'password': "abcde"
    }

def test_line_to_dict_with_2_digit_numbers():
    assert line_to_dict("14-15 j: jjjjjjjjjjjjjlcj") == {
        'first_pos': 14,
        'second_pos': 15,
        'given_char': 'j',
        'password': "jjjjjjjjjjjjjlcj"
    }

def test_first_example_line_is_valid():
    assert is_valid(example_lines[0])

def test_second_example_line_is_not_valid():
    assert not is_valid(example_lines[1])

def test_third_example_line_is_not_valid():
    assert not is_valid(example_lines[2])

def test_is_given_char():
    assert is_given_char('abcde', 1, 'a')

def test_count_valid_example_lines():
    assert count_valid_lines(example_lines) == 1

def line_to_dict(line):
    m = re.match(r'^(\d+)-(\d+) (.): (.*)$', line)
    return {
        'first_pos': int(m[1]),
        'second_pos': int(m[2]),
        'given_char': m[3],
        'password': m[4]
    }

def is_given_char(password, pos, given_char):
    return password[pos-1] == given_char

def is_valid(line):
    d = line_to_dict(line)
    return is_given_char(d['password'], d['first_pos'], d['given_char']) ^ \
            is_given_char(d['password'], d['second_pos'], d['given_char'])

def count_valid_lines(lines):
    return sum(is_valid(line) for line in lines)

if __name__ == "__main__":
    with open('day-2-input.txt', 'r') as f:
        print(count_valid_lines(f))
