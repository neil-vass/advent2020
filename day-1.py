import itertools

def test_happy_paths_find_pair():
    assert find_combination_that_sums_to([1,2,3], 2, 4) == (1,3)
    assert find_combination_that_sums_to([100, 150, 90, 110], 2, 240) == (150, 90)

def test_fetch_data_gives_list():
    li = fetch_data()
    assert li[0] == 1801
    assert len(li) == 200


def find_combination_that_sums_to(li, no_of_elements, target):
    combos = itertools.combinations(li, no_of_elements)
    return next(c for c in combos if sum(c) == target)

def fetch_data():
    with open('day-1-input.txt', 'r') as f:
        li = [int(x) for x in f]
    return li


if __name__ == "__main__":
    x, y, z = find_combination_that_sums_to(fetch_data(), 3, 2020)
    print(x * y * z)
