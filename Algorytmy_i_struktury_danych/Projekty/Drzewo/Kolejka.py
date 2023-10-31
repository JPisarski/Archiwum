from typing import Any


class Node:
    value: Any
    next: "Node"

    def __init__(self, value: Any = None, next: "Node" = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    head: "Node"
    tail: "Node"

    def __init__(self, head: "Node" = None, tail: "Node" = None) -> None:
        self.head = head
        self.tail = tail

    def __str__(self) -> str:
        x = ""
        if self.head != None:
            n = self.head.next
            x += f"{n.value}"
            while True:
                n = n.next
                if n == None:
                    break
                x += f" -> {n.value}"
        return x

    def __len__(self) -> int:
        l = 0
        if self.head != None:
            n = self.head
            while n.next != None:
                n = n.next
                l += 1
        return l

    def push(self, value: Any) -> None:
        if self.head == None:
            self.head = Node(next=Node(value))
            self.tail = Node(next=self.head.next)
        else:
            self.head.next = Node(value, self.head.next)

    def append(self, value: Any) -> None:
        if self.tail == None:
            self.tail = Node(next=Node(value))
            self.head = Node(next=self.tail.next)
        else:
            self.tail.next.next = Node(value)
            self.tail.next = self.tail.next.next

    def node(self, at: int) -> Node:
        w = 0
        n = self.head.next
        while w < at:
            n = n.next
            w += 1
        return n

    def insert(self, value: Any, after: Node) -> None:
        n = self.head
        while n != after:
            n = n.next
        if n.next != None:
            n.next = Node(value, n.next)
        else:
            n.next = Node(value)
            self.tail.next = n.next

    def pop(self) -> Any:
        if self.head == self.tail:
            w = self.head.next
            self.head.next = None
            self.tail.next = None
        else:
            w = self.head.next
            self.head.next = w.next
        return w

    def remove_last(self) -> Any:
        if self.head == self.tail:
            w = self.head.next
            self.head.next = None
            self.tail.next = None
        else:
            w = self.tail.next
            x = self.head
            while x.next.next != None:
                x = x.next
            x.next = None
        return w

    def remove(self, after: Node) -> Any:
        n = self.head
        while n != after:
            n = n.next
        if n.next.next == None:
            n.next = n.next.next
            self.tail.next = n
        else:
            n.next = n.next.next


class Queue(LinkedList):
    _storage: "LinkedList"

    def __int__(self) -> None:
        self._storage = LinkedList()

    def __str__(self) -> str:
        x = ""
        if self.head != None:
            n = self.head.next
            x += f"{n.value},"
            while True:
                n = n.next
                if n == None:
                    break
                x += f" {n.value},"
        return f"{x[0:-1]}"

    def __len__(self):
        return super().__len__()

    def peek(self) -> Any:
        return self.head.next.value

    def enqueue(self, element: Any) -> None:
        super().append(element)

    def dequeue(self) -> Any:
        return (super().pop()).value
