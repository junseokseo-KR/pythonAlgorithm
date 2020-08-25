class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤에 노드 삽입할때
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # 연결리스트를 문자열로 표현
    def __str__(self):
        res_str = "| "

        iterator = self.head

        while iterator is not None:
            res_str += f"{iterator.data} | "
            iterator = iterator.next

        return res_str

    # 해당 인덱스의 노드 검색
    def find_node_at(self,index):
        # 해당 인덱스의 노드 검색
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next

        return iterator

    # 두 노드 사이에 삽입 할때
    def insert_after(self,previous_node,data):
        new_node = Node(data)

        #가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    # 새로운 노드 데이터를 가장 앞에 삽입
    def prepend(self,data):
        new_node = Node(data)

        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head

        self.head = new_node

    # 노드 삭제 메소드
    def del_after(self,previous_node):
        data = previous_node.next.data

        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next

        return data

    # 가장 앞에 노드 삭제
    def pop_left(self):
        data = self.head.data

        if self.head != self.tail:
            self.head = self.head.next
            self.head.next = self.head.next
        else:
            self.head = None
            self.tail = None

        return data

list = LinkedList()

list.append(1)
print(list)
list.prepend(2)
print(list)
node = list.find_node_at(0)
list.insert_after(node, 4)
print(list)
list.del_after(node)
print(list)
list.pop_left()
print(list)
list.pop_left()
print(list)