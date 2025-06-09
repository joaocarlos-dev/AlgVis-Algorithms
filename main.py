from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Libera CORS para o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SortRequest(BaseModel):
    array: List[int]


class SortStep(BaseModel):
    array: List[int]
    compared: List[int]


@app.get("/")
def read_root():
    return {"message": "Backend de algoritmos rodando! Use /bubble-sort com POST."}


@app.post("/bubble-sort", response_model=List[SortStep])
def bubble_sort(data: SortRequest):
    steps = []
    arr = data.array[:]
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            steps.append(SortStep(array=arr[:], compared=[j, j + 1]))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(SortStep(array=arr[:], compared=[j, j + 1]))
    return steps
