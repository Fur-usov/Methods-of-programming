import random
import csv
import datetime
from datetime import datetime
import time
import matplotlib as plt
import numpy as np

class Ship:
    """Класс для работы с объектами класса 'Корабль'
    Имеет 5 полей:
    - название корабля (name)
    - дата постройки (date)
    - страна постройки (country)
    - тип корабля (ship_type)
    - имя капитана (captain)
     """
    def __init__(self, name, date, country, ship_type, captain):
        self.name = name
        self.date = date
        self.country = country
        self.ship_type = ship_type
        self.captain = captain

    def __lt__(self, other):
        return (self.date, self.name, self.ship_type) < (other.date, other.name, other.ship_type)

    def __gt__(self, other):
        return (self.date, self.name, self.ship_type) > (other.date, other.name, other.ship_type)

    def __ge__(self, other):
        return (self.date, self.name, self.ship_type) >= (other.date, other.name, other.ship_type)

    def __le__(self, other):
        return (self.date, self.name, self.ship_type) <= (other.date, other.name, other.ship_type)

    def __eq__(self, other):
        return (self.date, self.name, self.ship_type) == (other.date, other.name, other.ship_type)

    def pr(self):
        print(f"{self.name}, {self.date}, {self.country}, {self.ship_type}, {self.captain}", end="")
        print()


class TreeNode:
    def __init__(self, value=None, content=None):
        self.left = None
        self.right = None
        self.value = value
        self.content = content

    def insert(self, value, content=None):
        if self.value is None:
            self.value = value
            self.content = content
        elif value < self.value:
            if self.left is None:
                self.left = TreeNode(value, content)
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value, content)
            else:
                self.right.insert(value, content)

    def traversal(self):
        if self.left:
            self.left.traversal()
        print(self.value, self.content)
        if self.right:
            self.right.traversal()

    def find(self, value):
        if value < self.value:
            if self.left is None:
                raise Exception('error, node content is None')
                # return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                raise Exception('error, node content is None')
                # return None
            else:
                return self.right.find(value)
        else:
            return self.content


class RBNode:
    def __init__(self, val, content=None):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None
        self.content = content


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val, content=None):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val, content)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent

                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)

        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr.content is None:
            raise Exception('error, node content is None')
        else:
            return curr.content

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        print(node.val, node.content)
        print_tree(node.right, lines, level + 1)


def get_nums(num):
    random.seed(1)

    nums = []

    for _ in range(num):
        nums.append(random.randint(1, num - 1))

    return nums


class HashTable:
    __collisions = 0

    def __init__(self, n=100):
        self.MAX = n
        self.arr = [[] for i in range(self.MAX)]

    def __get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        hsh = self.__get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hsh]):
            if len(element) == 2 and element[0] == key:
                self.arr[hsh][idx] = (key, value)
                found = True
                break
        if not found and len(self.arr[hsh]) > 0:
            self.arr[hsh].append((key, value))
            self.__collisions += 1
        elif not found:
            self.arr[hsh].append((key, value))

    def __getitem__(self, key):
        hsh = self.__get_hash(key)
        for element in self.arr[hsh]:
            if element[0] == key:
                return element[1]

        raise Exception(f"No {key} key in HashTable")

    def __delitem__(self, key):
        hsh = self.__get_hash(key)
        for idx, element in enumerate(self.arr[hsh]):
            if element[0] == key:
                del self.arr[hsh][idx]

    def get_collisions_number(self):
        print(self.__collisions)

    def pr(self):
        for i in self.arr:
            print(i)


with open('Data_1.csv') as file:
    next(file)
    row_count = sum(1 for row in file)
    file.seek(0)
    next(file)
    tree_1 = TreeNode()
    rb_tree_1 = RBTree()
    table_1 = HashTable(row_count)
    for row in file:
        r = row.split(",")
        w = Worker(r[0], r[1], r[2], int(r[3]))
        tree_1.insert(value=r[0], content=w)
        rb_tree_1.insert(val=r[0], content=w)
        table_1[r[0]] = w


tree_1.find('Пётр Волков').get_info()
rb_tree_1.exists('Пётр Волков').get_info()
# print(rb_tree_1)
table_1['Пётр Волков'].get_info()
table_1.get_collisions_number()
# table_1.pr()
