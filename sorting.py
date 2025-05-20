class Sorter:
    """
    Пример использования
    s = Sorter()
    array = [64, 34, -19, 25, 12, 22, 11, 90]
    b = s.selection_sort(array.copy()) # Исходный массив не изменится при сортировке
    a = s.selection_sort(array) # Исходный массив изменится при сортировке

    """
    
    def selection_sort(self, array):
        # Реализация сортировки выбором O(n²)
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]
        return array

    def bubble_sort(self, array):
        # Реализация пузырьковой сортировки O(n²)
        for i in range(len(array)):
            swapped = False
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if not swapped:
                break
        return array

    def insertion_sort(self, array):
        # Реализация сортировки вставками O(n²)
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j] < array[j-1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    break
        return array
                

    
s = Sorter()