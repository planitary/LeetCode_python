import random


class DoubleListNode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    head: DoubleListNode = DoubleListNode()
    tail: DoubleListNode = DoubleListNode()

    # 双链表尾插法
    def append(self, val: int):
        newNode = DoubleListNode(val)
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    # 双链表头插法
    def insert(self, val: int):
        newNode = DoubleListNode(val)
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    # 遍历双链表
    @staticmethod
    def display_linked_list(head: DoubleListNode):
        if head.value is None:
            print("empty linkedlist")
        current_node: DoubleListNode = head
        while current_node is not None:
            if current_node.next is not None:
                print("%d<-->" % current_node.value, end="")
            else:
                print(current_node.value)
            current_node = current_node.next

    # 获取链表长度
    @staticmethod
    def get_size_of_linked_list(head: DoubleListNode) -> int:
        if head.value is None:
            return -1
        current_node: DoubleListNode = head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    # 任意位置插入链表
    def add(self, index: int, value: int):
        linked_list_size: int = DoubleLinkedList.get_size_of_linked_list(self.head)
        if 0 <= index <= linked_list_size:
            # 索引在开头，直接头插法
            if index == 0:
                self.insert(value)
                return
            # 索引在结尾，直接尾插法
            elif index == linked_list_size:
                self.append(value)
                return
            # 其余情况分开讨论，索引在左半边和右半边
            current_node: DoubleListNode = DoubleListNode()
            if index <= (linked_list_size >> 1) - 1:
                current_node = self.head
                while index > 0:
                    current_node = current_node.next
                    index -= 1
            else:
                current_node = self.tail
                i = linked_list_size - 1
                while i > index:
                    current_node = current_node.prev
                    i -= 1
            # 找到当前位置后进行插入，插入位置节点的prev的next（即前一个节点的next）指向新结点，新节点的next指向当前插入位置的节点
            new_node: DoubleListNode = DoubleListNode(value)
            current_node.prev.next = new_node
            new_node.next = current_node

    # 任意位置删除
    def delete(self,index:int):
        linked_size = self.get_size_of_linked_list(self.head)
        if 0 <= index <= linked_size:
            if index >= 0:
                delete_node : DoubleListNode = DoubleListNode()
                # 头部删除
                if index == 0:
                    delete_node = self.head
                    self.head = self.head.next
                    self.head.prev = None
                    delete_node.next = None
                    delete_node.prev = None
                    print("删除的链表节点为:%d" %delete_node.value)
                    return
                # 尾部删除
                if index == linked_size - 1:
                    delete_node = self.tail
                    self.tail = self.tail.prev
                    self.tail.next = None
                    delete_node.prev = None
                    delete_node.next = None
                    print("删除的链表结点为:%d" %delete_node.value)
                    return
                # 任意位置删除
                current_node:DoubleListNode = DoubleListNode()
                if index <= (linked_size >> 1) - 2:
                    current_node = self.head
                    while index > 0:
                        current_node = current_node.next
                        index -= 1
                else:
                    current_node = self.tail
                    j = linked_size - 1
                    while j > index:
                        current_node = current_node.prev
                        j -= 1
                # // 任意位置删除，将该节点的next指针指向空，prev指针指向空，下一个节点的prev指向该结点的上一个节点；
                # // 上一个节点的next指向该节点的下一个节点
                delete_node = current_node
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                delete_node.prev = None
                delete_node.next = None
                print("删除的链表结点为:%d" %delete_node.value)

if __name__ == "__main__":
    d = DoubleLinkedList()
    # 尾插
    for i in range(8):
        value = random.randint(0, 100)
        d.append(value)
        print(value, end=" ")
    print("")
    # 头插
    # for i in range(8):
    #     value = random.randint(0,100)
    #     d.insert(value)
    #     print(value,end=" ")
    # print(" ")
    d.display_linked_list(d.head)
    print("链表长度:%d" % DoubleLinkedList.get_size_of_linked_list(d.head))
    d.delete(6)
    d.display_linked_list(d.head)
    print("链表长度:%d" % DoubleLinkedList.get_size_of_linked_list(d.head))
