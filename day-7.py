import re

def test_read_input():
    data = read_input('day-7-example-input.txt')
    assert next(data) == "light red bags contain 1 bright white bag, 2 muted yellow bags."

def test_bag_rules():
    bag_rules = bag_rules_from(read_input('day-7-example-input.txt'))
    assert bag_rules['light red'] == [(1, 'bright white'), (2, 'muted yellow')]
    assert bag_rules['dark orange'] == [(3, 'bright white'), (4, 'muted yellow')]
    assert bag_rules['bright white'] == [(1, 'shiny gold')]
    assert bag_rules['dotted black'] == []

def test_outer_bags_that_could_contain():
    bag_rules = bag_rules_from(read_input('day-7-example-input.txt'))
    assert outer_bags_that_could_contain(bag_rules, 'shiny gold') == {
        'bright white', 'muted yellow', 'dark orange', 'light red'
    }

def test_count_bags_inside():
    bag_rules = bag_rules_from(read_input('day-7-example-input.txt'))
    assert count_bags_inside(bag_rules, 'shiny gold') == 32

def test_count_bags_inside_another_example():
    bag_rules = bag_rules_from(read_input('day-7-another-example.txt'))
    assert count_bags_inside(bag_rules, 'shiny gold') == 126
    
#-----------------------------------------#

def read_input(filename):
    with open(filename, 'r') as f:
        for ln in f:
            yield ln.rstrip()

def bag_rules_from(data):
    bag_rules = {}
    for ln in data:
        parts = ln.split(' contain ')
        key = parts[0].replace(' bags','')
        values = []
        if parts[1] != 'no other bags.':
            for c in parts[1].split(', '):
                m = re.match(r'(\d+) (.*) bag', c)
                values.append((int(m[1]), m[2]))

        bag_rules[key] = values
    return bag_rules

def bag_could_contain(bag_rules, k, colour):
    if colour in (col for num, col in bag_rules[k]):
        return True
    else:
        return any(bag_could_contain(bag_rules, col, colour) for num, col in bag_rules[k])

def outer_bags_that_could_contain(bag_rules, colour):
    answer = []
    for k,v in bag_rules.items():
        if bag_could_contain(bag_rules, k, colour):
            answer.append(k)
    return set(answer)


def count_bags_inside(bag_rules, colour):
    return sum((num + (num * count_bags_inside(bag_rules, col))) for num, col in bag_rules[colour])


if __name__ == "__main__":
    bag_rules = bag_rules_from(read_input('day-7-input.txt'))
    print(count_bags_inside(bag_rules, 'shiny gold'))