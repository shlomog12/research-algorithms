
from abc import ABC
import queue
from typing import Any, List
class Struct(ABC):

    def add(self, v:Any):
        raise NotImplementedError("Choose a struct")

    def get(self) -> Any:
        raise NotImplementedError("Choose a struct")

    def is_empty(self)-> bool:
        raise NotImplementedError("Choose a struct")

class Queue(Struct):

    def __init__(self):
        self.q = queue.Queue()
    

    def add(self, v:Any):
        self.q.put(v)

    def get(self) -> Any:
        return self.q.get()

    def is_empty(self) -> bool:
        return self.q.empty()

class Stack(Struct):

    def __init__(self):
        self.stack = []
    
    def add(self, v:Any):
        self.stack.append(v)

    def get(self) -> Any:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0