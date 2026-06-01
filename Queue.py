class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class DoublyNode:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def put(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def get(self):
        if self.is_empty():
            return None

        target_data = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.count -= 1
        return target_data


class Stack:

    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pull(self):
        if self.is_empty():
            return None

        target_data = self.top.value
        self.top = self.top.next
        self.count -= 1
        return target_data


class Deque:

    def __init__(self):
        self.left = None
        self.right = None
        self.count = 0

    def is_empty(self):
        return self.left is None

    def Lput(self, data):
        new_node = DoublyNode(data)
        if self.is_empty():
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
        self.count += 1

    def Rput(self, data):
        new_node = DoublyNode(data)
        if self.is_empty():
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
        self.count += 1

    def Lget(self):
        if self.is_empty():
            return None

        target_data = self.left.value
        self.left = self.left.next

        if self.left is None:
            self.right = None
        else:
            self.left.prev = None

        self.count -= 1
        return target_data

    def Rget(self):
        if self.is_empty():
            return None

        target_data = self.right.value
        self.right = self.right.prev

        if self.right is None:
            self.left = None
        else:
            self.right.next = None

        self.count -= 1
        return target_data


if __name__ == "__main__":
    print(" \033[31mChecking the queue:\033[0m ")
    q = Queue()
    for i in range(10):
        q.put(i)
    print(f"Empty? {q.is_empty()}")
    for _ in range(10):
        print(q.get(), end=" ")
    print(f"\nEmpty? {q.is_empty()}\n")

    print(" \033[31mChecking the stack:\033[0m ")
    s = Stack()
    for i in range(10):
        s.push(i)
    print(f"Empty? {s.is_empty()}")
    for _ in range(10):
        print(s.pull(), end=" ")
    print(f"\nEmpty? {s.is_empty()}\n")

    print(" \033[31mChecking the deck:\033[0m ")
    d = Deque()
    for i in range(10):
        d.Rput(i)
        d.Lput(i)
    print(f"Empty? {d.is_empty()}")
    for _ in range(10):
        print(f"R:{d.Rget()} L:{d.Lget()}", end=" | ")
    print(f"\nEmpty? {d.is_empty()}")