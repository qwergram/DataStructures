class Node(object):

    def __init__(self, value, child=None):
        """Initialize a new Node Object."""
        self.value = value
        self.child = child
        self._size = 1

    def insert(self, value):
        """Define a new value to add to the linked list."""
        if self.child:
            self._size += 1
            self.child.insert(value)
        else:
            self._size += 1
            self.child = Node(value)

    def remove(self, value):
        """Specify the value to remove from the linked list.

        This method will remove the first instance and only the first
        instance it finds of the value specified.

        You also cannot remove an item from a list containing only one item.
        """
        if self.value == value:
            try:
                self.value = self.child.value
                self.child = self.child.child
                self._size -= 1
                return True
            except AttributeError:
                return False
        elif self.child:
            if self.child.value == value:
                self.child = self.child.child
                self._size -= 1
                return True
            else:
                return self.child.remove(value)
        else:
            return False

    def pop(self):
        """Remove the first item in the list and return the value."""
        try:
            value = self.value
            self.value, self.child = self.child.value, self.child.child
            self._size -= 1
            return value
        except AttributeError:
            return

    def size(self):
        """Return the number of items in the linked list."""
        return self._size

    __len__ = size

    def search(self, value):
        """Return a node containing the value specified if it exists."""
        if self.value == value:
            return self
        elif self.child:
            return self.child.search(value)
        else:
            return False

    def __contains__(self, value):
        return bool(self.search(value))

    def display(self):
        """Return a string representation of the linked list."""
        string = "["
        cursor = self
        while cursor:
            string += "({})>".format(cursor.value)
            try:
                cursor = cursor.child
            except AttributeError:
                break
        return string[:-1] + ']'

    __str__ = display
