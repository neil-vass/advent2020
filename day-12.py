
from dataclasses import dataclass

def test_ship():
    ship = Ship()
    assert ship.xpos == 0
    ship.xpos += 10
    assert ship.status() == (10, 0, 10, 1)

def test_move_ship():
    ship = Ship()
    ship.execute('F10')
    assert ship.status() == (100, 10, 10, 1)
    ship.execute('N3')
    assert ship.status() == (100, 10, 10, 4)
    ship.execute('F7')
    assert ship.status() == (170, 38, 10, 4)
    ship.execute('R90')
    assert ship.status() == (170, 38, 4, -10)
    ship.execute('F11')
    assert ship.status() == (214, -72, 4, -10)

def test_follow_instructions_from_file():
    ship = Ship()
    for instuction in get_instructions('day-12-example-input.txt'):
        ship.execute(instuction)
    assert ship.status() == (214, -72, 4, -10)
    assert ship.manhattan_distance() == 286
    
#===========================================#

@dataclass
class Ship:
    xpos: int = 0
    ypos: int = 0 
    waypoint_xpos: int = 10
    waypoint_ypos: int = 1

    compass_points = 'NESW'

    def status(self):
        return (self.xpos, self.ypos, self.waypoint_xpos, self.waypoint_ypos)
    
    def manhattan_distance(self):
        return abs(self.xpos) + abs(self.ypos)

    def move_ship_to_waypoint(self, num_times):
        self.xpos += (self.waypoint_xpos * num_times)
        self.ypos += (self.waypoint_ypos * num_times)

    def move_waypoint(self, direction, distance):
        if direction == 'N':
            self.waypoint_ypos += distance
        elif direction == 'E':
            self.waypoint_xpos += distance
        elif direction == 'S':
            self.waypoint_ypos -= distance
        elif direction == 'W':
            self.waypoint_xpos -= distance

    def rotate_waypoint(self, turn_direction, degrees):
        if turn_direction == 'L':
            degrees = -degrees
        steps = (degrees // 90) % len(Ship.compass_points)
        for _ in range(steps):
            self.rotate_waypoint_right_90()
        
    def rotate_waypoint_right_90(self):
        self.waypoint_xpos, self.waypoint_ypos = self.waypoint_ypos, -self.waypoint_xpos


    def execute(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        
        if action in Ship.compass_points:
            self.move_waypoint(action, value)
        elif action in 'LR':
            self.rotate_waypoint(action, value)
        elif action == 'F':
            self.move_ship_to_waypoint(value)
        

def get_instructions(filename):
    with open(filename) as f:
        for ln in f:
            yield ln.rstrip()

if __name__ == "__main__":
    ship = Ship()
    for instuction in get_instructions('day-12-input.txt'):
        ship.execute(instuction)
    print(ship.manhattan_distance())