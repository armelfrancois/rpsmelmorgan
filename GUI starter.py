from tkinter import *
window = Tk()

canvasOne = Canvas(window, width = 550, height = 700)
canvasOne.pack()

firstRect = canvasOne.create_rectangle(225, 400, 325, 500, fill = "red")
secondRect = canvasOne.create_rectangle(75, 400, 175, 500, fill = "blue")
thirdRect = canvasOne.create_rectangle(375, 400, 475, 500, fill = "green")

def callBack(event):
    print("clicked at", event.x, event.y)
    if 225 < event.x < 325 and 450 < event.y < 550:
        firstRect = canvasOne.create_rectangle(225, 400, 325, 500, fill = "orange")
        
canvasOne.bind("<Button-1>", callBack)
canvasOne.bind("<>", callback)
canvasOne.pack()
       

window.geometry("550x700")
window.mainloop()
