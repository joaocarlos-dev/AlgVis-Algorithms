from typing import List
from sorts.model import SortRequest, SortStep


def insertion_sort(data: SortRequest) -> List[SortStep]:
    steps = []
    arr = data.array[:]

    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        steps.append(SortStep(array=arr[:], compared=[j, i]))

        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            steps.append(SortStep(array=arr[:], compared=[j]))

            j -= 1
            if j >= 0:
                steps.append(SortStep(array=arr[:], compared=[j, j + 1]))

        arr[j + 1] = key_item
        steps.append(SortStep(array=arr[:], compared=[j + 1]))

    return steps
