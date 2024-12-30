from tkinter import *

def createNewWidget(frame):
    button = Button(frame, text="test")
    button.pack()

def createPrefField(frame):
    for i in range(3):
        textbox = Entry(frame, width= 10)
        textbox.grid(row = 0, column = i, padx = 1, pady = 10)

root = Tk()

# frame = Frame(root)
# frame.pack()

# button = Button(frame, text="test", command=lambda: createPrefField(root))
# button.pack()

createPrefField(root)

root.mainloop()