class TreeNode:
    def __init__(self, parent=None, r_child=None, l_child=None, value=None):
        self.parent = parent
        self.r_child = r_child
        self.l_child = l_child
        self.value = value

    def has_r_ch(self):
        return self.r_child != None

    def has_l_ch(self):
        return self.l_child != None


class Solution:
    def __init__(self, root=None):
        self.root = None
        self.repetition = []

    def build_tree(self, inp_list):
        for item in inp_list:
            if self.root is None:
                self.root = TreeNode(value=item)
            else:
                self._build_tree(self.root, item)
        return

    def _build_tree(self, current_node, item):
        if current_node.value < item:
            if current_node.has_r_ch():
                self._build_tree(current_node.r_child, item)
            else:
                current_node.r_child = TreeNode(
                    parent=current_node, value=item)
        elif current_node.value > item:
            if current_node.has_l_ch():
                self._build_tree(current_node.l_child, item)
            else:
                current_node.l_child = TreeNode(
                    parent=current_node, value=item)
        elif current_node.value == item:
            if item not in self.repetition:
                self.repetition.append(item)

    def findDuplicates(self, nums, res=[]):
        self.build_tree(nums)
        return self.repetition


res = Solution().findDuplicates([])
print(res)

res = Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
print(res)

res = Solution().findDuplicates([10, 2, 5, 10, 9, 1, 1, 4, 3, 7])
print(res)
