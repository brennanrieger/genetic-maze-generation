from generation import *
from display import *
from htmldisp import *
import sys

# DEBUGGING IS OFF
debug_on = False

''' debug_print
Helper function. Prints the text if debugging or if ignoring is enabled.
'''
def debug_print(txt,ignore_debug) :
    if (debug_on or ignore_debug):
        print txt

''' genetic_alg
Runs the genetic algorithm with the given parameters. Outputs the optimal generator's parameters
    and mazes.
pop_size: The number of generators in a given generation.
num_fittest: The number of generators that will be used for the breeding of the next generation.
num_elites: The number of the fittest generators to keep in the next generation.
'''
def genetic_alg(pop_size, num_fittest, num_random, num_elites) :
    # Create a new generation
    current_gen = Generation(pop_size,num_fittest,num_random,num_elites)
    current_gen.spawn_random_generation()

    # Set the definition of "no more progress"
    negligible = 0.0

    best_fitness = None
    just_started = True

    # Actual loop
    gen_num = 0
    bad_gen_count = 0
    # Terminate after 3 successive negligible generations.
    bad_gen_termination = 3
    best_generator = None

    while(True) :
        gen_num = gen_num + 1
        debug_print("\nGENERATION #"+str(gen_num)+" COMPLETE",True)
        
        # run this generation and get its fitness
        new_fitness = current_gen.run()
        if just_started :
            best_fitness = new_fitness
        
        # Print some information about this generation for debugging
        debug_print("BEST FROM THIS GENERATION:", False)
        debug_print(new_fitness, False)
        debug_print("CURENT BEST:", False)
        debug_print(best_fitness, False)
        if (best_generator != None) :
            debug_print(best_generator.parameter_list, False)
        debug_print("DIFFERENCE FROM BEST GENERATOR:", False)
        debug_print(new_fitness-best_fitness, False)

        # If the change is non-negligible, record the fittest generator in the generation as the best.
        if (new_fitness - best_fitness > negligible) :
            bad_gen_count = 0
            best_generator = current_gen.fittest[0]
            best_fitness = new_fitness
        # Otherwise, say this is a bad generation and keep trying
        elif not just_started :
            bad_gen_count = bad_gen_count + 1
            debug_print("NO PROGRESS GENERATION # "+str(bad_gen_count)+" / "+str(bad_gen_termination)+"\n", True)
            if (bad_gen_count == bad_gen_termination) :
                break
        else :
            just_started = False
            # Make sure not to let best_generator = None if best generator appears first by chance
            best_generator = current_gen.fittest[0]
        # Spawn the next generation from the previous generation (even if it was bad!)
        current_gen = current_gen.spawn_next_generation()

    
    # Print info about the optimal generator
    # This is specfic to our project, which uses 7 parameters.
    annotations = ["Start Location Row","Start Location Column","Jump Probability","Forward Probability","Birds-Eye Probability","Return Distance Ratio","End Time Ratio"]
    
    debug_print("\n\nBEST GENERATOR: ", True)
    for i in range(0, 7) :
        debug_print(annotations[i] + ": " + str(best_generator.parameter_list[i]), True)
    debug_print("\nAVG RUNTIME: " + str(best_generator.avg_runtime), True)

    # Display mazes
    debug_print("\nALL MAZES:", True)
    display_obj = MazeDisplay()
    htmldisplay_obj = HTMLDisplay()
    num_of_mazes = len(best_generator.mazes)
    for m in range(0, num_of_mazes) :
        if m == num_of_mazes - 1 :
            debug_print("\nVERY BEST MAZE:\n", True)
        display_obj.display(best_generator.mazes[m])
        
    htmldisplay_obj.display(best_generator.mazes[num_of_mazes - 1])