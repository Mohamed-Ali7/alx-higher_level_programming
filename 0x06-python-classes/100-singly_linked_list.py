#!\usr\bin\python3

"""This module contains a class which is a Node of a singly linnked list"""


class Node:

    """This class represents a node of a singly linked list

    Attribute:
        data (int): Is the data of the node of integer type

        next_node (Node): Is a pointer to a node to
        refere to the next element in the linked list
    """

    def __init__(self, data, next_node=None):
        """This method initializes the node

        Args:
            data (int): the value that will be assigned to the data of the node

            next_node (node): Is a pointer to a node to
            refere to the next element in the linked list
        """

        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node

    @property
    def data(self):
        """This method return the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """This method sets the data of the node by assigning value to it

        Args:
            value (int): The value the will be assigned to the data of the node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This method return the next node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This method sets the next node of the node by assigning value to it

        Args:
            value (Node): The value the will be assigned
            to the next node of the node
        """

        if type(value) is not Node:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list

    Attributes:
        head (Node): Refers to the first node of the linked list
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        cur = self.__head
        prev = self.__head

        if not self.__head:
            self.__head = new_node
            return
        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        while cur:
            if cur.data > value:
                prev.next_node = new_node
                new_node.next_node = cur
                break
            prev = cur
            cur = cur.next_node
        if not cur:
            prev.next_node = new_node

    def __str__(self):
        temp = self.__head
        result = ""
        while temp:
            result += str(temp.data)
            temp = temp.next_node
            if temp:
                result += "\n"

        return result
