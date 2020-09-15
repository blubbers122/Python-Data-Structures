class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def add_node(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            self.get_last_node(self.root).next = node

    def get_last_node(self, curr):
        if curr.next:
            return self.get_last_node(curr.next)
        return curr

    def reverse_list(self):
        curr = self.root
        prev = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        self.root = prev
        print('list was reversed.')

    def search_for_node(self, node):
        curr = self.root
        #traverses list to find provided node
        while curr != node:
            if not curr:
                print("that node doesn't exist in this list.")
                return
            curr = curr.next

        return curr

    def search_for_value(self, value):
        curr = self.root
        
        #traverses list to find provided node
        while curr and curr.value != value:
            curr = curr.next

        if not curr:
            print("that value doesn't exist in this list.")
            return

        return curr.value

    def delete_root(self):
        new_root = self.root.next
        if new_root:
            self.root = new_root
        else:
            self.root = None

    def del_node(self, node_to_delete):
        if not self.root:
            print("the list is empty.")
            return
        if self.root == node_to_delete:
            self.delete_root()
            return

        curr = self.root
        while curr.next != node_to_delete:
            if not curr.next:
                print("that node doesn't exist in this list.")
                return
            curr = curr.next
        curr.next = node_to_delete.next
        print("deleting node with value %s" % node_to_delete.value)
        del node_to_delete


    def print_list(self):
        if not self.root:
            print("no list to print")
            return
        curr = self.root
        while curr:
            print(curr.value)
            curr = curr.next


linked_list = LinkedList()
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(7)
linked_list.add_node(8)
linked_list.add_node(90)
linked_list.print_list()
print(linked_list.search_for_value(7))
print(linked_list.search_for_value(4))
print(linked_list.search_for_value(90))
print(linked_list.search_for_value(1))
linked_list.del_node(linked_list.root)
linked_list.reverse_list()
linked_list.del_node(linked_list.root)
linked_list.print_list()
