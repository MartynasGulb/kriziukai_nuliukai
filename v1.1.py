import sys
def tikrinam_ar_laimejo(sarasas,move,zaidejas):
    if 4<move <=9:
        for combination in [(0, 6, 12), (2, 8, 14), (4, 10, 16),
                            (0, 2, 4), (6, 8, 10), (12, 14, 16),
                            (0, 8, 16), (4, 8, 12)]:
            if sarasas[combination[0]] == sarasas[combination[1]] == sarasas[combination[2]]:
                print("Laimejote", zaidejas)
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

def ivestis(zaidejas):
    while True:
        try:
            ivedimas = int(input(f'zaidejas {zaidejas} iveskite kuri skaiciu norite pasirinkiti | 1-9|: '))

            if ivedimas in range(0, 9):
                print()
            else:
                print('Iveskite tinkama skaiciu !')
        except UnboundLocalError:
            print('Tai nera skaicius')
        except:
            print('Tai nera skaicius')

        if ivedimas == 0:
            if dar_karta() == False:
                sys.exit()
            else:
                return True
        return ivedimas

def pakeitimas (ivedimas,sarasas,zaidejas):
    while True:
        try:
            antras = list(sarasas.split())
            antras.remove(str(ivedimas))
        # print(antras)
        # if str(pakeistas)  in antras:
        #     print('nerado tokio')

        except ValueError:
            print('jau panaudotas skaicius ')
            ivedimas = ivestis(zaidejas)
        return sarasas.replace(str(ivedimas),zaidejas)

# def patikrinam(ivedimas,sarasas,zaidejas):

def dar_karta():
    klausimas = input('Ar norite pradeti is naujo?\n Iveskite T/N ')
    atsakymas = klausimas.upper()
    if atsakymas == 'T':
        return True
    elif atsakymas == 'N':
        print('Aciu uz zaidima')
        return False

def botas(zaidejas):
    if zaidejas == 'X':
        print()

def zaidimas():
    move = 0
    zaidejas = 'X'
    sarasas = ('7 8 9\n4 5 6\n1 2 3')
    print(sarasas)
    while True:
        ivedimas = ivestis(zaidejas)
        if ivedimas is True:
            sarasas = ('7 8 9\n4 5 6\n1 2 3')
            move = 0
        move += 1
        sarasas = pakeitimas(ivedimas, sarasas, zaidejas)
        print(sarasas)
        tikrinam = tikrinam_ar_laimejo(sarasas,move,zaidejas)
        if tikrinam is True:
            sarasas = ('7 8 9\n4 5 6\n1 2 3')
            move = 0
        if zaidejas == 'X':
            zaidejas = 'O'
        else:
            zaidejas = 'X'

print('Su kuo norite zaisti? \nRoboto ar Zmogumi?')
su_kuo = input('R- su robotu\nZ-su zmogumi')
print(su_kuo)
# zaidimas()
