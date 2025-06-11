import random
from typing import List

from sorts.models import SortRequest, SortStep


def bubble_sort(data: SortRequest) -> List[SortStep]:
    steps = []
    arr = data.array[:]
    for i in range(len(arr)-1, 0, -1):
        changes = 0
        for j in range(i):
            steps.append(SortStep(array=arr[:], compared=[j, j + 1]))
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(SortStep(array=arr[:], compared=[j, j + 1]))
                changes += 1
        if changes < 1:
            break
    return steps


def bogo_sort(data: SortRequest) -> List[SortStep]:
    steps = []
    arr = data.array[:]

    def is_sorted(array):
        return all(array[i] <= array[i + 1] for i in range(len(array) - 1))

    while not is_sorted(arr):
        steps.append(SortStep(array=arr[:], compared=[]))
        random.shuffle(arr)
        steps.append(SortStep(array=arr[:], compared=[]))

    steps.append(SortStep(array=arr[:], compared=[]))
    return steps


def selection_sort(data: SortRequest) -> List[SortStep]:
    steps = []
    arr = data.array[:]
    for i in range(len(arr) - 1):
        minpos = i
        for j in range(i + 1, len(arr)):
            steps.append(SortStep(array=arr[:], compared=[j, minpos]))
            if arr[j] < arr[minpos]:
                minpos = j
                steps.append(SortStep(array=arr[:], compared=[minpos]))
        arr[i], arr[minpos] = arr[minpos], arr[i]
        steps.append(SortStep(array=arr[:], compared=[i, minpos]))
    return steps
