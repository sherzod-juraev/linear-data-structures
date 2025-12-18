from node import Node
from exception import Empty
from typing import Any


class SinglyLinkedList:

    def __init__(self):
        """Initialize an empty singly linked list"""

        self.__head = None
        self.__length = 0

    def __normalize_index(self, index: int, /) -> int:
        """
        Normalize a possibly negative index to a valid positive index.

        Raises:
            IndexError: If the normalized index is out of list bounds.
        """

        index = index if index >= 0 else self.__length + index
        if index >= self.__length:
            raise IndexError('Index out of range')
        return index

    def __autoincrement_length(self):

        self.__length += 1

    def __autodecrement_length(self):

        self.__length -= 1

    def __verify_index(self, index: int, /, *, remove: bool = False):
        """
        Check if the given index is valid for current list operations.

        Args:
            index (int): Index to verify.
            remove (bool): Set True if checking for removal operation.

        Raises:
            IndexError: If index is negative or beyond allowed range.
        """

        if self.__length < index or index < 0:
            raise IndexError('Invalid index')
        if remove and index == self.__length:
            raise IndexError('Invalid index for removal')

    def __verify_empty(self):
        """
        Ensure the list is not empty before performing an operation.

        Raises:
            Empty: If the list has no elements.
        """

        if self.__length == 0:
            raise Empty('List is empty')

    def __iter__(self):
        """Return an iterator for the list"""

        self.__current = self.__head
        return self

    def __next__(self):
        """Return the next element during iteration"""

        if self.__current is not None:
            val, self.__current = self.__current.value, self.__current.next
            return val
        else:
            raise StopIteration

    def __getitem__(self, item):
        """Return the element at the specified index"""

        self.__verify_empty()
        item = self.__normalize_index(item)
        current = self.__head
        for _ in range(item):
            current = current.next
        return current.value

    def __setitem__(self, key, value):
        """Set the element at the specified index to a new value"""

        self.__verify_empty()
        key = self.__normalize_index(key)
        current = self.__head
        for _ in range(key):
            current = current.next
        current.value = value

    def __len__(self):
        """Return the number of elements in the list"""

        return self.__length

    def prepend(self, value, /):
        """Insert a new element at the beginning of the list"""

        new_node = Node(value)
        self.__autoincrement_length()
        if self.__head is not None:
            new_node.next = self.__head
        self.__head = new_node

    def append(self, value: Any, /):
        """Insert a new element at the end of the list"""

        current = self.__head
        self.__autoincrement_length()
        if current is None:
            self.__head = Node(value)
            return None
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def insert_at(self, index: int, value: Any, /):
        """Insert a new element at the specified index"""

        self.__verify_index(index)
        new_node = Node(value)
        if index == 0:
            new_node.next = self.__head
            self.__head = new_node
            return None
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.__autoincrement_length()

    def remove_first(self):
        """Remove the first element of the list"""

        self.__verify_empty()
        self.__head = self.__head.next
        self.__autodecrement_length()

    def remove_last(self):
        """Remove the last element of the list"""

        self.__verify_empty()
        if self.__length == 1:
            self.remove_first()
            return None
        current = self.__head
        for _ in range(self.__length - 2):
            current = current.next
        self.__autodecrement_length()
        current.next = None

    def remove_at(self, index, /):
        """Remove the element at the specified index"""

        self.__verify_empty()
        self.__verify_index(index, remove=True)
        self.__autodecrement_length()
        if index == 0:
            self.__head = self.__head.next
            return None
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    def remove(self, value, /):
        """
        Remove the first node with the specified value.

        Raises:
            Empty: If the list is empty.
            ValueError: If the value is not found in the list.
        """

        self.__verify_empty()
        current = self.__head
        for i in range(self.__length - 1):
            if current.next.value == value:
                current.next = current.next.next
                self.__autodecrement_length()
                return None
            elif self.__head.value == value:
                self.__head = self.__head.next
                self.__autodecrement_length()
                return None
            current = current.next
        raise ValueError('qiymat topilmadi')