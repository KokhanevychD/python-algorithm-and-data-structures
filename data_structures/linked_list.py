class listNode:
    def __init__(self, data, key=None):
        self.data = data
        self.key = key
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.end = None

    def printList(self):
        temp = self.head
        while temp:
            print('this is key:')
            print(temp.key)
            print('this is data:')
            print(temp.data)
            print('______________')
            temp = temp.next

    def addElement(self, data, key=None):
        if self.head is None:
            if key is None:
                self.head = listNode(data, 0)
            else:
                self.head = listNode(data, key)

        elif self.end is None:
            if key is None:
                self.end = listNode(data, 1)
            else:
                self.end = listNode(data, key)
            self.head.next = self.end
        else:
            if key is None:
                self.end.next = listNode(data, self.end.key + 1)
            else:
                self.end.next = listNode(data, key)
            self.end = self.end.next

    def Key_ll(self, key, data=True):
        temp = self.head
        while temp:
            if key == temp.key:
                if data is not True:
                    return temp
                return temp.data
            temp = temp.next
        return 'No element with such key: ' + str(key)

    def Data_ll(self, data, key=True):
        temp = self.head
        while temp:
            if data == temp.data:
                if key is not True:
                    return temp
                return temp.key
            temp = temp.next
        return 'No element with such data: ' + str(data)

    def Pop_ll(self, key):
        obj = self.Key_ll(key, False)
        prev_obj = self.Key_ll(key - 1, False)
        prev_obj.next = obj.next
        key_changer = obj.next
        while key_changer:
            key_changer.key -= 1
            key_changer = key_changer.next
        return obj.data

    def Insert_ll(self, key, data):
        obj = self.Key_ll(key, False)
        prev_obj = self.Key_ll(key - 1, False)
        prev_obj.next = listNode(data, key)
        prev_obj.next.next = obj
        key_changer = obj
        while key_changer:
            key_changer.key += 1
            key_changer = key_changer.next

    def Swap_ll(self, key_1, key_2):
        obj_1 = self.Key_ll(key_1, False)
        obj_2 = self.Key_ll(key_2, False)
        obj_1.data, obj_2.data = obj_2.data, obj_1.data


l_list = LinkedList()
value_list = ['data1', 'data2', 'data3', 'data4', 'data5']
for item in value_list:
    l_list.addElement(item)

print('Elements added to the LinkedList')
l_list.printList()

print("Element's key found by data")
print(l_list.Data_ll('data4'))

print("Element's data found by key")
print(l_list.Key_ll(1))

new_elem = 10
l_list.Insert_ll(3, new_elem)
print('Element added to the list with key 3:')
l_list.printList()

get_elem = l_list.Pop_ll(3)
print('element with key 3 poped from list:')
l_list.printList()
print("this element's data:")
print(get_elem)

l_list.Swap_ll(3, 4)
print('swaped 3d and 4s elements data:')
l_list.printList()
