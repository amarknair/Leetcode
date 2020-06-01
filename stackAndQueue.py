stack = []
stack.append(1)
stack.append(2)
stack.append(3)
a = stack.pop()
print(stack)

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
b = queue.pop(0)
print(queue)

from Queue import PriorityQueue

q = PriorityQueue()
q.put(1)
q.put(2)
q.put(77)
q.put(10)