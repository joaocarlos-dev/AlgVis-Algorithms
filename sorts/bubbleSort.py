from typing import List
from sorts.model import SortRequest, SortStep


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
