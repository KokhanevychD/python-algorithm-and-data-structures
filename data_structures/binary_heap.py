class HeapNode():

    def __init__(self, key, value, right_child=None,
                 left_child=None, parent=None):
        self.key = key
        self.value = value
        self.right_child = right_child
        self.left_child = left_child
        self.parent = parent

    def has_child(self):
        return self.right_child or self.left_child

    def has_both_child(self):
        return self.right_child and self.left_child

    def has_lf_ch(self):
        return self.left_child

    def has_rt_ch(self):
        return self.right_child

    def is_heap(self):
        return self.heap

    def get_only_ch(self):
        if not self.has_both_child():
            if self.has_child():
                return self.right_child or self.left_child
        else:
            return None

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_left_child(self):
        return self.parent and self.parent.left_child == self


class BinaryHeap():

    def __init__(self):
        self.heap = None
        self.size = 0
        self.cmplt_level = []
        self.to_cmplt_level = []
        self.heap_style = 'min'

    def add(self, key, value=None):
        if not self.heap:
            self.heap = HeapNode(key, value)
            self.cmplt_level.append(self.heap)
        else:
            self._add_heap(key, value)
        self.size += 1

    def _add_heap(self, key, value=None):
        new_heap = None
        for node in self.cmplt_level:
            if not node.has_lf_ch():
                node.left_child = HeapNode(key, value, parent=node)
                self.to_cmplt_level.append(node.left_child)
                new_heap = node.left_child
                break
            elif not node.has_rt_ch():
                node.right_child = HeapNode(key, value, parent=node)
                self.to_cmplt_level.append(node.right_child)
                new_heap = node.right_child
                break
        if not new_heap:
            self.cmplt_level, self.to_cmplt_level = self.to_cmplt_level, []
            self._add_heap(key, value)
        else:
            self._perlocation_up(new_heap, new_heap.parent)

    def _perlocation_up(self, child, parent):
        if child.key < parent.key:
            child.key, parent.key = parent.key, child.key
        if child.value:
            child.value, parent.value = parent.value, child.value
        if parent.parent and parent.parent.key > parent.key:
            self._perlocation_up(parent, parent.parent)

    def heap_print(self, level=None):
        next_level = []
        print_list = []
        if self.heap is None:
            print('heap is empty')
            return
        elif not level:
            level = [self.heap]

        for item in level:
            if item.has_lf_ch():
                next_level.append(item.left_child)
            if item.has_rt_ch():
                next_level.append(item.right_child)
            print_list.append(item.key)

        print(print_list)
        if len(next_level) > 0:
            self.heap_print(next_level)

    def reset(self, objct):
        if objct.is_left_child():
            objct.parent.left_child = None
        elif objct.is_right_child():
            objct.parent.right_child = None

    def del_min(self):

        result = self.heap.key
        if self.heap.value:
            result.append(self.heap.value)
        swap = self.to_cmplt_level.pop(-1)
        self.heap.key = swap.key
        if self.heap.value:
            self.heap.value = swap.value
        self.reset(swap)
        self.size -= 1
        if self.cmplt_level == self.to_cmplt_level:
            self.heap = None
            return result
        elif len(self.to_cmplt_level) == 0:
            self.to_cmplt_level = self.cmplt_level
            if self.heap in self.cmplt_level:
                self._del_perlocation(self.heap)
            else:
                self.cmplt_level = []
                for item in self.to_cmplt_level:
                    if item.parent not in self.cmplt_level:
                        self.cmplt_level.append(item.parent)
        self._del_perlocation(self.heap)
        return result

    def _del_perlocation(self, objct):
        if objct.has_both_child():
            if objct.left_child.key <= objct.right_child.key:
                swap_child = objct.left_child
            else:
                swap_child = objct.right_child
        elif objct.has_child():
            swap_child = objct.get_only_ch()
        else:
            return
        if swap_child and objct.key > swap_child.key:
            objct.key, swap_child.key = swap_child.key, objct.key
            self._del_perlocation(swap_child)
        return

    def heap_sort(self, result_list=[]):
        if self.size > 0:
            result_list.append(self.del_min())
            result_list = self.heap_sort(result_list)
        return result_list


key_list = [20, 22, 8, 12, 4, 10, 14]
heap = BinaryHeap()
for key in key_list:
    heap.add(key)
heap.heap_print()
res_heap_sort = heap.heap_sort()
print(res_heap_sort)
heap.heap_print()
