#using lists as queues
from collections import deque
queue = deque(["one","two","three","four"])
queue.append("five")
queue.append("six")

queue.popleft()
print(queue)
