from fastapi import APIRouter
from typing import List
from sorts.model import SortRequest, SortStep
from sorts.bogoSort import bogo_sort
from sorts.bubbleSort import bubble_sort
from sorts.insertionSort import insertion_sort
from sorts.quickSort import quick_sort
from sorts.selectionSort import selection_sort

router = APIRouter()


@router.post("/bubble-sort", response_model=List[SortStep])
def bubble_sort_route(data: SortRequest):
    return bubble_sort(data)


@router.post("/selection-sort", response_model=List[SortStep])
def selection_sort_route(data: SortRequest):
    return selection_sort(data)


@router.post("/bogo-sort", response_model=List[SortStep])
def bogo_sort_route(data: SortRequest):
    return bogo_sort(data)


@router.post("/insertion-sort", response_model=List[SortStep])
def insertion_sort_route(data: SortRequest):
    return insertion_sort(data)


@router.post("/quick-sort", response_model=List[SortStep])
def quick_sort_route(data: SortRequest):
    return quick_sort(data)
