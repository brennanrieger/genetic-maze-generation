'''
Creates the activity GUI
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

''' make_radio
    Makes a radio button
    RETURNS: the value of the button
'''
def make_radio(parent, text1, text2):
    v = tk.IntVar()
    R1 = tk.Radiobutton(parent, text=text1, variable=v, value=1, command = check_radio).pack(anchor=tk.W)
    R2 = tk.Radiobutton(parent, text=text2, variable=v, value=2, command = check_radio).pack(anchor=tk.W)
    return v

''' enter
    Sets the return key to the check_all function
    RETURNS: no return
'''
def enter(event):
    check_all()

''' check_radio
    Checks to make sure radio button has been pressed
    RETURNS: true or false depending on input
'''
def check_radio():
    radio = act.get()
    if (radio == 1 or radio == 2):
        if radio == 1:
            check_radio.run_genetic = True
        else:
            check_radio.run_genetic = False
        return True
    else:
        print('Please pick an activity!')
        return False

''' check_val
    Checks to make sure numerical values are entered and ints within range
    RETURNS: true if done correctly
'''        
def check_val():
    # set default values
    rows_default = 20
    cols_default = 20

    # initialize entered to defaults
    rows_entered = rows_default
    cols_entered = cols_default

    # set "entered" to inputted value if given
    if rows.get() != "":
        rows_entered = (rows.get())
    if columns.get() != "":
        cols_entered = (columns.get())
        
    # print('Parameters Entered:',rows.get(),columns.get())
    if ((type (rows_entered) == int) or (rows_entered.isdigit())) and ((type (cols_entered) == int) or (cols_entered.isdigit())):
        if int (rows_entered) >= 4 and int (cols_entered) >=4:
            check_val.rows = int(rows_entered)
            check_val.cols = int(cols_entered)
            return True
        else:
            print('Wrong!: Rows and columns should be >= 4')
            return False
    else:
        print('Wrong!: Rows and columns should be positive integers')
        return False

''' check_all
    Makes sure radio values and text-fill values appropriate when user submits
    RETURNS: no return
'''
def check_all():
    if check_val() and check_radio():
        root.destroy()
        print('Parameters Accepted')
    
# set root and window sizes    
root = tk.Tk()
root.minsize(300,200)
#root.geometry("500x550")
root.title('BAAC Maze Generation')
                 
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
                 
#entries in window
mlabel= tk.Label(parent,text='Choose Activity:').pack()
act = make_radio(parent, "Genetic Algorithm", "Custom Maze")
rows = make_entry(parent, "\nNumber of Rows:", 16)
columns = make_entry(parent, "Number of Columns:", 16)

    
#button to enter
b = tk.Button(parent, borderwidth=5, text="Enter", width=10, pady=10, command=check_all)
b.pack(side=tk.BOTTOM)
rows.bind('<Return>', enter)
columns.focus_set()
parent.mainloop()

