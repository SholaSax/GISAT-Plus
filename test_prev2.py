# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")


# Create a function to clear the combobox
def clear_cb():
    cb.set('')


# Define Days Tuple
days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')


# Function to print the index of selected option in Combobox
def callback(*arg):
    Label(win, text="The value at index " + str(cb.current()) + " is" + " " + str(var.get()),
          font=('Helvetica 12')).pack()


# Create a combobox widget
var = StringVar()
cb = ttk.Combobox(win, textvariable=var)
cb['values'] = days
cb['state'] = 'readonly'
cb.pack(fill='x', padx=5, pady=5)

# Set the tracing for the given variable
var.trace('w', callback)

# Create a button to clear the selected combobox text value
button = Button(win, text="Clear", command=clear_cb)
button.pack()

win.mainloop()