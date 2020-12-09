from __future__ import annotations

def test_Program_init():
    p = Program(read_input('day-8-example-input.txt'))
    assert p.accumulator == 0
    assert p.position == 0
    assert len(p.instructions) == 9
    assert p.instructions[0] == ('nop', 0)
    assert len(p.instructions_called) == 9 

def test_Program_step():
    p = Program(read_input('day-8-example-input.txt'))
    
    # execute nop
    p.step()
    assert p.accumulator == 0
    assert p.position == 1

    # execute acc
    p.step()
    assert p.accumulator == 1
    assert p.position == 2

    # execute jmp
    p.step()
    assert p.accumulator == 1
    assert p.position == 6

def test_run_without_correction_hits_infinite_loop():
    p = Program(read_input('day-8-example-input.txt'))
    termination = p.run()
    assert termination == 'infinite loop'
    assert p.accumulator == 5

def test_run_with_manual_correction_terminates():
    p = Program(read_input('day-8-example-input.txt'))
    p.instructions[7] = ('nop', -4)
    termination = p.run()
    assert termination == 'normal'
    assert p.accumulator == 8

def test_run_with_autocorrect_terminates():
    accumulator = run_with_autocorrect('day-8-example-input.txt')
    assert accumulator == 8


#---------------------------------------------#

def read_input(filename):
    with open(filename) as f:
        for ln in f:
            yield ln.rstrip()

class Program:

    def __init__(self, input):
        self.accumulator = 0
        self.position = 0
        self.instructions = []
        for ln in input:
            op, arg = ln.split(' ')
            self.instructions.append((op, int(arg)))
        
        self.instructions_called = [0] * len(self.instructions)

    def step(self):
        self.instructions_called[self.position] += 1
        op, arg = self.instructions[self.position]

        if op == 'acc':
            self.accumulator += arg
            self.position += 1
        elif op == 'jmp':
            self.position += arg
        elif op == 'nop':
            self.position += 1
        else:
            raise ValueError('Unrecognized operation in program')

        if 0 > self.position >= len(self.instructions):
            raise ValueError('Been sent out of bounds of instructions')

    def run(self):
        while True: 
            self.step()
            if self.position == len(self.instructions):
                return 'normal'
            if self.instructions_called[self.position] > 0:
                return 'infinite loop'



def run_with_autocorrect(filename):
    p = Program(read_input(filename))

    for i in range(len(p.instructions)):
        op, arg = p.instructions[i]

        if op in ('nop', 'jmp'):
            replacement = 'nop' if op == 'jmp' else 'jmp'
            p.instructions[i] = (replacement, arg)
            if p.run() == 'normal':
                return p.accumulator
            p = Program(read_input(filename))


if __name__ == "__main__":
    print(run_with_autocorrect('day-8-input.txt'))