
import turtle as t
START_STATE = (5, 3)
GOAL_STATE = (2, 2)

def create_grid(n):
    rtn = []
    if (n <= 0): print ("invalid input")
    else:
        for i in range (n):
            row = []
            for j in range (n):
                row.append(" ")
            rtn.append(row)
    return rtn

def generate_grid():
    grid = create_grid(8)

    def add_stone(grid, r, c):
        grid[r][c] = "*"
        return grid

    stone_pos = [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (5, 2), (5, 6)]
    for stone_position in stone_pos:
        r, c = stone_position
        grid = add_stone(grid, r, c)

    grid [5][3] = 'S'
    grid [2][2] = 'G'
    return grid

def state_to_pos(state):
    r, c = state
    return (c + 1)  * 50 - 4 * 50, 4 * 50 - (r + 1)  * 50
def state_to_grid(state):
    r, c = state
    return (c + 1)  * 50 - 4 * 50 - 25, 4 * 50 - (r + 1)  * 50 + 25

def draw_grid():
    START_STATE = (5, 3)
    GOAL_STATE = (2, 2)

    t.reset()
    t.shape("arrow")
    t.speed('fastest')
    t.forward(200)
    t.setposition(200, 200)
    t.setposition(-200, 200)
    t.setposition(-200, -200)
    t.setposition(200, -200)

    for i in range (8):
        t.setposition(200, 200 - i * 50)
        t.setposition(-200, 200 - i * 50)
        t.setposition(-200, 200 - (i + 1) * 50)

    for i in range (8):
        t.setposition(-200 + i * 50, -200)
        t.setposition(-200 + i * 50, 200)
        t.setposition(- 200 + (i + 1) * 50, 200)

    t.up()

    x, y = state_to_pos((3, 5))
    t.setposition(x, y)
    t.up()

    stone_pos = [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (5, 2), (5, 6)]
    for stone in stone_pos:
        t.pencolor("brown")
        x, y = state_to_pos(stone)
        t.setposition(x, y)
        t.down()
        t.setposition(x - 50, y + 50)
        t.up()

    x,y = state_to_pos(GOAL_STATE)
    t.setposition(x - 20, y + 20)
    t.pencolor(0.2, 0.8, 0.55)
    t.down()
    t.setposition(x - 25, y + 20)
    t.setposition(x - 25, y + 25)
    t.setposition(x - 20, y + 25)
    t.setposition(x - 20, y + 20)
    t.up()

    x, y = state_to_pos(START_STATE)
    t.setposition(x - 25, y + 25)


def draw_path(path):
    t.shape("turtle")
    t.down()
    t.pencolor("red")
    t.down()
    t.speed(1)
    counter = 0
    for state in path:
        counter += 1
        x, y = state_to_grid(state)
        t.setposition(x, y)
        t.write(str(counter), move=True)
        
def draw_visited(path):
    t.shape("turtle")
    t.up()
    t.up()
    t.pencolor("red")
    t.up()
    t.speed(1)
    counter = 0
    for state in path:
        counter += 1
        x, y = state_to_grid(state)
        t.setposition(x, y)
        t.write(str(counter), move=True)