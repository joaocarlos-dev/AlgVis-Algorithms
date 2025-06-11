from typing import List
from sorts.model import SortRequest, SortStep


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
