from .node import Node
from .exception import Empty
from typing import Any


class Stack:
    """
    A simple LIFO (Last In, First Out) stack implementation using linked nodes.

    Attributes:
        __top (Node | None): The top node of the stack.
        __length (int): Number of elements in the stack.
    """

    def __init__(self):
        """Initialize an empty stack"""

        self.__top = None
        self.__length = 0

    def __autoincrement_length(self):

        self.__length += 1

    def __autodecrement_length(self):

        self.__length -= 1

    def __verify_empty(self):
        """
        Check if the stack is empty.

        Raises:
            Empty: If the stack has no elements.
        """
        if self.__length == 0:
            raise Empty('Stack is empty')

    def __normalize_index(self, index: int, /):
        """
        Normalize a possibly negative index to a valid positive index.

        Args:
            index (int): The index to normalize.

        Returns:
            int: Normalized positive index.

        Raises:
            IndexError: If the index is out of bounds.
        """

        index = index if index >= 0 else self.__length + index
        if self.__length <= index or index < 0:
            raise IndexError('Index out of range')
        return index

    def __iter__(self):
        """Iterate over stack elements from top to bottom"""

        current = self.__top
        while current:
            yield current
            current = current.next

    def __getitem__(self, item):
        """Return the element at the given index"""

        self.__verify_empty()
        item = self.__normalize_index(item)
        current = self.__top
        for _ in range(item):
            current = current.next
        return current.value

    def __setitem__(self, key, value):
        """Set the element at the given index to a new value"""

        self.__verify_empty()
        key = self.__normalize_index(key)
        current = self.__top
        for _ in range(key):
            current = current.next
        current.value = value

    def push(self, value: Any, /):
        """
        Add a new element to the top of the stack.

        Args:
            value (Any): The value to push onto the stack.
        """

        if self.__length == 0:
            self.__top = Node(value)
            self.__autoincrement_length()
            return
        new_node = Node(value)
        new_node.next = self.__top
        self.__top = new_node
        self.__autoincrement_length()

    def pop(self) -> Any:
        """
        Remove and return the top element of the stack.

        Returns:
            Any: The value of the removed top element.

        Raises:
            Empty: If the stack is empty.
        """

        self.__verify_empty()
        current = self.__top
        self.__top = self.__top.next
        self.__autodecrement_length()
        return current.value

    def peek(self) -> Any:
        """
        Return the value of the top element without removing it.

        Returns:
            Any: The value of the top element.

        Raises:
            Empty: If the stack is empty.
        """

        self.__verify_empty()
        return self.__top.value