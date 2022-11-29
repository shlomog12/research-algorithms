
from abc import ABC
import queue

class Struct(ABC):

    def __init__(self):
        raise NotImplementedError("Choose a specific output type")

    def add(self, v):
        raise NotImplementedError("Choose a specific output type")

    def get(self):
        raise NotImplementedError("Choose a specific output type")

    def is_empty(self):
        raise NotImplementedError("Choose a specific output type")

class Queue(Struct):

    def __init__(self):
        self.q = queue.Queue()
    

    def add(self, v):
        self.q.put(v)

    def get(self):
        return self.q.get()

    def is_empty(self):
        return self.q.empty()

class Stack(Struct):

    def __init__(self):
        self.stack = []
    
    def add(self, v):
        self.stack.append(v)

    def get(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0