# %% [markdown]
# # 09. Stacks and Queues
# ## Today's Agenda
# 1. Stacks
# 2. Queues
#

# %% [markdown]
# ## Stack (LIFO)
# In a FIFO queue, the first tasks added are the first retrieved.
#
# We can implement using:
# 1. list
# 2. [collections.deque](https://docs.python.org/3/library/collections.html#deque-objects)
# 3. [queue.Queue](https://docs.python.org/3/library/queue.html)
#
# Stacks typically support the following operation:
# 1. Push
# 2. Pop
# 3. Peek

# %%
# Using a list as a stack


# %%
class StackList:
    """
    Stack Implementation using a List
    """

    def __init__(self, size):
        self.container = [None] * size
        self.capacity = size
        self.top = -1

    def push(self, x):
        """
        Method to add an element `x` to the stack
        """
        if self.is_full():
            raise Exception("Stack is full!")

        pass

    def pop(self):
        """
        Method to pop a top element from the stack
        """
        if self.is_empty():
            return None

        print("Removing", self.peek(), "from the stack")

        pass

    def peek(self):
        """
        Method to return the top element of the stack
        """
        if self.is_empty():
            return None

        pass

    def size(self):
        """
        Method to return the size of the stack
        """
        return self.top + 1

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity


# %%
stack = StackList(3)

stack.push(1)
stack.push(2)

stack.pop()
stack.pop()

stack.push(3)

print("Top element is", stack.peek())
print("The stack size is", stack.size())

stack.pop()

if stack.is_empty():
    print("The stack is empty")
else:
    print("The stack is not empty")

# %% [markdown]
# We should prefer using the collections already provided by python as they are optimised and thread-safe.
# > The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming when information must be exchanged safely between multiple threads.

# %%
# LIFO QUEUE - i.e. Stack
from queue import LifoQueue

q = LifoQueue(maxsize=10)
q.put(1)
q.put(25)
q.put(30)

while not q.empty():
    print(q.get())


# %%
# Stack using collections.dequeue

from collections import deque

# NB: module deque alredy has useful methods, so we don't need to re-implement them
stack = deque()


stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")


print("Top element is", stack[-1])  # prints the stack's top (4)

print("Removing", stack.pop(), "from the stack")  # removing the top element (4)
print("Removing", stack.pop(), "from the stack")  # removing the next top (3)

# returns the total number of elements present in the stack
print("Stack size is", len(stack))

print("Removing", stack.pop(), "from the stack")  # removing the top element (2)
print("Removing", stack.pop(), "from the stack")  # removing the next top (1)

# check if the stack is empty
if len(stack) == 0:
    print("The stack is empty")
else:
    print("The stack is not empty")


# %% [markdown]
# ## Queues (FIFO)
# In a FIFO queue, the first tasks added are the first retrieved.
#
# We can implement using:
# 1. list
# 2. [collections.deque](https://docs.python.org/3/library/collections.html#deque-objects)
# 3. [queue.queue](https://docs.python.org/3/library/queue.html)
#
# Queues typically support the following operation:
# 1. Enqueue
# 2. Dequeue
# 3. Peek

# %%
# Using a list as a queue
data = []


# %%

"""
Queue Implementation using a List
"""


class MyQueue:
    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to the front element in the queue
        self.rear = -1  # rear points to the last element in the queue
        self.count = 0  # current size of the queue

    def pop(self):
        if self.is_empty():
            return None

        element = self.q[self.front]
        print("Removing element…", element)

        self.front = self.front + 1
        self.count = self.count - 1
        return element

    def append(self, value):
        if self.is_full():
            raise Exception("Queue is full!")

        print("Inserting element…", value)

        self.rear = self.rear + 1
        self.q[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.is_empty():
            return None

        return self.q[self.front]

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity


# %%

q = MyQueue(3)

q.append(1)
q.append(2)
q.append(3)

print("The queue size is", q.size())
print("The front element is", q.peek())
q.pop()
print("The front element is", q.peek())

q.pop()
q.pop()

if q.is_empty():
    print("The queue is empty")
else:
    print("The queue is not empty")


# %%
# FIFO QUEUE - i.e a queue
from queue import Queue

q = Queue(maxsize=10)
q.put(1)
q.put(25)
q.put(30)


while not q.empty():
    print(q.get())

# %%
# Queue using collections.dequeue

from collections import deque

# NB: module deque alredy has useful methods, so we don't need to re-implement them
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print("The front element is", queue[0])  # 1

queue.popleft()  # removing the front element (1)
queue.popleft()  # removing the front element (2)

# Print front item of the queue
print("The front element is", queue[0])  # 3

print("The queue size is", len(queue))  # 2

# check whether the queue is empty
if len(queue) == 0:
    print("The queue is empty")
else:
    print("The queue is not empty")

# %% [markdown]
# ## Bonus - Priority Queue
# With a priority queue, the entries are kept sorted and the lowest valued entry is retrieved first.

# %%
from queue import PriorityQueue

party = PriorityQueue(maxsize=5)

party.put((1, "food"))
party.put((3, "drinks"))
party.put((2, "music"))
party.put((5, "lights"))
party.put((0, "clean_the_house"))

while not party.empty():
    print(party.get())
