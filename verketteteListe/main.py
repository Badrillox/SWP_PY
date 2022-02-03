class Knoten:
    def __init__(self, daten):
        self.daten = daten
        self.naechste = None
        return
        
    def besitzt_Wert(self,wert):
        if self.daten == wert:
            return True
        else:
            return False

class verketteListe:
    def __init__(self):
        self.Kopf = None
        self.Pfad = None
        return
    
    def add_element_toList(self, item):
        if not isinstance(item, Knoten):
            item = Knoten(item)
        
        if self.Kopf is None:
            self.Kopf = item
        else:
            self.Pfad.naechste = item
        
        self.Pfad = item
        return
    
    def list_lenght(self):
        count = 0
        derzeitiger_Knoten = self.Kopf
        
        while derzeitiger_Knoten is not None:
            count = count +1
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
        return count
        
    def list_output(self):
        derzeitiger_Knoten = self.Kopf
        ausgabe = []
        while derzeitiger_Knoten is not None:
            ausgabe.append(derzeitiger_Knoten.daten)
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
        print(ausgabe)

    def ungeordnete_Suche(self, value):
        derzeitiger_Knoten = self.Kopf
        Knoten_Id = 1
        ergebnis = []
        
        while derzeitiger_Knoten is not None:
            if derzeitiger_Knoten.besitzt_Wert(value):
                ergebnis.append(Knoten_Id)
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_Id = Knoten_Id +1
        
        return ergebnis
    
    def remove_element(self, item_id):
        current_id = 1
        derzeitiger_Knoten = self.Kopf
        Knoten_davor = None

        while derzeitiger_Knoten is not None:
            if current_id == item_id:
                if Knoten_davor is not None:
                    Knoten_davor.naechste = derzeitiger_Knoten.naechste
                else:
                    self.head = derzeitiger_Knoten.naechste
                    return

            Knoten_davor = derzeitiger_Knoten
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            current_id = current_id + 1

        return
        
    def add_random(self):
        import random
        lenght = int(input("Länge?: "))
        for i in range(lenght):
            Knoten_input = random.randint(0,100)
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

    def menu(self):
        repeat = True
        answer = None
        while(repeat):
            answer = input("Löschen [l] - Suche [s] - Beenden [any]").lower()
            if answer == "l":
                self.remove()
            elif answer == "s":
                self.searching()
            else:
                repeat = False
                print("Verlassen")
                

if __name__ == '__main__':
    list = verketteListe()
    list.add_random()
    list.ausgabe()
    
    list.menu()
