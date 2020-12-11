def test_max_for_device():
    adaptors = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    assert max_for_device(adaptors) == 22

def test_choose_next_adaptor():
    outlet = 0
    adaptors = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    adaptors.sort()

    chosen, diff, remaining_adaptors = choose_next_adaptor(outlet, adaptors)
    assert diff == 1

    chosen, diff, remaining_adaptors = choose_next_adaptor(chosen, remaining_adaptors)
    assert diff == 3


def test_count_differences():
    outlet = 0
    adaptors = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    assert count_differences(outlet, adaptors) == { 1: 7, 3: 5 }

def test_larger_example():
    adaptors = read_input('day-10-example-input.txt')
    assert count_differences(0, adaptors) == { 1: 22, 3: 10 }


def test_count_different_arrangements():
    adaptors = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    assert count_different_arrangements(0, adaptors) == 8
#-----------------------------------------------------------#

def read_input(filename):
    with open(filename) as f:
        for ln in f:
            yield int(ln.rstrip())

def max_for_device(adaptors):
    return max(adaptors) + 3

def choose_next_adaptor(rating, adaptors):
    return adaptors[0], (adaptors[0] - rating), adaptors[1:]

def count_differences(outlet, adaptors):
    differences = {}
    adaptors = list(adaptors)
    adaptors.sort()
    adaptors.append(max_for_device(adaptors))
    chosen = outlet
    while adaptors:
        chosen, diff, adaptors = choose_next_adaptor(chosen, adaptors)
        differences[diff] = differences.get(diff, 0) + 1
    return differences

def count_different_arrangements(outlet, adaptors):
    arrangements = 0
    adaptors = list(adaptors)
    adaptors.sort()
    

if __name__ == "__main__":
    adaptors = read_input('day-10-input.txt')
    d = count_differences(0, adaptors)
    print(d)
    print(d[1] * d[3])