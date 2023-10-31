from typing import Any, List, Callable, Union
from Kolejka import Queue
import graphviz


class TreeNode:
    value: Any
    children: List["TreeNode"]

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if self.children == []:
            return True
        else:
            return False

    def add(self, child: "TreeNode") -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[["TreeNode"], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[["TreeNode"], None]) -> None:
        visit(self)
        fifo: "Queue" = Queue()
        for x in self.children:
            fifo.enqueue(x)
        while len(fifo) > 0:
            visit(fifo.peek())
            for y in fifo.peek().children:
                fifo.enqueue(y)
            fifo.dequeue()

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        fifo: "Queue" = Queue()
        for x in self.children:
            fifo.enqueue(x)
        while len(fifo) > 0:
            if fifo.peek().value == value:
                return fifo.peek()
            for y in fifo.peek().children:
                fifo.enqueue(y)
            fifo.dequeue()
        return None

    def __str__(self) -> str:
        return self.value


class Tree:
    root: "TreeNode"

    def __init__(self, root: "TreeNode") -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.add(TreeNode(value=value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self):
        drzewo = graphviz.Digraph()

        def dodaj(g: "TreeNode") -> None:
            for x in g.children:
                drzewo.node(f"{x.value}")
                drzewo.edge(f"{g.value}", f"{x.value}")

        drzewo.node(f"{self.root.value}")
        dodaj(self.root)
        fifo: "Queue" = Queue()
        for x in self.root.children:
            fifo.enqueue(x)
        while len(fifo) > 0:
            dodaj(fifo.peek())
            for y in fifo.peek().children:
                fifo.enqueue(y)
            fifo.dequeue()
        drzewo.render(view=True)


F = TreeNode("F")
Drzewo_1 = Tree(F)
B = TreeNode("B")
G = TreeNode("G")
F.add(B)
F.add(G)
A = TreeNode("A")
D = TreeNode("D")
B.add(A)
B.add(D)
C = TreeNode("C")
E = TreeNode("E")
D.add(C)
D.add(E)
I = TreeNode("I")
G.add(I)
H = TreeNode("H")
I.add(H)

# # sprawdzanie metod
# print(F.is_leaf())
# print()
# print(E.is_leaf())
# print()
# B.for_each_deep_first(print)
# print()
# B.for_each_level_order(print)
# print()
# print(F.search("N"))
# print()
# print(F.search("E"))
# print()
# Drzewo_1.add("J", F)
# Drzewo_1.for_each_level_order(print)
# print()
# Drzewo_1.for_each_deep_first(print)

Drzewo_1.show()


