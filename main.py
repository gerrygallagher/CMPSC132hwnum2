import random


class Node(object):
    """Doubly linked node which stores an object"""

    def __init__(self, element, next_node=None, previous_node=None):
        # The underscores are to prevent overwriting the variables if inherited and prevents access from outside of scope
        self.__element = element
        self.__next_node = next_node
        self.__previous_node = previous_node

    def get_element(self):
        """Returns the element stored in this node"""
        return self.__element

    def get_previous(self):
        """Returns the previous linked node"""
        return self.__previous_node

    def get_next(self):
        """Returns the next linked node"""
        return self.__next_node

    def set_element(self, element):
        """Sets the element stored in this node"""
        self.__element = element

    def set_previous(self, previous_node):
        """Sets the previous linked node"""
        self.__previous_node = previous_node

    def set_next(self, next_node):
        """Sets the next linked node"""
        self.__next_node = next_node

    def __str__(self):
        return str(self.__element)


class DoublyLinkedList(object):
    """Doubly linked node data structure"""

    def __init__(self):
        self.__size = 0
        self.__header = Node('Header')
        self.__trailer = Node('Trailer')
        self.__header.set_next(self.__trailer)
        self.__trailer.set_previous(self.__header)
        self.__current = None

    def __iter__(self):
        self.__current = None
        return self

    def __next__(self):
        """Standard python iterator method"""
        if self.is_empty() or self.__current == self.__trailer:
            raise StopIteration()
        elif self.__current is None:
            self.__current = self.__header
        self.__current = self.__current.get_next()
        return self.__current

    def map(self, function):
        """Run function on every element in the list"""
        for node in self:
            if node != self.__trailer and node != self.__header:
                node.set_element(function(node.get_element()))

    def size(self):
        """Returns the number of elements in the list"""
        return self.__size

    def is_empty(self):
        """Returns the number of elements in the list"""
        return self.__size == 0

    def get_first(self):
        """Get the first element of the list"""
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__header.get_next()

    def get_last(self):
        """Get the last element of the list"""
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__trailer.get_previous()

    def get_previous(self, node):
        """Returns the node before the given node"""
        if node == self.__header:
            raise Exception("Cannot get the element before the header of this list")
        else:
            return node.get_previous()

    def get_next(self, node):
        """Returns the node after the given node"""
        if node == self.__trailer:
            raise Exception("Cannot get the element after the trailer of this list")
        else:
            return node.get_next()

    def add_before(self, new, existing):
        """Insert the new before existing"""
        previous_existing = self.get_previous(existing)
        new.set_previous(previous_existing)
        new.set_next(existing)
        existing.set_previous(new)
        previous_existing.set_next(new)
        self.__size += 1

    def add_after(self, new, existing):
        """Insert the new after existing"""
        next_existing = self.get_next(existing)
        new.set_previous(existing)
        new.set_next(next_existing)
        existing.set_next(new)
        next_existing.set_previous(new)
        self.__size += 1

    def add_first(self, new):
        """Insert the node at the head of the list"""
        self.add_after(new, self.__header)

    def add_last(self, new):
        """Insert the node at the tail of the list"""
        self.add_before(new, self.__trailer)

    def remove(self, node):
        """Removes the given node from the list"""
        before = self.get_previous(node)
        after = self.get_next(node)
        before.set_next(after)
        after.set_previous(before)
        node.set_next(None)
        node.set_previous(None)
        self.__size -= 1




dll = DoublyLinkedList()
for i in range(10):
    dll.add_last(Node(random.randint(0, 10)))
for i in dll:
    print(i)

print()
print()
print()


#task 11
add2 = lambda num : num + 2
dll.map(add2)
for i in dll:
    print(i)

print()
print()
print()

#task 12
multby5 = lambda num : num * 5
dll.map(multby5)
for i in dll:
    print(i)

print()
print()
print()




# task 13

# remove mults of 6

current = dll.get_first()
while (current != dll.get_last().get_next()):
    next = current.get_next()
    if (current.get_element() % 6 == 0):
        dll.remove(current)
    current = next

