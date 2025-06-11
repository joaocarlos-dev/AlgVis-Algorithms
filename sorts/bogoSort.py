import random
from typing import List
from sorts.model import SortRequest, SortStep


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
