from tkinter import *

class Window:
    def __init__(self, height, width):
        self.root = Tk()
        self.height = height
        self.width = width
        self.root.title = "Sorting Algorithm Visualizer"
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="light grey")
        self.canvas.create_rectangle((100, 75), (1100, 300), fill="green")

        self.r1 = Radiobutton(self.root, text="Option A", value="A")
        self.r2 = Radiobutton(self.root, text="Option B", value="B")
        self.r3 = Radiobutton(self.root, text="Option C", value="C")
        self.r4 = Radiobutton(self.root, text="Option D", value="D")

        self.r1.place(x=250, y=124)
        self.r2.place(x=250, y=149)
        self.r3.place(x=250, y=174)
        self.r4.place(x=250, y=224)

        self.canvas.pack()
        self.root.mainloop()
        