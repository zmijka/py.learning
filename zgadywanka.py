import random


def wylosuj():
    losowa = random.randrange(1, 10)

    return losowa


# main #
if __name__ == "__main__":

    while True:

        print("Podaj liczbę: ")
        liczba = int(input())

        losowa = wylosuj()

        if liczba == losowa:
            print(f"Zgadłeś!!!! - wylosowana liczba to: {losowa}")
        else:
            print(f"Nie zgadłeś!!!! - wylosowana liczba to: {losowa}")
