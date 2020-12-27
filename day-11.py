

def test_get_plan():
    plan = get_plan('day-11-example-input.txt')
    assert plan[0][0] == 'L'
    assert plan[0][1] == '.'
    assert plan[2][4] == 'L'

def test_get_adjacents():
    plan = get_plan('day-11-example-input.txt')
    assert get_adjacents(plan, 0, 0) == ['.', 'L', 'L']
    assert get_adjacents(plan, 2, 4) == ['L', 'L', 'L', '.', '.', 'L', '.', 'L' ]
    assert get_adjacents(plan, 9, 9) == ['.', 'L', 'L']

def test_new_state_for_pos():
    plan = get_plan('day-11-example-input.txt')
    assert new_state_for_pos(plan, 0, 0) == '#'
    assert new_state_for_pos(plan, 0, 1) == '.'
    assert new_state_for_pos(plan, 2, 4) == '#'

def test_step_change():
    plan = get_plan('day-11-example-input.txt')
    updated = step_change(plan)
    assert updated == [
        '#.##.##.##',
        '#######.##',
        '#.#.#..#..',
        '####.##.##',
        '#.##.##.##',
        '#.#####.##',
        '..#.#.....',
        '##########',
        '#.######.#',
        '#.#####.##'
    ]
    
    updated = step_change(updated)
    assert updated == [
        '#.LL.L#.##',
        '#LLLLLL.L#',
        'L.L.L..L..',
        '#LLL.LL.L#',
        '#.LL.LL.LL',
        '#.LLLL#.##',
        '..L.L.....',
        '#LLLLLLLL#',
        '#.LLLLLL.L',
        '#.#LLLL.##'
    ]
    
def test_change_until_stable():
    plan = get_plan('day-11-example-input.txt')
    assert change_until_stable(plan) == [
        '#.#L.L#.##',
        '#LLL#LL.L#',
        'L.#.L..#..',
        '#L##.##.L#',
        '#.#L.LL.LL',
        '#.#L#L#.##',
        '..L.L.....',
        '#L#L##L#L#',
        '#.LLLLLL.L',
        '#.#L#L#.##'
    ]

def test_count_occupied_seats():
    plan = get_plan('day-11-example-input.txt')
    assert count_occupied_seats(plan) == 0
    filled = change_until_stable(plan)
    assert count_occupied_seats(filled) == 37

        
#=======================================================#

def get_plan(filename):
    plan = []
    with open(filename) as f:
        for ln in f:
            plan.append(ln.strip())
    return plan

def get_adjacents(plan, row, col):
    adj = []
    look_left = col if col == 0 else col-1
    look_right = col if col == len(plan[0])-1 else col+1

    if row > 0:
        adj += plan[row-1][look_left:look_right+1]
    if look_left != col:
        adj += plan[row][look_left]
    if look_right != col:
        adj += plan[row][look_right]
    if row < len(plan)-1:
        adj += plan[row+1][look_left:look_right+1]
    return adj


def new_state_for_pos(plan, row, col):
    current = plan[row][col]
    if current == '.': 
        return '.'

    adj = get_adjacents(plan, row, col)
    if current == 'L' and adj.count('#') == 0:
        return '#'
    elif current == '#' and adj.count('#') >= 4:
        return 'L'
    else:
        return current

def step_change(plan):
    updated = []
    for row in range(len(plan)):
        new_row = ''
        for col in range(len(plan[0])):
            new_row += new_state_for_pos(plan, row, col)
        updated.append(new_row)
    return updated

def change_until_stable(plan):
    last_ver = plan
    new_ver = step_change(plan)
    while new_ver != last_ver:
        last_ver = new_ver
        new_ver = step_change(new_ver)
    return new_ver

def count_occupied_seats(plan):
    return sum(row.count('#') for row in plan)


if __name__ == "__main__":
    plan = get_plan('day-11-input.txt')
    settled = change_until_stable(plan)
    print(count_occupied_seats(settled))