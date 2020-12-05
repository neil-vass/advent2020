import re

required_fields_and_rules = {
    'byr': lambda val: is_4_digits_in_range(1920, 2002, val), 
    'iyr': lambda val: is_4_digits_in_range(2010, 2020, val), 
    'eyr': lambda val: is_4_digits_in_range(2020, 2030, val), 
    'hgt': lambda val: meets_height_field_rules(val),  
    'hcl': lambda val: re.fullmatch(r'#[0-9|a-f]{6}', val) is not None, 
    'ecl': lambda val: re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', val) is not None, 
    'pid': lambda val: re.fullmatch(r'\d{9}', val) is not None,
}

optional_fields_and_rules = {
    'cid': lambda val: True
}

def test_get_data():
    data = get_data('day-4-example-input.txt')
    assert next(data) == "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"
    assert next(data) == "byr:1937 iyr:2017 cid:147 hgt:183cm"

def test_get_next_passport():
    data = get_data('day-4-example-input.txt')
    assert get_next_passport(data) == {
        'ecl':'gry', 'pid':'860033327', 'eyr':'2020', 'hcl':'#fffffd',
        'byr':'1937', 'iyr':'2017', 'cid':'147', 'hgt':'183cm'
    }

def test_get_all_passports():
    data = get_data('day-4-example-input.txt')
    passport_count = 0
    p = get_next_passport(data)
    while p:
        passport_count += 1
        p = get_next_passport(data)
    assert passport_count == 4

def test_passport_with_all_fields_is_valid():
    data = get_data('day-4-example-input.txt')
    first_passport = get_next_passport(data)
    assert is_valid(first_passport)

def test_passport_with_missing_required_field_is_not_valid():
    data = get_data('day-4-example-input.txt')
    get_next_passport(data)
    second_passport = get_next_passport(data)
    assert not is_valid(second_passport)

def test_passport_with_missing_optional_field_is_valid():
    data = get_data('day-4-example-input.txt')
    for _ in range(2): get_next_passport(data)
    third_passport = get_next_passport(data)
    assert is_valid(third_passport)

def test_passport_with_missing_optional_field_and_missing_required_field_is_not_valid():
    data = get_data('day-4-example-input.txt')
    for _ in range(3): get_next_passport(data)
    fourth_passport = get_next_passport(data)
    assert not is_valid(fourth_passport)

def test_field_value_matches_rule_byr():
    assert field_value_matches_rule('byr', '2002')
    assert not field_value_matches_rule('byr', '2003')

def test_field_value_matches_rule_hcl():    
    assert field_value_matches_rule('hcl', '#123abc')
    assert not field_value_matches_rule('hcl', '#123abz')
    assert not field_value_matches_rule('hcl', '123abc')

def test_field_value_matches_rule_ecl():    
    assert field_value_matches_rule('ecl', 'brn')
    assert not field_value_matches_rule('ecl', 'wat')

def test_field_value_matches_rule_pid():    
    assert field_value_matches_rule('pid', '000000001')
    assert not field_value_matches_rule('pid', '0123456789')

def test_count_valid_passports():
    data = get_data('day-4-example-input.txt')
    assert count_valid_passports(data) == 2


def test_is_4_digits_in_range():
    assert is_4_digits_in_range(1000, 2000, '1500')
    assert not is_4_digits_in_range(1000, 2000, '3000')
    assert not is_4_digits_in_range(1000, 2000, '1500.5')

def test_meets_height_field_rules():
    assert meets_height_field_rules('60in')
    assert meets_height_field_rules('190cm')
    assert not meets_height_field_rules('190in')
    assert not meets_height_field_rules('190')

def test_invalid_examples():
    data = get_data('day-4-example-invalid.txt')
    assert count_valid_passports(data) == 0

def test_valid_examples():
    data = get_data('day-4-example-valid.txt')
    assert count_valid_passports(data) == 4

#-------------------------------------------------------#


def is_4_digits_in_range(lowest, highest, str_to_check):
    if not re.fullmatch(r'\d{4}', str_to_check): return False
    return lowest <= int(str_to_check) <= highest

def meets_height_field_rules(str_to_check):
    m = re.fullmatch(r'(\d+)(cm|in)', str_to_check)
    if not m:
        return False
    elif m[2] == 'cm':
        return 150 <= int(m[1]) <= 193
    else:
        return 59 <= int(m[1]) <= 76


def get_data(filename):
    with open(filename, 'r') as f:
        for ln in f:
            yield ln.rstrip()

def get_next_passport(data):
    passport = {}
    try:
        ln = next(data)
        while len(ln):
            for pair in ln.split(' '):
                key, val = pair.split(':')
                passport[key] = val
            ln = next(data)
    except StopIteration:
        pass
    return passport

def correct_fields_are_present(passport):
    passport_fields = set(passport.keys())
    required_fields = set(required_fields_and_rules.keys())
    optional_fields = set(optional_fields_and_rules.keys())
    return (passport_fields.issuperset(required_fields) and 
        (passport_fields - required_fields).issubset(optional_fields))


def field_value_matches_rule(key, value):
    rule = (required_fields_and_rules | optional_fields_and_rules)[key]
    return rule(value)

def fields_follow_rules(passport):
    for key, value in passport.items():
        if not field_value_matches_rule(key, value):
            return False
    return True

def is_valid(passport):
    return correct_fields_are_present(passport) and fields_follow_rules(passport)
    
def count_valid_passports(data):
    valid_passports_count = 0
    passport = get_next_passport(data)
    while passport:
        if is_valid(passport): valid_passports_count += 1
        passport = get_next_passport(data)
    return valid_passports_count

if __name__ == "__main__":
    data = get_data('day-4-input.txt')
    print(count_valid_passports(data))
    
