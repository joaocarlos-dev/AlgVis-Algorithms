# models.py
from pydantic import BaseModel
from typing import List


class SortRequest(BaseModel):
    array: List[int]


class SortStep(BaseModel):
    array: List[int]
    compared: List[int]
