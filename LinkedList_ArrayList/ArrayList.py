from array import array


class ArrayList():
    def __init__(self):
        # self.value = None
        self.arr = []

    def adding_elem(self, val):
        for i in range(len(val)):
            self.arr.append(val[i])

    def delete(self, item):
        self.arr.pop(item)
        print("Element wurde gelöscht")

    def search(self, item):
        for i in range(len(list)):
            if self.arr[i] == item:
                print("Element existiert in der Liste: " + str(i))

    def output(self):
        print("Länge : %i" % self.length_list())
        print(self.arr)

    def length_list(self):
        return int(len(self.arr))

    def insertBefore(self, item, item_id):
        for i in range(len(self.arr)):
            if i == item_id:
                self.arr.insert(item_id - 1, item)

    def insertAfter(self, item_id, item):
        for i in range(len(self.arr)):
            if i == item_id:
                self.arr.insert(item_id + 1, item)

    def deleteBefore(self, number):
        for i in range(len(self.arr)):
            if i == number:
                self.arr.pop(number - 1)

    def deleteAfter(self, number):
        for i in range(len(self.arr)):
            if i == number:
                self.arr.pop(number + 1)

    def sortAsc(self):
        arr = self.arr
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def sortDesc(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key > self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def insertionSortAscO(self):
        self.sortAsc()
        self.output()

    def insertionSortDescO(self):
        self.sortDesc()
        self.output()

    def delete_elem(self):
        item_id = int(input("Welches Element sollte gelöscht werden?: "))
        self.delete(item_id)
        self.output()

    def search_elem(self):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        self.search(item_value)

    def insert_before_Node(self):
        item_value = int(input("Vor welchem Element sollte es eingefügt werden?: "))
        item_value_before = int(input("Welches Element sollte vorher eingefügt werden?: "))
        self.insertBefore(item_value_before, item_value)
        self.output()

    def insert_after_node(self):
        item_value = int(input("Welches Element sollte ausgewählt werden?: "))
        item_value_after = int(input("Welches Element sollte danach eingefügt werden?: "))
        self.insertAfter(item_value, item_value_after)
        self.output()

    def delete_after_node(self):
        item_value = int(input("Welches Element sollte danach entfernt werden: "))
        self.deleteAfter(item_value)
        self.output()

    def delete_before_node(self):
        item_value = int(input("Welches Element sollte davor entfernt werden: "))
        self.deleteBefore(item_value)
        self.output()

    def menu(self):
        repeat = True
        answer = None
        while (repeat):
            answer = input("Löschen [l] - Suche [s] - Einfügen nachher [a] - Einfügen davor [b] "
                           "- Element danach entfernen [d] \n - Element davor entfernen [v] - "
                           "Sortieren ASC [o] - Sortieren DESC [u] - Beenden [any] ").lower()
            if answer == "l":
                self.delete_elem()
            elif answer == "s":
                self.search_elem()
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
