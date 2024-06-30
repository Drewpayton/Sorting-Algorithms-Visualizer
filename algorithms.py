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
                    time.sleep(.05)
                if key(self.arr[j]) > key(self.arr[j+1]):
                    # Highlight the rectangles being swapped
                    self.arr[j].change_color('red')
                    self.arr[j+1].change_color('red')
                    if visualize:
                        visualize()
                        time.sleep(0.05)  # Longer delay to highlight the swap

                    # Swap the rectangles
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True

                    # Revert the color after swap
                    self.arr[j].change_color('blue')
                    self.arr[j+1].change_color('blue')
                    if visualize:
                        visualize()
                        time.sleep(0.05)  # Delay to show the reverted color
                else:
                    self.arr[j].change_color("blue")
                    self.arr[j+1].change_color("blue")
                    if visualize:
                        visualize()
                        time.sleep(.05)
            self.arr[j+1].change_color("purple")
            if visualize:
                visualize()
                # time.sleep(.2)
            if not swapped:
                for k in range(i+1):
                    self.arr[k].change_color("purple")
                    if visualize:
                        visualize()
                        time.sleep(0.05)
                break
        

    def insertionSort(self, key=lambda x: x, visualize=None):
        n = len(self.arr)

        for i in range(1, n):
            j = i
            while key(self.arr[j-1]) > key(self.arr[j]) and j > 0:
                self.arr[j-1], self.arr[j] = self.arr[j], self.arr[j - 1]
                self.arr[j-1].change_color("yellow")
                j -= 1
                if visualize:
                    visualize()
                    time.sleep(0.2)
                self.arr[j].change_color("blue")
                if visualize:
                    visualize()
            
        

    def selectionSort(self, key=lambda x: x, visualize=None):
        n = len(self.arr)

        for i in range(n):
            cur_min = i
            self.arr[i].change_color("yellow")
            if visualize:
                visualize()
                time.sleep(.1)
            for j in range(i+1, n):
                self.arr[j].change_color("red")
                if visualize:
                    visualize()
                    time.sleep(.3)
                self.arr[j].change_color("blue")
                if visualize:
                    visualize()
                if key(self.arr[j]) < key(self.arr[cur_min]):
                    if cur_min != i:
                        self.arr[cur_min].change_color("blue")
                    cur_min = j
                    self.arr[cur_min].change_color("green")
                    if visualize:
                        visualize()
                
            self.arr[i], self.arr[cur_min] = self.arr[cur_min], self.arr[i]
            self.arr[i].change_color("blue")
            self.arr[cur_min].change_color("blue")
            if visualize:
                visualize()
                time.sleep(.3)

    # def mergeSort(self, key=lambda x: x, visualize=None):
    #     def _mergeSort(arr):
    #         if len(arr) > 1:
    #             mid = len(arr) // 2
    #             left_arr = arr[:mid]
    #             right_arr = arr[mid:]

    #             # Recursive calls
    #             left_arr = _mergeSort(left_arr)
    #             right_arr = _mergeSort(right_arr)

    #             i, j, k = 0, 0, 0
    #             while i < len(left_arr) and j < len(right_arr):
    #                 if key(left_arr[i]) < key(right_arr[j]):
    #                     arr[k] = left_arr[i]
    #                     i += 1
    #                     if visualize:
    #                         visualize()
    #                 else:
    #                     arr[k] = right_arr[j]
    #                     j += 1
    #                 if visualize:
    #                     visualize()
    #                     time.sleep(0.1)
    #                 k += 1

    #             while i < len(left_arr):
    #                 arr[k] = left_arr[i]
    #                 i += 1
    #                 k += 1
    #                 if visualize:
    #                     visualize()
    #                     time.sleep(0.05)

    #             while j < len(right_arr):
    #                 arr[k] = right_arr[j]
    #                 j += 1
    #                 k += 1
    #                 if visualize:
    #                     visualize()
    #                     time.sleep(0.05)

    #         return arr

    #     self.arr = _mergeSort(self.arr)
    #     if visualize:
    #         visualize()
    #         time.sleep(.3)

            



    # def heapSort(self, key=lambda x: x, visualize=None):
    #     pass

    # def radixSort(self, key=lambda x: x, visualize=None):
    #     pass
    
    # def quickSort(self, key=lambda x: x, visualize=None):
    #     pass
    