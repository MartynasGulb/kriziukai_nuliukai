import sys


def tikrinam_ar_laimejo(sarasas, move, zaidejas, laimetojai):
    if 5 <= move <= 9:
        for combination in [(0, 6, 12), (2, 8, 14), (4, 10, 16),
                            (0, 2, 4), (6, 8, 10), (12, 14, 16),
                            (0, 8, 16), (4, 8, 12)]:
            if sarasas[combination[0]] == sarasas[combination[1]] == sarasas[combination[2]]:
                if zaidejas not in laimetojai:
                    laimetojai[zaidejas] = 1
                else:
                    laimetojai[zaidejas] += 1
                for zaidejas in laimetojai:
                    print(f'Zaidejas {zaidejas} laimejo {laimetojai[zaidejas]} karta/us')
                if dar_karta() == False:
                    sys.exit()
                else:
                    return True
    if move == 9:
        print('lygiosios')
        if dar_karta() == False:
            sys.exit()
        else:
            return True


def laimejimai(laimejimai, zaidejas):
    if zaidejas not in laimejimai:
        laimejimai[zaidejas] = 0
    laimejimai[zaidejas] += 1


def ivestis(zaidejas):
    while True:
        try:
            ivedimas = input(f'zaidejas {zaidejas} iveskite kuri skaiciu norite pasirinkiti | 1-9|: ')
            ivedimas = int(ivedimas)
            if ivedimas in range(1, 10):
                return ivedimas
            elif ivedimas == 0:
                if dar_karta() == False:
                    sys.exit()
                else:
                    return True
            elif 1 > ivedimas or ivedimas > 9.1:
                print('Iveskite tinkama skaiciu !')
            elif ivedimas is not int:
                print('Tai nera skaicius')

        except TypeError:
            print('Tai nera skaicius')
        except ValueError:
            print('Tai nera skaicius')


def pakeitimas(ivedimas, sarasas, zaidejas):
    while True:
        try:
            antras = list(sarasas.split())
            antras.remove(str(ivedimas))
        except ValueError:
            print('jau panaudotas skaicius ')
            ivedimas = ivestis(zaidejas)
        else:
            return sarasas.replace(str(ivedimas), zaidejas)


def dar_karta():
    klausimas = input('Ar norite pradeti is naujo?\n Iveskite T/N ')
    atsakymas = klausimas.upper()
    if atsakymas == 'T':
        return True
    elif atsakymas == 'N':
        print('Aciu uz zaidima')
        return False


def zaidimas():
    move = 0
    zaidejas = 'X'
    sarasas = ('7 8 9\n4 5 6\n1 2 3')
    print(sarasas)
    laimetojai = {'X': 0, 'O': 0}
    while True:
        ivedimas = ivestis(zaidejas)
        if ivedimas is True:
            sarasas = ('7 8 9\n4 5 6\n1 2 3')
            move = 0
        move += 1
        sarasas = pakeitimas(ivedimas, sarasas, zaidejas)
        print(sarasas)
        tikrinam = tikrinam_ar_laimejo(sarasas, move, zaidejas, laimetojai)
        if tikrinam is True:
            sarasas = ('7 8 9\n4 5 6\n1 2 3')
            print(sarasas)
            move = 0
        if zaidejas == 'X':
            zaidejas = 'O'
        else:
            zaidejas = 'X'


zaidimas()
