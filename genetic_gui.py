'''
Creates the genetic algorithm GUI
Used http://effbot.org/tkinterbook/entry.htm to figure out syntax
'''

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import string

''' make_entry
    Makes a text-fill box
    RETURNS: the entry
'''
def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

''' make_option
    Makes a drop down list
    RETURNS: the value of the drop-down
'''
def make_option(parent, OPTIONS,*values):
    variable = tk.StringVar(parent)
    variable.set(OPTIONS[0]) # default value
    w = apply(tk.OptionMenu, (parent,variable) + tuple(OPTIONS))
    w.pack()
    return variable

''' enter
    Sets the return key to the check_all function
    RETURNS: no return
'''        
def enter(event):
    check_all()

''' check_option
    Sets chosen solver to variable
    RETURNS: no return
'''    
def check_option():
    check_option.solver = solver_chosen.get()

''' not_empty
    Checks whether user left field blank
    RETURNS: true if not empty
'''
def not_empty(string):
    if type(string) == str:
        return len (string) > 0
    else:
        return False

''' is_Int
    Checks whether inputted string is an int
    RETURNS: boolean depending on number
'''
def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
    
''' within_range
    Checks whether inputted values are within range and of the correct type
    RETURNS: true if suitably entered
'''
def within_range(num):
    filled = filter(not_empty,num)
    if all((isInt(param)) for param in filled):
        size = int(num[0])
        fittest = int(num[1])
        random = int(num[2])
        elites = int(num[3])
        if (all((param >= 0) for param in filled)) and (size >= (random + elites)) and (elites <= fittest) and (size != 0) and (fittest != 0):
            return True
        else:
            return False
    else:
        return False
    
''' check_val
    Checks to make sure numerical values are entered and ints within range
    RETURNS: true if done correctly
'''         
def check_val():
    # set default values
    size_default = 10
    fittest_default = 5
    random_default = 2
    elites_default = 2

    # initialize entered to defaults
    size_entered = size_default
    fittest_entered = fittest_default
    random_entered = random_default
    elites_entered = elites_default

    # set "entered" to inputted value if given
    if size.get() != "":
        size_entered = (size.get())
    if fittest.get() != "":
        fittest_entered = (fittest.get())
    if random.get() != "":
        random_entered = (random.get())
    if elites.get() != "":
        elites_entered = (elites.get())
        
    print "Genetic Parameters Entered:\nsize = %s\nfittest = %s\nrandom = %s\nelites = %s"%(size.get(),fittest.get(),random.get(), elites.get())
    if within_range([size_entered, fittest_entered,random_entered, elites_entered]):
        check_val.size = int (size_entered)
        check_val.fittest = int(fittest_entered)
        check_val.random = int(random_entered)
        check_val.elites = int(elites_entered)
        return True                
    else:
        print('Wrong!: Genetic Parameters NOT Accepted. Check Rules!')
        return False

''' check_all
    Makes sure radio values and text-fill values appropriate when user submits
    RETURNS: no return
'''
def check_all():
    if check_val():
        check_option()
        root.destroy()
        print('Genetic Algorithm Parameters Accepted')

# set root and window sizes    
root = tk.Tk()
root.minsize(300,300)
#root.geometry("500x570")
root.title('Enter Genetic Algorithm Parameters')
                 
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
                 
#entries in window
mlabel= tk.Label(parent,text='Choose Solver:').pack()
solver_chosen = make_option(parent,["smart",
           "pythagorean",
           "inverse"],16)
mlabel= tk.Label(parent,text='\nEnter Algorithm Parameters:').pack()
size = make_entry(parent, "Population Size (default = 10)", 16)
fittest = make_entry(parent, "Number of Fittest (default = 5):", 16)
random = make_entry(parent, "Number of Additional Random Generators (default = 2):", 16)
elites = make_entry(parent, "Number of Elites: (default = 2)", 16)
mlabel= tk.Label(parent,text='\n SOME RULES: \n The population size must be greater than or equal to number of elites + number of random').pack()
mlabel = tk.Label(parent, text ='The number of elites must be less than or equal to the number of fittest').pack()
mlabel= tk.Label(parent, text = 'Population size and number of fittest must be ints greater than 0. \nThe number of elite and number of random must be ints greater than or equal to 0.').pack()

    
#button to enter
b = tk.Button(parent, borderwidth=5, text="Enter", width=10, pady=10, command=check_all)
b.pack(side=tk.BOTTOM)
size.bind('<Return>', enter)
fittest.focus_set()
parent.mainloop()
