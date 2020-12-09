import itertools, collections

def test_one_number_past_preamble():
    # says it's random. What are the odds?
    preamble = range(1, 26)
    assert is_valid(preamble, 26)
    assert is_valid(preamble, 49)
    assert not is_valid(preamble, 100)
    assert not is_valid(preamble, 50)

def test_two_numbers_past_preamble():
    preamble = [20] + list(range(1,20)) + list(range(21, 26))
    assert first_invalid_number(25, preamble + [45, 26]) == None
    assert first_invalid_number(25, preamble + [45, 65]) == 65
    assert first_invalid_number(25, preamble + [45, 64]) == None
    assert first_invalid_number(25, preamble + [45, 66]) == None

def test_longer_example():
    data = read_input('day-9-example-input.txt')
    assert first_invalid_number(5, data) == 127

def test_find_set_that_sums():
    data = read_input('day-9-example-input.txt')
    assert find_set_that_sums(127, data) == [15, 25, 47, 40]

def test_find_weakness():
    data = read_input('day-9-example-input.txt')
    assert find_weakness(5, data) == 62

#------------------------------------------#

def read_input(filename):
    with open(filename) as f:
        for ln in f:
            yield int(ln.rstrip())

def is_valid(preamble, num):
    try:
        x,y = next((x, y) for x, y in itertools.combinations(preamble, 2) if x + y == num)
        return True
    except StopIteration:
        return False

def first_invalid_number(preamble_size, data):
    preamble = collections.deque([], preamble_size)
    for num in data:
        if len(preamble) == preamble_size:
            if not is_valid(preamble, num):
                return num
        preamble.append(num)
    return None
        
def find_set_that_sums(target, data):
    datalist = list(data)
    for i in range(len(datalist)):
        sum = datalist[i]
        j = i+1
        while sum < target and j < len(datalist):
            sum += datalist[j]
            j += 1
            if sum == target:
                return datalist[i:j]
            if sum > target:
                continue
    raise ValueError('No set sums to target!')

def find_weakness(preamble_size, data):
    datalist = list(data)
    target = first_invalid_number(preamble_size, datalist)
    set_that_sums = find_set_that_sums(target, datalist)
    return min(set_that_sums) + max(set_that_sums)

if __name__ == "__main__":
    data = read_input('day-9-input.txt')
    print(find_weakness(25, data))