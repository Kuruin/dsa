class Sorting1:
    def selection_sort(self, arr):
        for i in range(len(arr)-1):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)

    def bubble_sort(self, arr):
        swap = 0
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap += 1
            if swap == 0:
                break
        print(arr)

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            j = i  # j is used just for better understanding, you can use i instead
            while (j > 0 and arr[j-1] > arr[j]):
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
        print(arr)

    def insertion_sort2(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while (j >= 0 and arr[j] > key):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        print(arr)


sol = Sorting1()
sol.insertion_sort2([13, 46, 24, 52, 20, 9])
