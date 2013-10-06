import sys
from generator import *
from maze import *

''' display
    Implements HTML display as a class
'''

class HTMLDisplay:
    def display (self, maze):
        
        # open an HTML file to show output in a browser
        HTMLFILE = 'Maze_output.html'
        f = open(HTMLFILE, 'w')

        #board from ob
        list =  maze.board
        n_rows = maze_num_rows
        n_cols = maze_num_cols
                

        # Define START coordinates
        start_x = maze.start[0]
        start_y = maze.start[1]

        # Define END coordinates
        end_x = maze.end[0]
        end_y = maze.end[1]

        result = "<TABLE ID='TMaze' CELLSPACING=0 CELLPADDING=0> \n"

        # set border
        for i in range (n_rows):
            result += "<TR HEIGHT = 30>"

            for j in range (n_cols):
                result += "<TD WIDTH=30 align=center style='"
                if i==0:
                    result += "BORDER-TOP: 3px black solid;"
                if i==n_rows-1:
                    result += "BORDER-BOTTOM: 3px black solid;"
                if j==0:
                    result += "BORDER-LEFT: 3px black solid;"
                if j==n_cols-1:
                    result += "BORDER-RIGHT: 3px black solid;"
                

                if (list[i][j]==False):
                    result += "BACKGROUND-COLOR:#99CCFF;"

                if i == start_x and j == start_y:
                    result += "BACKGROUND-COLOR:#336633;"
                if i == end_x and j == end_y:
                    result += "BACKGROUND-COLOR:#990000;"
                result += "'>"
                    

                # set start and end
                if i == start_x and j == start_y:
                    result += "<font color='FFFFFF' FACE='SANS-SERIF' size=4pt ><b>S</b></font>"
                if i == end_x and j == end_y:
                    result += "<font color='FFFFFF' FACE='SANS-SERIF' size=4pt><b>E</b></font>"

                    

                else:
                    result += "&nbsp;"
                result += "</TD>\n"

            result += "</TR>\n"
                    
        result += "</TABLE>\n"


        #return result
        f.write(result)

display_object = HTMLDisplay()

        
   
