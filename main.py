class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head

        if self.head is None:
            new_node.next = new_node
        else:
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node

        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        temp = self.head

        while temp is not None:
            temp = temp.next

            if temp.next == self.head:
                temp.next = new_node
                break

        new_node.next = self.head

    def add_after(self, prev_node,data):
        new_node = Node(data)
        temp = self.head

        if prev_node is None:
            print('There is no node in this circular linked list')
            return

        while temp is not None:
            temp = temp.next

            if temp == prev_node:
                new_node.next = temp.next
                temp.next = new_node
                break

    def print(self):
        head = self.head

        if self.head is None:
            print('The circular linked list is empty')
            return

        while head is not None:
            print(f'{head.data}')
            head = head.next

            if head == self.head:
                break


if __name__ == '__main__':
    cllist = CircularLinkedList()
    cllist.push(12)
    cllist.push(56)
    cllist.push(2)
    cllist.push(11)
    cllist.append(7)
    cllist.add_after(cllist.head.next, 8)
    cllist.print()
