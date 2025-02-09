Overview
This project demonstrates two selection algorithms for finding the k-th smallest element in an unsorted list:

Median of Medians (Deterministic Selection)
Quickselect (Randomized Selection)
It also provides implementations of common data structures such as:

Array
Stack
Queue
Singly Linked List
The provided script tests both algorithms and the data structures.

Algorithms
1. Median of Medians
The Median of Medians is a deterministic algorithm that guarantees an optimal pivot selection, leading to a worst-case time complexity of O(n). It works as follows:

Divides the array into groups of 5 elements.
Finds the median of each group.
Recursively finds the median of those medians.
Partitions the array based on this pivot and selects the k-th smallest element.
Time Complexity:
Worst Case: O(n)
Best Case: O(n)2. Quickselect
The Quickselect algorithm is a randomized selection algorithm similar to QuickSort. It chooses a random pivot, partitions the array, and recursively selects the k-th smallest element.

Time Complexity:
Average Case: O(n)
Worst Case: O(n²) (if an unlucky pivot is chosen)Data Structures
This project also implements fundamental data structures:

1. Array
A simple dynamic array implementation with:

insert(value): Adds an element to the array.
delete(index): Removes an element at the given index.
access(index): Retrieves an element by index.

2. Stack
A last-in, first-out (LIFO) data structure with:

push(value): Adds an element to the stack.
pop(): Removes and returns the top element.
peek(): Returns the top element without removing it.
3. Queue
A first-in, first-out (FIFO) data structure with:

enqueue(value): Adds an element to the queue.
dequeue(): Removes and returns the front element.
4. Singly Linked List
A linked list with:

insert(value): Inserts a node at the head.
delete(value): Deletes the first occurrence of a node with the given value.
traverse(): Prints all elements in the linked list.

Performance Comparison
The script compares the Median of Medians and Quickselect algorithms in terms of execution time. Generally, Quickselect is faster on average but has a worse-case O(n²) complexity.

Testing
To test the data structures manually:

Modify the script to insert, delete, or access elements.
Run the script and check console output.
