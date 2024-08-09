from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.deque = deque([],maxlen=size)
    def next(self, val: int) -> float:
        self.deque.append(val)
        return sum(self.deque)/len(self.deque)


class MovingAverage2:
    def __init__(self, size: int):
        self.sum = 0
        self.size = size
        self.data = []
    def next(self, val: int) -> float:
        self.sum += val
        self.data.append(val)
        if len(self.data) > self.size:
            self.sum -= self.data[0]
            self.data.pop(0)
        return self.sum / len(self.data)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)