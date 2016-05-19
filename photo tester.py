from tkinter import *
window = Tk()

photo=PhotoImage(file="background.gif")
w = Label(window, image=photo)
w.photo = photo
w.pack()

window.mainloop()
