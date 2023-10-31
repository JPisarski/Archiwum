# zadanie_1

from typing import Any

from typing import Any


class Node:
    value: Any
    next: "Node"

    def __init__(self, value: Any = None, next: "Node" = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head: "Node" = None, tail: "None" = None) -> None:
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
        if  self.tail == None:
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


list_ = LinkedList()
assert list_.head == None
print(list_)

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
print(list_)

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'
print(list_)

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
print(list_)
print(len(list_))

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element == returned_first_element
print(list_)

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element == returned_last_element
assert str(list_) == '1 -> 5 -> 9'
print(list_)

second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'
print(list_)

# zadanie 2


class Stack(LinkedList):
    _storage: "LinkedList"

    def __int__(self, _storage: "LinkedList" = None) -> None:
        self._storage = _storage

    def __str__(self) -> str:
        x = ""
        if self.head != None:
            n = self.head.next
            x += f"{n.value} \n"
            while True:
                n = n.next
                if n == None:
                    break
                x += f"{n.value}\n"
        return x

    def __len__(self) -> int:
        return super().__len__()

    def push(self, element: Any) -> None:
        super().append(element)

    def pop(self) -> Any:
        return (super().remove_last()).value


stack = Stack()
assert len(stack) == 0
print()
print(stack)
print(len(stack))

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
print()
print(stack)
print(len(stack))

top_value = stack.pop()
assert top_value == 1
print()
print(stack)
print(len(stack))

assert len(stack) == 2
print()
print(stack)
print(len(stack))

# zadanie 3


class  Queue(LinkedList):
    _storage: "LinkedList"

    def __int__(self, _storage: "LinkedList" = None) -> None:
        self._storage = _storage

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
        return self._storage.head.next.value

    def enqueue(self, element: Any) -> None:
        super().append(element)

    def dequeue(self) -> Any:
        return (super().pop()).value


queue = Queue()
print(queue)

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue)
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
print(queue)
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
