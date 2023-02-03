import queue
class LFUCache:

    def __init__(self, capacity: int):
        self.cap=queue.Queue()
        self.n=capacity

    def get(self, key: int) -> int:
        self.cap.count

    def put(self, key: int, value: int) -> None:
        
# a=queue.Queue()
# a.put(2)
# a.put(6)
# a.put(7)
# a.put(9)
# a.put(12)
# a.put(2)
# a.put(1)
# while not a.empty():
#     print(a.get())

1,2,3,4,5
5,4,3,2,1
4,5,3,2,1
4,5,1,2,3