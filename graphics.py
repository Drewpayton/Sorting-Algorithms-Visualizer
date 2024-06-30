from tkinter import Tk, BOTH, Canvas, Button, Radiobutton, StringVar
from algorithms import Algorithms
import random
import time

class Window:
    def __init__(self, height, width):
        # Created window with title and canvas, array for rectangles.
        self.root = Tk()
        self.height = height
        self.width = width
        self.root.title("Sorting Algorithm Visualizer")
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="light grey")
        self.rectangles = []
        self.running = False
        
        # This automatically assigns the default value with Bubble sort
        self.selected_algorithm = StringVar()
        self.selected_algorithm.set("A")

        # used bubbleSort, insertionSort, and selectionSort to sort out the rectangles array.
        self.r1 = Radiobutton(self.root, text="Bubble Sort", variable=self.selected_algorithm, value="A")
        self.r2 = Radiobutton(self.root, text="Insertion Sort", variable=self.selected_algorithm, value="B")
        self.r3 = Radiobutton(self.root, text="Selection Sort", variable=self.selected_algorithm, value="C")
        # self.r4 = Radiobutton(self.root, text="Merge Sort", variable=self.selected_algorithm, value="D")
        # self.r5 = Radiobutton(self.root, text="Heap Sort", variable=self.selected_algorithm, value="E")
        # self.r6 = Radiobutton(self.root, text="Radix Sort", variable=self.selected_algorithm, value="F")
        # self.r7 = Radiobutton(self.root, text="Quick Sort", variable=self.selected_algorithm, value="G")
        self.solveButton = Button(self.root, text="Sort", command=self.sorter)
        self.newArrayButton = Button(self.root, text="New Array", command=self.randomizer)

        # Placing the buttons
        self.r1.place(x=250, y=99)
        self.r2.place(x=250, y=124)
        self.r3.place(x=250, y=149)
        # self.r4.place(x=250, y=174)
        # self.r5.place(x=250, y=199)
        # self.r6.place(x=250, y=224)
        # self.r7.place(x=250, y=249)
        self.solveButton.place(x=500, y=100)
        self.newArrayButton.place(x=500, y=200)

        # Creating a structured UI
        self.canvas.create_rectangle((100, 75), (1100, 300), fill="light gray")
        self.canvas.create_rectangle((100, 325), (1100, 800), fill="light gray")
        self._create_rectangle(20)

        self.canvas.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # Updates any pending tasks because tkinter doesn't automatically update.
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    # This waits on the user to close the window.
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            # time.sleep(0.05)
    
    def close(self):
        self.running = False
    
    # This allows the sorting algorithm to move the rectangles
    def visualize(self):
        for i, rect in enumerate(self.rectangles):
            rect.move(300+i * 30, rect.y1)
        self.canvas.update()
        # time.sleep(0.05)
    
    # User chooses the algorithm and then this selects it
    def sorter(self):
        val = self.selected_algorithm.get()
        if val == "A":
            self.bubble_sort_visualize()
        elif val == "B":
            self.insertion_sort_visualize()
        elif val == "C":
            self.selection_sort_visualize()
        elif val == "D":
            self.merge_sort_visualize()
        elif val == "E":
            self.heap_sort_visualize()
        elif val == "F":
            self.radix_sort_visualize()
        elif val == "G":
            self.quick_sort_visualize()

    # calls the algorithm passing in the each rectangles height and visualize function
    def bubble_sort_visualize(self):
        def key(rect): return rect.height
        sorting = Algorithms(self.rectangles)
        sorting.bubbleSort(key=key, visualize=self.visualize)
    
    def insertion_sort_visualize(self):
        def key(rect): return rect.height
        sorting = Algorithms(self.rectangles)
        sorting.insertionSort(key=key, visualize=self.visualize)

    def selection_sort_visualize(self):
        def key(rect): return rect.height
        sorting = Algorithms(self.rectangles)
        sorting.selectionSort(key=key, visualize=self.visualize)

    # def merge_sort_visualize(self):
    #     def key(rect): return rect.height
    #     sorting = Algorithms(self.rectangles)
    #     sorting.mergeSort(key=key, visualize=self.visualize)

    # def heap_sort_visualize(self):
    #     def key(rect): return rect.height
    #     sorting = Algorithms(self.rectangles)
    #     sorting.heapSort(key=key, visualize=self.visualize)

    # def radix_sort_visualize(self):
    #     def key(rect): return rect.height
    #     sorting = Algorithms(self.rectangles)
    #     sorting.radixSort(key=key, visualize=self.visualize)

    # def quick_sort_visualize(self):
    #     def key(rect): return rect.height
    #     sorting = Algorithms(self.rectangles)
    #     sorting.quickSort(key=key, visualize=self.visualize)

    # Creates each rectangle and appends it to an arr
    def _create_rectangle(self, num_rectangles):
        for i in range(num_rectangles):
            x1, y1 = 300 + i * 30, random.randint(450, 700)
            x2, y2 = x1 + 15, 800
            color = "blue"
            height = y2 - y1
            rect = Rectangle(self.canvas, x1, y1, x2, y2, color, height)
            self.rectangles.append(rect)

    # Copies over the rectangle arr and calls _create_rectangle to create 20 more rectangles that are randomized
    def randomizer(self):
        self.rectangles = []
        self.canvas.delete("all")
        self.canvas.create_rectangle((100, 75), (1100, 300), fill="light gray")
        self.canvas.create_rectangle((100, 325), (1100, 800), fill="light gray")
        self._create_rectangle(20)

# This class is the structure to create a rectangle.
class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2, color, height):
        self.canvas = canvas
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.color = color
        self.height = height

    # This allows the visualizer to move the rectangles.
    def move(self, x1, y1):
        x2 = x1 + (self.x2 - self.x1)
        y2 = y1 + (self.y2 - self.y1)
        self.canvas.coords(self.id, x1, y1, x2, y2)
    
    # Changes the color of the rectangle.
    def change_color(self, color):
        self.canvas.itemconfig(self.id, fill=color)