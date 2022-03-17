class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None

    def addingNode(self, item):
        NewNode = Node(item)
        if self.head == None:
            self.head = NewNode
            self.tail = NewNode
            return

        self.tail.next = NewNode
        NewNode.prev = self.tail
        self.tail = NewNode

    def length_list(self):
        count = 0
        current_Node = self.head

        while current_Node is not None:
            count = count + 1
            current_Node = current_Node.next
        return count

    def output_List(self):
        current_Node = self.head
        output = []
        while current_Node is not None:
            output.append(current_Node.data)
            current_Node = current_Node.next
        print(output)

    def find_index(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index = index + 1
        return -1

    def deleteNode(self, item_id):
        temp = self.head

        if temp is not None:
            if temp.data == item_id:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == item_id:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return

        prev.next = temp.next

        temp = None

    def insert_after(self, item_id, item):
        if not isinstance(item, Node):
            item = Node(item)
        current_id = 1
        current_node = self.head

        while current_node is not None:
            if current_id == item_id:
                item.prev = current_node
                item.next = current_node.next
                current_node.next.prev = item
                current_node.next = item

            current_node = current_node.next
            current_id = current_id + 1

    def insert_before(self, item_id, item):
        if not isinstance(item, Node):
            item = Node(item)
        current_id = 1
        current_node = self.head

        while current_node is not None:
            if current_id == item_id:
                item.prev = current_node.prev
                item.next = current_node
                current_node.prev.next = item
                current_node.prev = item

            current_node = current_node.next
            current_id = current_id + 1

    def delete_before(self, item_id):
        current_id = 1
        current_node = self.head

        while current_node is not None:
            if current_id == item_id:
                prevnode = current_node.prev
                if prevnode is self.head:
                    self.head = current_node
                    current_node.prev = None
                    return
                prevnode.prev.next = current_node
                current_node.prev = prevnode.prev

            current_node = current_node.next
            current_id = current_id + 1

    def delete_after(self, item_id):
        current_id = 1
        current_node = self.head

        while current_node is not None:
            if current_id == item_id:
                nextNode = current_node.next
                if nextNode.next is not None:
                    nextNode.next.prev = current_node
                current_node.next = nextNode.next
            current_node = current_node.next
            current_id = current_id + 1

    def swapData(self, first, second):
        first.data, second.data = second.data, first.data

    def insertionSortAsc(self):
        front = self.head
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data < back.prev.data:
                back.data, back.prev.data = back.prev.data, back.data
                back = back.prev
            front = front.next

    def insertionSortDesc(self):
        front = self.head
        back = None
        while (front != None):
            back = front.next
            while (back != None and back.prev != None and back.data > back.prev.data):
                self.swapData(back, back.prev)
                back = back.prev
            front = front.next

    def adding_random(self, value):
        # import random
        # length = int(input("Länge?: "))
        # for i in range(length):
        #    input_Node = random.randint(0, 100)
        #    list.addingNode(input_Node)
        for i in range(len(value)):
            input_Node = value[i]
            self.addingNode(input_Node)  # unnötig da list == self

    def output(self):
        print("Länge : %i" % self.length_list())
        self.output_List()

    def delete(self):
        item_id = int(input("Welches Element sollte gelöscht werden?: "))
        self.deleteNode(item_id)
        self.output()

    def search(self):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        print(self.find_index(item_value))

    def insert_before_Node(self):
        item_value = int(input("Welches Element sollte vorher eingefügt werden?: "))
        item_value_before = int(input("Vor welchem Element sollte es eingefügt werden?: "))
        self.insert_before(item_value_before, item_value)
        self.output()

    def insert_after_node(self):
        item_value = int(input("Welches Element sollte ausgewählt werden?: "))
        item_value_after = int(input("Welches Element sollte danach eingefügt werden?: "))
        self.insert_after(item_value, item_value_after)
        self.output()

    def delete_after_node(self):
        item_value = int(input("Welcher Knoten sollte danach entfernt werden: "))
        self.delete_after(item_value)
        self.output()

    def delete_before_node(self):
        item_value = int(input("Welcher Knoten sollte davor entfernt werden: "))
        self.delete_before(item_value)
        self.output()

    def insertionSortAscO(self):
        self.insertionSortAsc()
        self.output()

    def insertionSortDescO(self):
        self.insertionSortDesc()
        self.output()

    def menu(self):
        repeat = True
        answer = None
        while (repeat):
            answer = input("Löschen [l] - Suche [s] - Einfügen nachher [a] - Einfügen davor [b] "
                           "- Knoten danach entfernen [d] - Knoten davor entfernen [v] \n - "
                           "Sortieren ASC [o] - Sortieren DESC [u] - Beenden [any] ").lower()
            if answer == "l":
                self.delete()
            elif answer == "s":
                self.search()
            elif answer == "a":
                self.insert_after_node()
            elif answer == "b":
                self.insert_before_Node()
            elif answer == "d":
                self.delete_after_node()
            elif answer == "v":
                self.delete_before_node()
            elif answer == "o":
                self.insertionSortAscO()
            elif answer == "u":
                self.insertionSortDescO()
            else:
                repeat = False
                print("Verlassen")
