#!/usr/bin/python3
# 100-singly_linked_list.py
"""Define Node & SinglyLinkedList classes"""


class Node:
    """Definition of Node class"""

    def __init__(self, data, next_node=None):
        """Function to initialise Node fields"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data field"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data field"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next_node field"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node field"""
        if (not isinstance(value, Node) and
                value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Definition of SinglyLinkedList class"""

    def __init__(self):
        """Function to initialise SinglyLinkedList field"""
        self.__head = None

    def __str__(self):
        """Function to define the format of the printable object"""
        list_data = []
        current = self.__head
        while current is not None:
            list_data.append(str(current.data))
            current = current.next_node
        return ('\n'.join(list_data))

    def sorted_insert(self, value):
        """Function that inserts a new Node into the correct
        sorted position in the list
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new
