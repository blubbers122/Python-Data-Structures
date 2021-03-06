class node:
    def __init__(self, value=None):
        self.value=value
        self.count=1
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self, value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            cur_node.count += 1

    def print_tree(self):
        if self.root != None:
            print("tree:")
            self._print_tree(self.root)
        else:
            print("no tree to print")

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            if cur_node.count > 1:
                print(str(cur_node.value) + " x " + str(cur_node.count))
            else:
                print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def print_reverse_tree(self):
        if self.root != None:
            print("reverse tree:")
            self._print_reverse_tree(self.root)
        else:
            print("no tree to print")

    def _print_reverse_tree(self, cur_node):
        if cur_node != None:
            self._print_reverse_tree(cur_node.right)
            if cur_node.count > 1:
                print(str(cur_node.value) + " x " + str(cur_node.count))
            else:
                print(str(cur_node.value))
            self._print_reverse_tree(cur_node.left)

    def get_sum_in_range(self, L, R):
        sum = 0
        def dfs(node):
            if node:
                if L <= node.value <= R:
                    nonlocal sum
                    sum += node.value
                if L < node.value:
                    dfs(node.left)
                if R > node.value:
                    dfs(node.right)

        dfs(self.root)
        return sum

    # def build_from_sorted_array(self, nums):
    #     self.root = self._build_from_sorted_array(nums)
    #
    # def _build_from_sorted_array(self, nums):
    #     if not nums: return None
    #     middle_index = len(nums) >> 1
    #     root = node(nums[middle_index])
    #     print(str(root.value))
    #     root.left = self.build_from_sorted_array(nums[:middle_index])
    #     root.right = self.build_from_sorted_array(nums[middle_index + 1:])
    #     return root

    def delete_tree(self):
        pass

bst = BST()
bst.build_from_sorted_array([1,2,3,4,5,6,7,8,9,10,11,34,45,56,78,788])
bst.print_tree()
