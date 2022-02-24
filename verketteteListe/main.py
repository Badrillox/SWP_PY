class Knoten:
    def __init__(self, daten):
        self.prev = None
        self.daten = daten
        self.next = None
        return

    def besitzt_Wert(self, wert):
        if self.daten == wert:
            return True
        else:
            return False


class verketteListe:
    def __init__(self):
        self.Kopf = None
        # self.Pfad = None
        return

    def add_element_toList(self, item):
        if not isinstance(item, Knoten):
            item = Knoten(item)
        if self.Kopf is not None:
            last_node = self.Kopf
            while last_node.next is not None:
                last_node = last_node.next

            item.prev = last_node
            last_node.next = item
        else:
            self.Kopf = item
        return
        # if self.Kopf is None:
        #   self.Kopf = item
        # else:
        #   self.Pfad.next = item
        #
        # self.Pfad = item
        # return

    def list_lenght(self):
        count = 0
        derzeitiger_Knoten = self.Kopf
        while derzeitiger_Knoten is not None:
            count = count + 1
            derzeitiger_Knoten = derzeitiger_Knoten.next
        return count

    def list_output(self):
        derzeitiger_Knoten = self.Kopf
        ausgabe = []
        while derzeitiger_Knoten is not None:
            ausgabe.append(derzeitiger_Knoten.daten)
            derzeitiger_Knoten = derzeitiger_Knoten.next
        print(ausgabe)

    def ungeordnete_Suche(self, value):
        derzeitiger_Knoten = self.Kopf
        Knoten_Id = 1
        ergebnis = []

        while derzeitiger_Knoten is not None:
            if derzeitiger_Knoten.besitzt_Wert(value):
                ergebnis.append(Knoten_Id)
            derzeitiger_Knoten = derzeitiger_Knoten.next
            Knoten_Id = Knoten_Id + 1

        return ergebnis

    def remove_element(self, item_id):
        current_id = 1
        derzeitiger_Knoten = self.Kopf
        Knoten_davor = None

        while derzeitiger_Knoten is not None:
            if current_id == item_id:
                if Knoten_davor is not None:
                    Knoten_davor.next = derzeitiger_Knoten.next
                else:
                    self.head = derzeitiger_Knoten.next
                    return

            Knoten_davor = derzeitiger_Knoten
            derzeitiger_Knoten = derzeitiger_Knoten.next
            current_id = current_id + 1

        return

    def add_random(self):
        import random
        lenght = int(input("Länge?: "))
        for i in range(lenght):
            Knoten_input = random.randint(0, 100)
            list.add_element_toList(Knoten_input)

    def ausgabe(self):
        print("Länge : %i" % list.list_lenght())
        list.list_output()

    def remove(self):
        item_id = int(input("Welches Element sollte gelöscht werden?: "))
        list.remove_element(item_id)
        self.ausgabe()

    def searching(self):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        print(list.ungeordnete_Suche(item_value))

    def insertAfter(self, item_id, item):
        if not isinstance(item, Knoten):
            item = Knoten(item)
        current_id = 1
        current_node = self.Kopf

        while current_node is not None:
            if current_id == item_id:
                item.prev = current_node
                item.next = current_node.next
                current_node.next.prev = item
                current_node.next = item

            current_node = current_node.next
            current_id = current_id + 1
        return

    def insertBefore(self,item_id, item):
        if not isinstance(item, Knoten):
            item = Knoten(item)
        current_id = 1
        current_node = self.Kopf

        while current_node is not None:
            if current_id == item_id:
                item.prev = current_node.prev
                item.next = current_node
                current_node.prev.next = item
                current_node.prev = item

            current_node = current_node.next
            current_id = current_id + 1
        return

    def deleteAfter(self,item_id):
        current_id = 1
        current_node = self.Kopf

        while current_node is not None:
            if current_id == item_id:
                nextnode = current_node.next
                if nextnode.next is not None:
                    nextnode.next.prev = current_node
                current_node.next = nextnode.next

            current_node = current_node.next
            current_id = current_id + 1
        return

    def deleteBefore(self,item_id):
        current_id = 1
        current_node = self.Kopf

        while current_node is not None:
            if current_id == item_id:
                prevnode = current_node.prev
                if prevnode is self.Kopf:
                    self.Kopf = current_node
                    current_node.prev = None
                    return
                prevnode.prev.next = current_node
                current_node.prev = prevnode.prev

            current_node = current_node.next
            current_id = current_id + 1
        return

    def menu(self):
        repeat = True
        answer = None
        while (repeat):
            answer = input("Löschen [l] - Suche [s] - Beenden [any]").lower()
            if answer == "l":
                self.remove()
            elif answer == "s":
                self.searching()
            else:
                repeat = False
                print("Verlassen")


class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class dopple_kette:
    def __init__(self):
        self.head = None

    def insert(self, new_Node):
        if self.head:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

            new_Node.prev = last_node
            last_node.next = new_Node


if __name__ == '__main__':
    list = verketteListe()
    list.add_random()
    list.ausgabe()
    #list.deleteBefore(2)
    #list.ausgabe()
    list.menu()
