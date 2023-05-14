# ADT

Abstract Data Type (ADT): A description of information and a collection of operations on that information.

The information is accessed only through the operations.

For example, list is an Abstract Data Type, we can perform these operations.

```python
lst.append()
lst.pop()
lst.extend
```

We do not know how exactly list is implement, it is like a black box and we can access the black box through the operations it provide.

# Linked List

<img src="./img/0.png" />

**Example of linked List in python**

```python
class Node:
    def __init__(self, data = None):
      self.data = data
      self.next_node = None

class LinkedList:
    def __init__(self):
      self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_head = Node(data)
            new_head.next_node = self.head

            self.head = new_head

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        pass
```

**Complexity of Linked list:**
- Insert: O(1)
- Delete: O(n)
- Search:  O(n)

**Exercise**: Write the delete funciton in class LinkedList


# Advantages

Linked lists are beneficial in situations where you need to do frequent insertions and deletions. Unlike arrays and lists, which require O(n) time complexity to insert an element at the beginning or middle, linked lists can perform these operations in O(1) time complexity.

In addition, if you're working in an environment where memory is fragmented (rather than contiguous as required by arrays), linked lists can be more efficient.

# Singly Linked List vs Doubly Linked List

The linked list we've described so far is a singly linked list, because each node only has a reference to the next node.

In contrast, a doubly linked list has nodes that also reference the previous node. This provides more flexibility at the cost of increased complexity and memory usage.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        pass

    def search(self, node):
        pass

    def delete(self, pos):
        pass
```

**Exercise**: Fill the  function for class DoublyLinkedList.


# Double Pointer
This problem can be solved using two pointers: a slow-pointer and a fast-pointer. The slow-pointer moves one step at a time, while the fast-pointer moves two steps at a time. If there's a cycle, the fast-pointer will eventually meet the slow-pointer again. If there's no cycle, the fast-pointer will reach the end of the list.

**Example**: Detect a cycle

```python
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True
```

**Exercise**: Use Linked list to see if a string is a Palindrome

```python
def is_palindrome(s):
    pass

s = 'aba'
is_palindrome(s) # True

s = 'abcdedcba'
is_palindrome(s) # True
```


# Summary

Linked lists provide a versatile tool for handling ordered data. While their performance characteristics make them less suitable for certain tasks (like accessing elements by index), they excel in other areas, particularly when it comes to insertion and deletion of elements.

Remember that the right data structure depends on the specific requirements of your task, such as the nature of your data, the operations you need to perform on it, and the memory and performance constraints of your system.