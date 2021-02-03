#!/usr/bin/python

"""
Princess Peach is trapped in one of the four corners of a square grid. 
You are in the center of the grid and can move one step at a time in any of the four directions. 
Can you rescue the princess?
"""
"""
Print out the moves you will take to rescue the princess in one go. 
The moves must be separated by '\n', a newline. 
The valid moves are LEFT or RIGHT or UP or DOWN.
"""

def displayPathtoPrincess(n, grid):
    for j, row in enumerate(grid):
        if 'p' in [char for char in row]:
            peach_row = j
            for i, char in enumerate([char for char in grid[j]]):
                if char == 'p':
                    peach_col = i
    

    center = n // 2
    if peach_row > center and peach_col > center:
        # peach @ Bottom Right
        for move in range(center):
            print('DOWN')
            print('RIGHT')
    if peach_row > center and peach_col < center:
        # peach @ Bottom Left
        for move in range(center):
            print('DOWN')
            print('LEFT')
    if peach_row < center and peach_col > center:
        # peach @ Top Right
        for move in range(center):
            print('UP')
            print('RIGHT')
    if peach_row < center and peach_col < center:
        # peach @ Top Left
        for move in range(center):
            print('UP')
            print('LEFT')


        



if __name__ == '__main__':
    
    m = int(input('Size of Grid: '))
    grid = [] 
    for i in range(0, m): 
        grid.append(input('Grid: ').strip())

    displayPathtoPrincess(m,grid)