for i in dll:
    print(i)


print()
print()
print()


#task 14

current = dll.get_first();
while (current != dll.get_last().get_next()):
    next = current.get_next();
    if (current.get_element() % 2 == 1):
        dll.remove(current);

    current = next;

for i in dll:
    print(i)


























"""**Task 1 (5 points)**: Using the constructor from the **DoublyLinkedList**, 
create a new doubly linked list of random integers between 1 and 10."""
"""## Using a Doubly Linked List
The given **DoublyLinkedList** Python class
contains helpful methods for using a doubly linked list.
Answer the following questions while implementing
the methods of the **DoublyLinkedList** class.
**Task 2 (10 points)**: Implement the `size` method that returns the size of a 
doubly linked list.
```python
def size(self):
  '''Returns the number of elements in the list.'''
  pass 
```
"""
# Test your implementation here
"""**Task 3 (5 points)**: Implement the `is_empty` method that checks
whether a doubly linked list is empty.
```python
def is_empty(self):
  '''Returns the number of elements in the list'''
  pass
```
"""
# Test your implementation here
"""**T4 (10 points)**: Implement the methods `get_first` and `get_last`
to get the first and the last element of the list, respectively.
_Hint_: Return an exception in case the list is empty.
```python
def get_first(self):
  '''Get the first element of the list'''
  pass
def get_last(self):
  '''Get the last element of the list'''
  pass
```
"""
# Test your implementation here
"""**Task 5 (10 points)**: Implement the methods `get_previous` and `get_next`
to get the previous and the next node of the list, respectively.
_Hint_: Return an exception in case the list is empty.
```python
def get_previous(self, node):
  '''Returns the node before the given node'''
  pass      
def get_next(self, node):
  '''Returns the node after the given node'''
  pass
```
"""
# Test your implementation here
"""**Task 6(10 points)**: Implement the methods `add_before` and `add_after`
to respectively insert new elements before and after a node of the list.
```python
def add_before(self, new, existing):
  '''Insert the new before existing'''
  pass
def add_after(self, new, existing):
  '''Insert the new after existing'''
  pass
```
"""
# Test your implementation here
"""**Task 7 (10 points)**: Implement the methods `add_first` and `add_first`
to respectively insert new nodes in the beginning and in the end of a list.
```python
def add_first(self, new):
  '''Insert the node at the head of the list'''
  pass
def add_last(self, new):
  '''Insert the node at the tail of the list'''
  pass
```
"""
# Test your implementation here
"""**Task 8 (10 points)**: Implement the method `remove` to remove
a node from a list.
```python
def remove(self, node):
  '''Removes the given node from the list'''
  pass
```
"""
# Test your implementation here
"""**Task 9 (10 points)**: Implement the method `map` to apply a function on
each element of a list.
```python
def map(self, function):
  '''Run function on every element in the list'''
  pass
```
"""
# Test your implementation here
"""**Task 10 (10 points)**: Implement the method `next` to iterate the elements
of a list.
```python
'''Standard methods for Python iterator'''
def __iter__(self):
  pass
def __next__(self):
  pass
```
"""
# Test your implementation here
"""## Applying methods of the DoublyLinkedList and Node classes
Answer the following questions by using
the implemented methods from the Node and DoublyLinkedList classes.
Apply your operations on the list you created in T1.
**Task 11 (5 points)**: Add 2 to each element of the list.
_Hint_: Use the method `map`.
"""
"""
**Task 12 (5 points)**: Multiply each element of the list by 5.
_Hint_: Use the methods `map`, `get_previous`, and `set_element`."""
"""
**Task 13 (5 points)**: Remove elements that are multiplies of 6.
_Hint_: Use the methods `next` and `remove`."""
"""
**Task 14 (5 points)**: Remove elements from the list that are odd numbers. 
_Hint_: Use the methods `get_previous` and `remove`."""
"""## Proving performance properties
**Task 15 (5 points)**: Prove when the complexity to delete a node in a doubly 
"linked list is $O(1)$ and $O(n)$"
"""