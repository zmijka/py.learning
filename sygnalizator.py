class Sygnalizator():

    listaSwiatel = {"zielone": 0, "pomaranczowe": 0, "czerwone": 0}

    def zapal(self, kolor):

        if kolor == 1:
            self.listaSwiatel["zielone"] = self.listaSwiatel["zielone"] + 1
            print("Zapalono swiatlo zielone:", self.listaSwiatel["zielone"], "razy")

        elif kolor == 2:
            self.listaSwiatel["pomaranczowe"] = self.listaSwiatel["pomaranczowe"] + 1
            print("Zapalono swiatlo pomaranczowe:", self.listaSwiatel["pomaranczowe"], "razy")

        elif kolor == 3:
            self.listaSwiatel["czerwone"] = self.listaSwiatel["czerwone"] + 1
            print("Zapalono swiatlo czerwone:", self.listaSwiatel["czerwone"], "razy")

        elif kolor == 4:
            print("Statystyki: ")
            for s in (self.listaSwiatel.keys()):
                print("Zapalono swiatlo", s, self.listaSwiatel[s], "razy")
        else:
            print("zly wybor", kolor)


swiatlo = Sygnalizator()

while True:
    print("Podaj liczbe: 1 - zielone, 2 - pomaranczowe, 3 - czerwone ")

    x = input()             # pobranie liczby jako string
    x = int(x)              # zmiana liczby ze string na int

    swiatlo.zapal(x)
