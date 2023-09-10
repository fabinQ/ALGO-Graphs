def find_exit(maze):
    rows = len(maze)
    if rows == 0:
        return False
    columns = len(maze[0])
    #top
    for col in range(columns):
        if maze[0][col] == ' ':
            return True
    #bottom
    for col in range(columns):
        if maze[rows - 1][col] == ' ':
            return True
    #left side
    for row in range(rows):
        if maze[row][0] == ' ':
            return True
    #right side
    for row in range(rows):
        if maze[row][columns - 1] == ' ':
            return True
    return False

def has_exit(maze):
    if len(maze) == 1:
        return True

    '''Ogarnij funkcje map i lambda'''
    maze = list(map(lambda x: list(x), maze))
    
    
    def find_starting_point(maze):
        start = []
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == 'k':
                    start.append((row, col))
                    return start

    if find_exit(maze) == False:
        return False

    def dfs(x, y):
        if x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[0]) - 1:
            return True

        maze[x][y] = 'X'
        moves = [(0, 1),
                 (0, -1),
                 (1, 0),
                 (-1, 0)]
        for dx, dy in moves:
            newx, newy = x+dx, y+dy
            if (
                0 <= newx < len(maze) and
                0 <= newy < len(maze[0]) and
                maze[newx][newy] == ' '
            ):
                if dfs(newx, newy):
                    return True
        return False

    start = find_starting_point(maze)
    if len(start) == 1:
        x, y = start[0]
        return dfs(x, y)
    else:
        raise ValueError('There should no be multiple Kates')


maze =[
'### #',
'#  # #',
'#k  #',
'#####']

print(has_exit(maze))
