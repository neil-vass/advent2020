
def test_FB_ranges():
    assert range_for(0, 127, 'F') == (0, 63)
    assert range_for(0, 63, 'B') == (32, 63)
    assert range_for(32, 63, 'F') == (32, 47)
    assert range_for(32, 47, 'B') == (40, 47)   

def test_find_seat_for():
    assert find_seat_for('FBFBBFFRLR') == (44, 5)
    assert find_seat_for('BFFFBBFRRR') == (70, 7)
    assert find_seat_for('FFFBBBFRRR') == (14, 7)
    assert find_seat_for('BBFFBBFRLL') == (102, 4)


def test_get_seat_id():
    assert get_seat_id('FBFBBFFRLR') == 357
    assert get_seat_id('BFFFBBFRRR') == 567
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820

def test_whats_happening():
    assert get_seat_id('BBBBFFBLRL') == 970

#----------------------------------------––#


def range_for(min, max, chr):
    midpoint = min + ((max - min) // 2)
    if chr in ('F','L'):
        return min, midpoint
    else:
        return midpoint+1, max

def find_seat_for(code):
    row_min, row_max = 0, 127
    for c in code[:7]:
        row_min, row_max = range_for(row_min, row_max, c)  
    
    col_min, col_max = 0, 7
    for c in code[7:]:
        col_min, col_max = range_for(col_min, col_max, c)
    return row_min, col_min

def get_seat_id(code):
    row, col = find_seat_for(code.rstrip())
    return (row * 8) + col


if __name__ == "__main__":
    with open('day-5-input.txt', 'r') as f:
        seat_ids = [get_seat_id(code) for code in f]
        seat_ids.sort()
        one_before = next((idx, seat) for idx, seat in enumerate(seat_ids) 
                            if seat_ids[idx+1] == seat+2)
        print(one_before)
        print(seat_ids[516:525])
