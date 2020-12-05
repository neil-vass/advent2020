

example_pattern = [
"..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"
]

def test_init():
    state = init(iter(example_pattern), 3, 1)
    assert state['current_row'] == "..##......."
    assert state['current_pos'] == 0
    assert state['right_step'] == 3
    assert state['down_step'] == 1
    assert next(state['remaining_pattern']) == "#...#...#.."

def test_we_can_advance_through_map():
    state = init(iter(example_pattern), 3, 1)
    state = traverse(state)
    assert state['current_row'] == "#...#...#.."
    assert state['current_pos'] == 3
    assert state['right_step'] == 3
    assert state['down_step'] == 1
    assert next(state['remaining_pattern']) == ".#....#..#."

def test_we_can_advance_through_map_2_steps():
    state = init(iter(example_pattern), 3, 1)
    state = traverse(state)
    state = traverse(state)
    assert state['current_row'] == ".#....#..#."
    assert state['current_pos'] == 6
    assert next(state['remaining_pattern']) == "..#.#...#.#"

def test_first_step_is_not_tree():
    state = init(iter(example_pattern), 3, 1)
    state = traverse(state)
    assert not is_tree(state) 

def test_second_step_is_tree():
    state = init(iter(example_pattern), 3, 1)
    state = traverse(state)
    state = traverse(state)
    assert is_tree(state) 

def test_is_tree_extends_pattern():
    state = init(iter(example_pattern), 3, 1)
    state['current_pos'] = 13
    assert is_tree(state)
    state['current_pos'] = 20
    assert not is_tree(state)

def test_5_steps_extends_pattern_and_is_tree():
    state = init(iter(example_pattern), 3, 1)
    for _ in range(5):
        state = traverse(state)
    assert state['current_row'] == "..#.##....."
    assert state['current_pos'] == 15
    assert is_tree(state)

def test_count_trees():
    state = init(iter(example_pattern), 3, 1)
    assert count_trees(state) == 7

def init(pattern, right_step, down_step):
    return {
        'current_row': next(pattern),
        'current_pos': 0,
        'right_step': right_step,
        'down_step': down_step,
        'remaining_pattern': pattern
    }

def traverse(state):
    new_pos = state['current_pos'] + state['right_step']
    for _ in range(state['down_step']): 
        new_row = next(state['remaining_pattern'], None)

    return {
        'current_row': new_row,
        'current_pos': new_pos,
        'right_step': state['right_step'],
        'down_step': state['down_step'],
        'remaining_pattern': state['remaining_pattern']
    }

def is_tree(state):
    row = state['current_row'].rstrip()
    pos = state['current_pos']
    return row[pos % len(row)] == '#'

def count_trees(state):
    trees = 0
    state = traverse(state)
    while state['current_row']:
        if is_tree(state): trees +=1
        state = traverse(state)
    return trees

def file_runthrough(right, down):
    with open('day-3-input.txt', 'r') as f:
        state = init(f, right, down)
        return(count_trees(state))


if __name__ == "__main__":
    print (
        file_runthrough(1, 1) *
        file_runthrough(3, 1) *
        file_runthrough(5, 1) *
        file_runthrough(7, 1) *
        file_runthrough(1, 2)
    )
    
