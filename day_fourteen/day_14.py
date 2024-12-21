from pathlib import Path
from utils.file import readin_files


class Robot:
    pos: tuple[int, int]
    vel: tuple[int, int]
    maxrange: tuple[int, int]
    mid_x: int
    mid_y: int

    def __init__(self, start, vel, max_range):
        self.pos = start
        self.vel = vel
        self.maxrange = max_range
        self.mid_y = int(self.maxrange[1] / 2)
        self.mid_x = int(self.maxrange[0] / 2)

    def move(self):
        newX = (self.pos[0] + self.vel[0])
        newY = (self.pos[1] + self.vel[1])
        self.pos = (newX, newY)

    def teleport(self):
        newX = self.pos[0]
        newY = self.pos[1]
        if self.pos[0] >= self.maxrange[0]:
            newX -= self.maxrange[0]
        if self.pos[0] < 0:
            newX += self.maxrange[0]
        if self.pos[1] >= self.maxrange[1]:
            newY -= self.maxrange[1]
        if self.pos[1] < 0:
            newY += self.maxrange[1]
        self.pos = (newX, newY)

    def getQuadrant(self) -> int:
        if self.pos[0] < self.mid_x:
            if self.pos[1] < self.mid_y:
                return 1
            elif self.pos[1] > self.mid_y:
                return 3
        elif self.pos[0] > self.mid_x:
            if self.pos[1] < self.mid_y:
                return 2
            elif self.pos[1] > self.mid_y:
                return 4
        return 0


def printMap(ListOfRobots):
    fullMap = [['.' for _ in range(ListOfRobots[0].maxrange[0])] for _ in
               range(ListOfRobots[0].maxrange[1])]
    for robot in ListOfRobots:
        if (fullMap[robot.pos[1]][robot.pos[0]]) == '.':
            fullMap[robot.pos[1]][robot.pos[0]] = 1
        else:
            fullMap[robot.pos[1]][robot.pos[0]] += 1
    print('')
    print('#'.join(['' for _ in range(ListOfRobots[0].maxrange[0])]))
    for line in fullMap:
        for char in line:
            print(char, end='')
        print('')
    print('#'.join(['' for _ in range(ListOfRobots[0].maxrange[0])]))
    print('')


def part_one(input_file: str, input_path: Path, tile_sizes: tuple[int, int] = (101, 103)) -> int:
    file_content = readin_files(input_file, input_path)
    list_of_robots: list[Robot] = []
    for line in file_content:
        pos, vel = line.strip().split(' ')
        _, pos = pos.split('=')
        _, vel = vel.split('=')
        posX, posY = pos.split(',')
        velX, velY = vel.split(',')
        list_of_robots.append(Robot((int(posX), int(posY)), (int(velX), int(velY)), tile_sizes))

    # printMap(list_of_robots)
    for counter in range(100):
        [x.move() for x in list_of_robots]
        [x.teleport() for x in list_of_robots]

    # printMap(list_of_robots)
    robotsMap: dict = {x: 0 for x in range(5)}
    for robot in list_of_robots:
        robotsMap[robot.getQuadrant()] += 1

    result = 1
    for key, value in robotsMap.items():
        if key == 0:
            continue
        result *= value
    return result


def part_two(input_file, input_path: Path = Path.cwd()) -> int:
    file_content = readin_files(input_file, input_path)

    return 0


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    print(part_one('input.txt', my_input_path))
    print(part_two('input.txt', my_input_path))
