import sys
from maze import*

class MazeDisplay:

    ''' display
    Prints an ASCII maze
    RETURNS: nothing
    -maze: the maze object to be printed
    '''
    def display (self,maze):

        # Choose shape to represent a non-walkable square
        square = "X" #unicode(u"\u25A9") #big square diagonal crosshatch

        # Copy board from object maze
        lst = []
        for e in maze.board:
            lst.append(list(e))
        
        # Define START coordinates
        start_x = maze.start[0]
        start_y = maze.start[1]

        # Define END coordinates
        end_x = maze.end[0]
        end_y = maze.end[1]

        # Update board (change booleans to "start" and "end")
        lst[start_x][start_y] = "start"
        lst[end_x][end_y] = "end"

        # Set border to number of columns 
        border_length = 0
        for i in lst:
            border_length = len(i)

        # Create upper border
        sys.stdout.write("+")
        for i in range(border_length):
            sys.stdout.write("--")
        print "+\r"

        # Print board
        for i in lst:
            sys.stdout.write("|")
            for j in i:
                if j == False : sys.stdout.write(square + ' ')
                elif j == "start" : sys.stdout.write("s ")
                elif j == "end" : sys.stdout.write("e ")
                else : sys.stdout.write("  ")
            print "|" + " \r"

        # Create lower border
        sys.stdout.write("+")
        for i in range(border_length):
            sys.stdout.write("--")
        print "+\r"

display_object = MazeDisplay()

