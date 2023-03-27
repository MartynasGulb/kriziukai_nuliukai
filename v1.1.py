def tikrinam_ar_laimejo(sarasas,move,zaidejas):
    if move !=9:
        for combination in [(0, 6, 12), (2, 8, 14), (4, 10, 16),
                            (0, 2, 4), (6, 8, 10), (12, 14, 16),
                            (0, 8, 16), (4, 8, 12)]:
            if sarasas[combination[0]] == sarasas[combination[1]] == sarasas[combination[2]]:
                print("Laimejote", zaidejas)
                return dar_karta()

    elif move == 9:   #todo kad jeigu visi
        print('lygiosios')
        return dar_karta()


def ivestis(zaidejas):
    while True:
        try:
            ivedimas = int(input(f'zaidejas {zaidejas} iveskite kuri skaiciu norite pasirinkiti | 1-9|: '))
            if ivedimas in range(0, 10):
                return ivedimas

            else:
                print('Iveskite tinkama skaiciu !')
        except:
            print('Tai nera skaicius')

def pakeitimas (ivedimas,sarasas,zaidejas):
     return sarasas.replace(str(ivedimas),zaidejas)

def dar_karta():
    klausimas = input('Ar norite zaisti dar karta?\n Iveskite T/N ')
    atsakymas = klausimas.upper()
    if atsakymas == 'T':
        move = 0
        return True
    elif atsakymas == 'N':
        print('Aciu uz zaidima')
        return False

def zaidimas():
    move = 0
    zaidejas = 'X'
    sarasas = ('7 8 9\n4 5 6\n1 2 3')
    print(sarasas)
    while True:
        ivedimas = ivestis(zaidejas)
        move += 1
        sarasas = pakeitimas(ivedimas, sarasas, zaidejas)
        print(sarasas)
        if tikrinam_ar_laimejo(sarasas,move,zaidejas) is True:
            sarasas = ('7 8 9\n4 5 6\n1 2 3')
            move = 0

        elif tikrinam_ar_laimejo(sarasas,move,zaidejas) is False:
            break



        if zaidejas == 'X':
            zaidejas = 'O'
        else:
            zaidejas = 'X'



zaidimas()
# move = 0
# zaidejas = 'X'
# sarasas = ('1 8 9\n1 5 6\n1 2 3')
#
# tikrinam_ar_laimejo(sarasas,move,zaidejas)