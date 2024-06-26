from tkinter import Tk, BOTH, Canvas, Button
from algorithms import Algorithms
import random
import time

class Window:
    def __init__(self, height, width):
        self.root = Tk()
        self.height = height
        self.width = width
        self.root.title("Sorting Algorithm Visualizer")
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="light grey")
        self.rectangles = []
        self.running = False
        # self.canvas.create_rectangle((100, 75), (1100, 300), fill="light gray")
        # self.canvas.create_rectangle((100, 325), (1100, 800), fill="light gray")

        # self.r1 = Radiobutton(self.root, text="Bubble Sort", value="A")
        # self.r2 = Radiobutton(self.root, text="Insertion Sort", value="B")
        # self.r3 = Radiobutton(self.root, text="Selection Sort", value="C")
        # self.r4 = Radiobutton(self.root, text="Merge Sort", value="D")
        # self.r5 = Radiobutton(self.root, text="Heap Sort", value="E")
        # self.r6 = Radiobutton(self.root, text="Radix Sort", value="F")
        # self.r7 = Radiobutton(self.root, text="Quick Sort", value="G")

        # self.r1.place(x=250, y=99)
        # self.r2.place(x=250, y=124)
        # self.r3.place(x=250, y=149)
        # self.r4.place(x=250, y=174)
        # self.r5.place(x=250, y=199)
        # self.r6.place(x=250, y=224)
        # self.r7.place(x=250, y=249)

        self._create_rectangle(15)


    
        self.canvas.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.bubble_sort_visualize()
        # self.root.mainloop()

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            # time.sleep(0.05)
    def close(self):
        self.running = False
    
    def visualize(self):
        for i, rect in enumerate(self.rectangles):
            rect.move(100+i * 40, rect.y1)
        self.canvas.update()
        time.sleep(0.1)

    def bubble_sort_visualize(self):
        def key(rect):
            return rect.height
        sorting = Algorithms(self.rectangles)
        sorting.bubbleSort(key=key, visualize=self.visualize)
                
    def _create_rectangle(self, num_rectangles):
        for i in range(num_rectangles):
            x1, y1 = 400 + i * 40, random.randint(450, 700)
            x2, y2 = x1 + 20, 800
            color = "red"
            height = y2 - y1
            rect = Rectangle(self.canvas, x1, y1, x2, y2, color, height)
            self.rectangles.append(rect)

class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2, color, height):
        self.canvas = canvas
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.color = color
        self.height = height

    def move(self, x1, y1):
        x2 = x1 + (self.x2 - self.x1)
        y2 = y1 + (self.y2 - self.y1)
        self.canvas.coords(self.id, x1, y1, x2, y2)
    
    def change_color(self, color):
        self.canvas.itemconfig(self.id, fill=color)

    def get_coords(self):
        return self.canvas.coords(self.id)