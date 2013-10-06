# Make global variables in scope
display_maze_generation_in_real_time = None
display_maze_solution = None
run_genetic_algorithm = None
maze_num_rows = None
maze_num_cols = None
maze_solver = None

from sys import platform
from os import system

def run_system_command(pc, maclinux) :
    if platform == 'win32' :
        system(pc)
    else :
        system(maclinux)

import activity_gui
run_genetic_algorithm = activity_gui.check_radio.run_genetic
maze_num_rows = activity_gui.check_val.rows
maze_num_cols = activity_gui.check_val.cols


if run_genetic_algorithm:
    import genetic_gui
    display_maze_generation_in_real_time = False
    display_maze_solution = False
    # solver options: "inverse", "pythagorean", "smart", or "display"
    maze_solver = genetic_gui.check_option.solver
    num_mazes = 10
    display_all_outputted_mazes = False
    display_maze_solution = False

else:
    import custom_gui
    display_maze_generation_in_real_time = custom_gui.check_box.disp_steps
    display_maze_solution = custom_gui.check_box.disp_sol
    num_mazes = 1
    display_all_outputted_mazes = True
    maze_solver = "display"



