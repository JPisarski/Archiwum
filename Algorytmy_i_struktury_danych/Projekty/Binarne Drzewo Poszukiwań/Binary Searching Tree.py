from __future__ import annotations
from typing import Any, List
import graphviz


class BinaryNode:
    value: Any
    left_child: BinaryNode
    right_child: BinaryNode

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> BinaryNode:
        if self.left_child == None:
            return self
        else:
            return self.left_child.min()

    def __str__(self) -> str:
        return f"{self.value}"


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        self.root = self.__insert(self.root, value)

    def __insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node == None:
            node = BinaryNode(value)
        elif node.value > value:
            node.left_child = self.__insert(node.left_child, value)
        else:
            node.right_child = self.__insert(node.right_child, value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for x in list_:
            self.insert(x)

    def contains(self, value: Any) -> bool:
        x: BinaryNode = self.root
        while x != None:
            if x.value == value:
                return True
            elif x.value > value:
                x = x.left_child
            else:
                x = x.right_child
        return False

    def remove(self, value: Any) -> None:
        self.root = self.__remove(self.root, value)

    def __remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        r: BinaryNode = None
        w: BinaryNode = node
        while w.value != value:
            if w.value > value:
                r = w
                w = w.left_child
            else:
                r = w
                w = w.right_child

        if w.left_child == None and w.right_child == None:
            if w == self.root:
                self.root = None
                return None
            if r.left_child != None and r.left_child.value == value:
                r.left_child = None
            else:
                r.right_child = None
            return node

        if w.left_child != None and w.right_child == None:
            if r.left_child != None and r.left_child.value == value:
                r.left_child = w.left_child
            else:
                r.right_child = w.left_child
            return node

        if w.left_child == None and w.right_child != None:
            if r.left_child != None and r.left_child.value == value:
                r.left_child = w.right_child
            else:
                r.right_child = w.right_child
            return node

        if w.left_child != None and w.right_child != None:
            x: BinaryNode = w.right_child
            y: BinaryNode = w
            while x.left_child != None:
                y = x
                x = x.left_child
            if x.left_child == None and x.right_child == None:
                if y.left_child == x:
                    y.left_child = None
                else:
                    y.right_child = None
                w.value = x.value
            else:
                w.value = x.value
                if y.left_child == x:
                    y.left_child = x.right_child
                else:
                    y.right_child = x.right_child
            return node

    def show(self) -> None:
        drzewo = graphviz.Digraph()

        def draw(node: BinaryNode) -> None:
            if node.left_child != None:
                drzewo.node(f"{node.left_child.value}")
                drzewo.edge(f"{node.value}", f"{node.left_child.value}", color="red", label="L", style="dotted")
                draw(node.left_child)
            if node.right_child != None:
                drzewo.node(f"{node.right_child.value}")
                drzewo.edge(f"{node.value}", f"{node.right_child.value}", color="blue", label="R", style="dotted")
                draw(node.right_child)

        if self.root != None:
            drzewo.node(f"{self.root.value}")
            draw(self.root)
        drzewo.render(view=True)


A = BinarySearchTree(BinaryNode(8))
A.insert_list([3, 10, 1, 6, 14, 4, 7, 13])
print(A.contains(7))
A.show()
