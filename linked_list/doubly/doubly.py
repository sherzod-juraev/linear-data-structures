from .node import Node
from .exception import Empty
from typing import Any


class DoublyLinkedList:

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__length = 0

    def __normalize_index(self, index: int, /) -> int:

        index = index if index >= 0 else self.__length + index
        if self.__length <= index or index < 0:
            raise IndexError('Index out of range')
        return index

    def __verify_empty(self):

        if self.__length == 0:
            raise Empty('List is empty')

    def __verify_index(self, index: int, /, *, remove: bool = False):

        if self.__length < index or index < 0:
            raise IndexError('Invalid index')
        if remove and self.__length == index:
            raise IndexError('Invalid index for removal')

    def __autoincrement_length(self):

        self.__length += 1

    def __autodecrement_length(self):

        self.__length -= 1

    def __iter__(self):

        current = self.__head
        while current:
            yield current.value
            current = current.next

    def __getitem__(self, item):

        self.__verify_empty()
        item = self.__normalize_index(item)
        if item < self.__length // 2:
            current = self.__head
            for _ in range(item):
                current = current.next
            return current.value
        current = self.__tail
        for _ in range(self.__length - 1, item, -1):
            current = current.prev
        return current.value

    def __setitem__(self, key, value):

        self.__verify_empty()
        key = self.__normalize_index(key)
        if key < self.__length // 2:
            current = self.__head
            for _ in range(key):
                current = current.next
            current.value = value
            return
        current = self.__tail
        for _ in range(self.__length - 1, key, -1):
            current = current.prev
        current.value = value

    def __len__(self):

        return self.__length

    def prepend(self, value: Any, /):
        """Insert a value at the beginning of the list"""

        new_node = Node(value)
        self.__autoincrement_length()
        if self.__head is not None:
            new_node.next = self.__head
            self.__head.prev = new_node
        if self.__tail is None:
            self.__tail = new_node
        self.__head = new_node

    def append(self, value: Any, /):
        """Insert a value at the end of the list"""

        new_node = Node(value)
        self.__autoincrement_length()
        if self.__head is not None:
            self.__tail.next = new_node
            new_node.prev = self.__tail
        else:
            self.__head = new_node
        self.__tail = new_node

    def insert_at(self, index: int, value: Any, /):
        """Insert a value at the specified index"""

        if index == 0:
            self.prepend(value)
            return
        elif index == self.__length:
            self.append(value)
            return
        self.__verify_index(index)
        self.__autoincrement_length()
        new_node = Node(value)
        if index < (self.__length - 1) // 2:
            current = self.__head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            return
        current = self.__tail
        for _ in range(self.__length - 1, index, -1):
            current = current.prev
        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

    def remove_first(self):
        """Remove the first element of the list"""

        self.__verify_empty()
        if self.__length == 1:
            self.__head = None
            self.__tail = None
            self.__autodecrement_length()
            return
        else:
            self.__head = self.__head.next
            self.__head.prev = None
        self.__autodecrement_length()

    def remove_last(self):
        """Remove the last element of the list"""

        self.__verify_empty()
        if self.__length == 1:
            self.remove_first()
            return
        self.__tail = self.__tail.prev
        self.__tail.next = None
        self.__autodecrement_length()

    def remove_at(self, index: int, /):
        """Remove the element at the specified index"""

        self.__verify_empty()
        self.__verify_index(index, remove=True)
        if index == 0:
            self.remove_first()
            return
        elif index == self.__length - 1:
            self.remove_last()
            return
        self.__autodecrement_length()
        if index < self.__length // 2:
            current = self.__head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            return
        current = self.__tail
        for _ in range(self.__length - 1, index, -1):
            current = current.prev
        current.prev.next = current.next
        current.next.prev = current.prev

    def remove(self, value: Any, /):
        """Remove the first occurrence of the given value"""

        self.__verify_empty()
        if self.__head.value == value:
            self.remove_first()
            return
        elif self.__tail.value == value:
            self.remove_last()
            return
        current = self.__head
        for _ in range(self.__length - 1):
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__autodecrement_length()
                return
            current = current.next
        raise ValueError('Value not found')