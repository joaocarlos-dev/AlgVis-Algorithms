# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List


import sorts
from sorts.models import SortRequest, SortStep
from sorts.sorts import bubble_sort, insertion_sort, selection_sort, bogo_sort

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Backend de algoritmos rodando! Use /bubble-sort com POST."}


@app.post("/bubble-sort", response_model=List[SortStep])
def bubble_sort_route(data: SortRequest):
    return bubble_sort(data)


@app.post("/selection-sort", response_model=List[SortStep])
def selection_sort_route(data: SortRequest):
    return selection_sort(data)


@app.post("/bogo-sort", response_model=List[SortStep])
def bogo_sort_route(data: SortRequest):
    return bogo_sort(data)


@app.post("/insertion-sort", response_model=List[SortStep])
def insertion_sort_route(data: SortRequest):
    return insertion_sort(data)
