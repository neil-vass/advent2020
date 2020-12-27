import itertools

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


def test_can_jump():
    assert can_jump(0, 2)
    assert not can_jump(0, 4)
    assert not can_jump(10, 22)


def test_count_different_arrangements_single_adaptor():
    assert count_different_arrangements(outlet=0, adaptors=[4]) == 0
    assert count_different_arrangements(outlet=0, adaptors=[2]) == 1


def test_count_different_arrangements():
    adaptors = [1,2,3]
    assert count_different_arrangements(0, adaptors) == 4
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

def can_jump(left, right):
    return 1 <= (right - left) <= 3

def find_arrangements(outlet_to_device):
    return find_arrangements_by_lookup_table(outlet_to_device)

def find_arrangements_by_lookup_table(outlet_to_device):
    diffs = [j-i for i, j in zip(outlet_to_device[:-1], outlet_to_device[1:])]
    arrangements = 1
    for k, g in itertools.groupby(diffs):
        if k == 1:
            count_of_ones = len(list(g))
            possible_combinations = {
                1: 1,
                2: 2,
                3: 4,
                4: 7,
                5: 13,
                6: 22,
            }[count_of_ones]
            arrangements *= possible_combinations
    return arrangements
    

def count_different_arrangements(outlet, adaptors):
    adaptors = list(adaptors)
    adaptors.sort()
    device = max_for_device(adaptors)
    
    flatter = [outlet, *adaptors, device]

    for i in range(len(flatter) -1):
        if not can_jump(flatter[i], flatter[i+1]):
            return 0

    return find_arrangements(flatter)

if __name__ == "__main__":
    # I have _no idea_ how to solve part 2, this code borrows a lot from:
    # https://dev.to/rpalo/advent-of-code-2020-solution-megathread-day-10-adapter-array-33ea
    # I can count combinations on my fingers and that matches the switch table, 
    # no clue on how to make a general rule for it.
    adaptors = read_input('day-10-input.txt')
    print(count_different_arrangements(0, adaptors))