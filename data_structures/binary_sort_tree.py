
class TreeNode():

    def __init__(self, key, value, right_child=None,
                left_child=None, parent=None):
        self.key = key
        self.value = value
        self.right_child = right_child
        self.left_child = left_child
        self.parent = parent

    def has_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_child(self):
        return self.is_left_child() or self.is_right_child()

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child and self.left_child)

    def has_child(self):
        return self.right_child or self.left_child

    def has_both_child(self):
        return self.right_child and self.left_child

    def _only_child(self):
        if not self.has_both_child():
            if self.has_left_child():
                return self.left_child
            return self.right_child


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def add_element(self, key, value):
        if self.root:
            self._add_element(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _add_element(self, key, value, cur_node):
        if cur_node.key > key:
            if cur_node.has_left_child():
                self._add_element(key, value, cur_node.left_child)
            else:
                cur_node.left_child = TreeNode(key, value, parent=cur_node)
        elif cur_node.key == key:
            cur_node.value = value
        else:
            if cur_node.has_right_child():
                self._add_element(key, value, cur_node.right_child)
            else:
                cur_node.right_child = TreeNode(key, value, parent=cur_node)

    def __setitem__(self, key, value):
        self.add_element(key, value)

    def tree_search(self, key):
        if self.root:
            result = self._tree_search(key, self.root)
            if result:
                return result
            print('No elemen with such key')
        print('The BT is empty!')

    def _tree_search(self, key, cur_node):
        if key < cur_node.key and cur_node.has_left_child():
            return self._tree_search(key, cur_node.left_child)
        elif key == cur_node.key:
            return cur_node
        elif cur_node.has_right_child():
            return self._tree_search(key, cur_node.right_child)
        return None

    def __getitem__(self, key):
        return self.tree_search(key).value

    def __contains__(self, key):
        return self.tree_search(key) is not None

    def print_tree(self, order='preorder'):
        if self.root:
            if order == 'preorder':
                order = self._preorder(self.root, [])
            elif order == 'in_order':
                order = self._in_order(self.root, [])
            elif order == 'post_order':
                order = self._post_order(self.root, [])
            for item in order:
                print('Key:', item.key, 'Value:', item.value)
        else:
            print('Tree is empty')

    def _preorder(self, cur_node, res_list=[]):
        # preorder traversal, returns objects

        res_list.append(cur_node)
        if cur_node.has_both_child():
            res_list = self._preorder(cur_node.left_child, res_list)
            res_list = self._preorder(cur_node.right_child, res_list)
        elif cur_node.has_left_child():
            res_list = self._preorder(cur_node.left_child, res_list)
        elif cur_node.has_right_child():
            self._preorder(cur_node.right_child, res_list)
        return res_list

    def _in_order(self, cur_node, res_list):
        # in order raversal, returns objects

        if cur_node.has_left_child():
            res_list = self._in_order(cur_node.left_child, res_list)
        res_list.append(cur_node)
        if cur_node.has_right_child():
            res_list = self._in_order(cur_node.right_child, res_list)
        return res_list

    def _post_order(self, cur_node, res_list):
        # post order raversal, returns objects

        if cur_node.has_left_child():
            res_list = self._post_order(cur_node.left_child, res_list)
        if cur_node.has_right_child():
            res_list = self._post_order(cur_node.right_child, res_list)
        res_list.append(cur_node)
        return res_list

    def pop_element(self, key):
        object = self._tree_search(key, self.root)
        if object:
            return self._pop_element(object)
        return None

    def _pop_element(self, object):
        # internal func for object poping, wich replace connections and return deleted object
        # free root deletion block
        if object.is_root() and not object.has_child():
            self.root = None
            self.size -= 1
            return object

        # leaf deletion block
        elif object.is_leaf():
            if object.is_left_child():
                object.parent.left_child = None
            else:
                object.parent.right_child = None
            self.size -= 1
            return object

        # has one child deletion block
        elif object.has_child() and not object.has_both_child():
            child = object._only_child()
            if object.is_left_child():
                child.parent, object.parent.left_child = object.parent, child
            else:
                child.parent, object.parent.right_child = object.parent, child
            self.size -= 1
            return object

        # has both child deletion block
        elif object.has_both_child():
            # successor search
            successor = self._pop_element(self._successor(object, object.right_child))
            # swap object with successor
            if object.is_left_child():
                object.parent.left_child = successor
            elif object.is_root():
                self.root = successor
            else:
                object.parent.right_child = successor
            if object.has_right_child():
                object.right_child.parent, successor.right_child = successor, object.right_child
            object.left_child.parent, successor.left_child = successor, object.left_child
            return object

    def _successor(self, object, child, successor=None):
        # recursion to find smalest successor bigger than object
        # skip nodes with both childs:
        if child.has_both_child():
            successor = self._successor(object, child.left_child, successor)
        elif not successor:
            successor = child
        elif child.key < successor.key:
            successor = child
        elif child.has_child():
            successor = self._successor(object, child._only_child(), successor)
        return successor

    def lc_ancestor(self, key_1, key_2):
        obj_1 = self._tree_search(key_1, self.root)
        obj_2 = self._tree_search(key_2, self.root)
        if obj_1.is_root() or obj_2.is_root():
            return self.root
        return self._lca(obj_1, obj_2, [])

    def _lca(self, obj_1, obj_2, trvsl_list):
        if obj_1 in trvsl_list:
            return obj_1
        elif obj_1 is obj_2:
            return obj_1
        else:
            trvsl_list.append(obj_1)
            if obj_1.is_child():
                obj_1 = obj_1.parent
        if obj_2 in trvsl_list:
            return obj_2
        else:
            trvsl_list.append(obj_2)
            if obj_2.is_child():
                obj_2 = obj_2.parent
        return self._lca(obj_1, obj_2, trvsl_list)


if __name__ == '__main__':

    tree_key_list = [20, 22, 8, 12, 4, 10, 14]
    tree_value_list = list(range(10))
    tree = BinarySearchTree()
    for key, item in zip(tree_key_list, tree_value_list):
        tree[key] = item
    print('preorder tree traversal:')
    tree.print_tree()
    print('_____')
    print('in order tree traversal:')
    tree.print_tree(order="in_order")
    print('post order traversal:')
    tree.print_tree(order='post_order')
