import time

class Algorithms:
    def __init__(self, arr):
        self.arr = arr

    def bubbleSort(self, key=lambda x: x, visualize=None):
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                self.arr[j].change_color("green")
                self.arr[j+1].change_color("green")
                if visualize:
                    visualize()
                    time.sleep(.1)
                if key(self.arr[j]) > key(self.arr[j+1]):
                    # Highlight the rectangles being swapped
                    self.arr[j].change_color('red')
                    self.arr[j+1].change_color('red')
                    if visualize:
                        visualize()
                        time.sleep(0.1)  # Longer delay to highlight the swap

                    # Swap the rectangles
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True

                    # Revert the color after swap
                    self.arr[j].change_color('blue')
                    self.arr[j+1].change_color('blue')
                    if visualize:
                        visualize()
                        time.sleep(0.1)  # Delay to show the reverted color
                else:
                    self.arr[j].change_color("blue")
                    self.arr[j+1].change_color("blue")
                    if visualize:
                        visualize()
                        time.sleep(.1)
            self.arr[j+1].change_color("purple")
            if visualize:
                visualize()
                # time.sleep(.2)
            if not swapped:
                for k in range(i+1):
                    self.arr[k].change_color("purple")
                    if visualize:
                        visualize()
                        time.sleep(0.1)
                break
        
        
    def insertionSort(self):
        pass

    def selectionSort(self):
        pass

    def mergeSort(self):
        pass

    def heapSort(self):
        pass

    def radixSort(self):
        pass
    
    def quickSort(self):
        pass
    