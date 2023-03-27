def tikrinam_ar_laimejo(sarasas,move):
    if move == 9:
        return False
    for combination in [(0,6,12), (2,8,14), (4,10,16),
                        (0,2,4), (6,8,10), (12,14,16),
                        (0,8,16),(4,8,12)]:
        if sarasas[combination[0]] == sarasas[combination[1]] == sarasas[combination[2]]:

            return True

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
def zaidimas(sarasas):
    move = 0
    zaidejas = 'X'
    print(sarasas)
    while True:
        ivedimas = ivestis(zaidejas)
        move += 1
        sarasas = pakeitimas(ivedimas, sarasas, zaidejas)
        print(sarasas)
        if tikrinam_ar_laimejo(sarasas,move) is True:
            print("Laimejote", zaidejas)
            break
        elif tikrinam_ar_laimejo(sarasas,move) is False:
            print('Lygiosios')
            break


        if zaidejas == 'X':
            zaidejas = 'O'
        else:
            zaidejas = 'X'



Sarasas = ('7 8 9\n4 5 6\n1 2 3')


zaidimas(Sarasas)