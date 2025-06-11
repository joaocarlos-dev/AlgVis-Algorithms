from typing import List

from sorts.model import SortRequest, SortStep


def quick_sort(data: SortRequest) -> List[SortStep]:
    steps = []
    arr = data.array[:]

    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        steps.append(SortStep(array=arr[:], compared=[high]))

        for j in range(low, high):
            steps.append(SortStep(array=arr[:], compared=[j, high]))

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(SortStep(array=arr[:], compared=[i, j]))  # troca

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(SortStep(array=arr[:], compared=[i + 1, high]))

        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return steps
