# -*- coding: utf-8 -*-

# skrypt zwraca roznice w minutach miedzy 2 godzinami

godziny = 24
minuty = 60
doba = minuty * godziny

def htom(godz, min):    # funkcja przelicza godz na min
    godz = (godz * minuty) + min
    godz = doba - godz
    return godz     # zwraca minuty

print("Pierwsza godzina: ")     # pobranie pierwszej godziny
godz_a = int(input())

print("minut: ")
min_a = int(input())

print("Druga godzina: ")    # pobranie drugiej godziny
godz_b = int(input())

print("minut: ")
min_b = int(input())

godz_a = htom(godz_a, min_a)    # wywolanie funkcji dla pierwszej godziny
godz_b = htom(godz_b, min_b)    # wywolanie funkcji dla drugiej godziny


print("wynik: %d"% (godz_a - godz_b))   # wypisanie wyniku

