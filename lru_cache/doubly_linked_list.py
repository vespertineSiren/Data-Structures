"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        node = ListNode(value, None, None)
        if not self.head and not self.tail:
          self.head = node
          self.tail = node
        else:
          node.next = self.head
          self.head.prev = node
          self.head = node
          self.length += 1

    def remove_from_head(self):
        remove = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            self.head.pre.delete()
            self.length -= 1
        return remove

    def add_to_tail(self, value):
        next = ListNode(value, self.tail)
        if not self.head and not self.tail:
            self.head = next
            self.tail = next
            self.head.prev = None
            self.head.next = None
            self.length = 1
        else:
            self.tail.next = next
            self.tail = next
            self.length += 1

    def remove_from_tail(self):
        removed = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.tail = self.tail.prev
            self.tail.next.delete()
            self.length -= 1
        return removed

    def move_to_front(self, node):
        self.add_to_head(node)
        self.length -= 1

    def move_to_end(self, node):
        if self.length > 1 and node is not self.tail:
            self.tail.insert_after(node.value)
            self.tail = self.tail.next
        if node == self.head:
            self.head = node.next
        node.delete()

    def delete(self, node):
        if node == self.head:
            if node.next:
                self.head = node.next
                self.head.prev = None
            else:
                self.head = None
        if node == self.tail:
            self.tail = None
        self.length -= 1

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
