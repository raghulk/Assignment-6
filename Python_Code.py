import random

# Deterministic Selection (Median of Medians)
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide into groups of 5 and find medians
    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]

    # Step 2: Recursively find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Step 3: Partition around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + arr.count(pivot):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - arr.count(pivot))

# Randomized Quickselect Algorithm
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]

    if k < len(low):
        return quickselect(low, k)
    elif k < len(low) + arr.count(pivot):
        return pivot
    else:
        return quickselect(high, k - len(low) - arr.count(pivot))

# Implementation of Basic Data Structures

# 1. Arrays and Matrices
class Array:
    def __init__(self):
        self.data = []
    def insert(self, value):
        self.data.append(value)
    def delete(self, index):
        if 0 <= index < len(self.data):
            self.data.pop(index)
    def access(self, index):
        return self.data[index] if 0 <= index < len(self.data) else None

# 2. Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def peek(self):
        return self.stack[-1] if self.stack else None

# 3. Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

# 4. Singly Linked List Implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def delete(self, value):
        temp = self.head
        prev = None
        while temp and temp.value != value:
            prev, temp = temp, temp.next
        if temp:
            if prev:
                prev.next = temp.next
            else:
                self.head = temp.next
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value, end=' -> ')
            temp = temp.next
        print('None')

# Testing the Implementations
if __name__ == "__main__":
    import time

    arr = [random.randint(1, 100000) for _ in range(10000)]
    k = 5000

    start = time.time()
    print(f"Median of Medians result: {median_of_medians(arr, k)}")
    print(f"Time Taken: {time.time() - start} seconds")

    start = time.time()
    print(f"Quickselect result: {quickselect(arr, k)}")
    print(f"Time Taken: {time.time() - start} seconds")

    # Testing Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack Pop:", stack.pop())

    # Testing Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue Dequeue:", queue.dequeue())

    # Testing Linked List
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print("Linked List Traversal:")
    ll.traverse()
