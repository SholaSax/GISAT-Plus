from tkinter import *

root =Tk()
root.title('GISAT Plus')
#root.iconbitmap()
root.geometry("800x900")

#Define image
bg = PhotoImage(file="images/GISAT_plus.png")

#Creat a label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)



root.mainloop()