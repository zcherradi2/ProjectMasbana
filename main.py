import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application")
root.geometry("500x300")
# create label widgets


frame1 = tk.Frame(root, height=200,width=200, bg='red')
frame2 = tk.Frame(root, height=200, width=200,bg='green')

label1 = tk.Label(frame2, text="Enter your name:")
label2 = tk.Label(frame2, text="Enter your age:")

btnServices = tk.Button(frame1)
btnServices.grid(row=0,column=0)
#btnServices.grid()
# create entry widgets
entry1 = tk.Entry(frame2)
entry2 = tk.Entry(frame2)

# set layout using grid geometry manager
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

#frame1.grid(row=0, column=0, sticky='nsew')
#frame2.grid(row=1, column=0, sticky='nsew')
frame1.pack(fill="x")
frame2.pack(fill="x")


# start the main event loop
root.mainloop()
