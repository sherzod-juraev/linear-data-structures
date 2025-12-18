from operator import index
from typing import Any


class Node:

    def __init__(self, value, /):

        self.value = value
        self.next = None

class SinglyLinkedList:

    def __init__(self):

        self.__head = None
        self.__length = 0

    def __normalize_index(self, index: int, /) -> int:

        if index >= self.__length:
            raise IndexError('Indeks tashqarisiga murojaat')
        index = index if index >= 0 else self.__length + index
        return index

    def __autoincrement_length(self):

        self.__length += 1

    def __verify_index(self, index: int, /, *, remove: bool = False):

        if self.__length < index or index < 0:
            raise IndexError('Indeks xatosi')
        if remove and index == self.__length:
            raise IndexError('Indeks xatosi')

    def __iter__(self):

        self.__current = self.__head
        return self

    def __next__(self):

        if self.__current is not None:
            val, self.__current = self.__current.value, self.__current.next
            return val
        else:
            raise StopIteration

    def __getitem__(self, item):

        item = self.__normalize_index(item)
        for ind, val in enumerate(self):
            if item == ind:
                return val

    def __setitem__(self, key, value):

        key = self.__normalize_index(key)
        current, ind = self.__head, 0
        while current is not None:
            if ind == key:
                current.value = value
                return None
            current = current.next
            ind += 1

    def prepend(self, value, /):
        """boshiga qoshish"""

        new_node = Node(value)
        self.__autoincrement_length()
        if self.__head is not None:
            new_node.next = self.__head
        self.__head = new_node

    def append(self, value: Any, /):
        """oxiriga qoshish"""

        current = self.__head
        self.__autoincrement_length()
        if current is None:
            self.__head = Node(value)
            return None
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def insert_at(self, index: int, value: Any, /):
        """indeks boyicha qoshish"""

        self.__verify_index(index)
        current, ind = self.__head, -1
        while index != ind + 1:
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        self.__autoincrement_length()

    def remove_first(self):
        """boshidan ochirish"""

        if self.__head is None:
            raise

    def remove_last(self):
        """oxiridan ochirish"""

        pass

    def remove_at(self, index, /):
        """indeks boyicha"""

        pass

    def remove(self, value, /):
        """birinchi uchragan qiymatni ochirish"""

        pass



l = SinglyLinkedList()
l.prepend(1)
print(l[0])
l.prepend(2)
print(l[0], 'l1= ', l[1])