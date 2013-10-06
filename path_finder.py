import math
from maze import *
from settings import *
from display import *
from sys import exit

class PathFinder:
    
    ''' path_finder_solve
    Finds the direct path from start to end in a maze that contains no loops. If display_maze_solution is True, then it will also display
    this path. It updates the runtime of the maze based on a heuristic called on this solver.
    RETURNS: No return value.
    -m: a maze with start and end in different locations and a path between them. Maze must have no loops
    '''
    def path_finder_solve(self,m):
        
        # local board to hold and edit a copy of m.board
        maze = []
        for row in m.board:
            maze.append(list(row))
        
        # enumeration
        North = 0
        East = 1
        South  = 2
        West = 3
        
        ''' move
        Gives coordinates of moving from square in direction dir. Cannot be called from a square on the border.
        RETURNS: No return value.
        -square : the square being moved from
        -dir : the direction in which to move
        '''
        def move(square,dir):
            if (dir == North):
                return(square[0]+1,square[1])
            elif dir == South:
                return(square[0]-1,square[1])
            elif dir == East:
                return(square[0],square[1]+1)
            elif dir == West:
                return(square[0],square[1]-1)
            else:
                print "error: moved not passed a valid direction"
                exit()
            return
        
        ''' check_square
        Checks whether a square is a dead end. A square is consider a dead end if it is surrounded on three sides by 
        walls (False squares).
        RETURNS: True if it is a dead end, False otherwise
        -row: row of square to be checked
        -column: column of square to be checked
        '''
        def check_square(row,column):
            if maze[row][column] == False:
                return False
            if (row,column) == m.start or (row,column) == m.end:
                return False
            true_neighbors = 0
            for dir in [North,East,South,West]:
                neighbor = move((row,column),dir)
                if maze[neighbor[0]][neighbor[1]]:
                    true_neighbors = true_neighbors + 1
            if true_neighbors == 1:
                return True
            elif true_neighbors == 0:
                print "error, square is isolated"
            else:
                return False
        
        ''' display
        Creates a maze consisting of the squares in Maze. Then calls display_object.display to display this maze.
        RETURNS: No return value.
        '''
        def display():
            maze_for_display = Maze()
            maze_for_display.board = maze
            maze_for_display.start = m.start
            maze_for_display.end = m.end
            display_object.display(maze_for_display)
            return
        
        ''' evaluate_path
        Applies heuristic to path from start to end. Heuristic goes through path and increments runtime for each step.
        Heuristic gives higher weight to movements along path that lead away from end and that are far away from end.
        RETURNS: No return value.
        '''
        def evaluate_path():
            runtime = 0
            coordinates = m.start
            while(coordinates != m.end):
                for dir in [North,East,South,West]:
                    neighbor = move(coordinates,dir)
                    if maze[neighbor[0]][neighbor[1]]:
                        current_dist = math.sqrt((coordinates[0] - m.start[0])**2 + (coordinates[1] - m.start[1])**2)
                        neighbor_dist = math.sqrt((neighbor[0] - m.start[0])**2 + (neighbor[1] - m.start[1])**2)
                        runtime += (neighbor_dist - current_dist + 1) * neighbor_dist
                        maze[coordinates[0]][coordinates[1]] = False
                        coordinates = neighbor
            m.runtime += runtime
            
        
        while(True):
            deletions = 0
            for row in range(0,maze_num_rows):
                for column in range(0,maze_num_cols):
                    if check_square(row,column):
                        maze[row][column] = False
                        deletions = deletions + 1
            if deletions == 0:
                break
        if display_maze_solution:
            display()
        evaluate_path()
                    

pf = PathFinder()


                    