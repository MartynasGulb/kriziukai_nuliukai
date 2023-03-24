# def tikrinam_ar_laimejo(S,z):
#     if S[0] == S[6] == S[12]:
#         print("Laimejote", z)
#         return 1
#     if S[2] == S[8] == S[14]:
#         print("Laimejote", z)
#         return 1
#     if S[4] == S[10] == S[16]:
#         print("Laimejote", z)
#         return 1
#     if S[0] == S[2] == S[4]:
#         print("Laimejote", z)
#         return 1
#     if S[6] == S[8] == S[10]:
#         print("Laimejote", z)
#         return 1
#     if S[12] == S[14] == S[16]:
#         print("Laimejote", z)
#         return 1
#     if S[0] == S[8] == S[16]:
#         print("Laimejote", z)
#         return 1
#     if S[4] == S[8] == S[12]:
#         print("Laimejote", z)
#         return 1
#     return 0

def tikrinam_ar_laimejo(S, z):
    for combination in [(0, 6, 12), (2, 8, 14), (4, 10, 16), (0, 2, 4), (6, 8, 10), (12, 14, 16), (0, 8, 16), (4, 8, 12)]:
        if S[combination[0]] == S[combination[1]] == S[combination[2]]:
            print("Laimejote", z)
            return 1
def pas(t, s,z):
    if t(s,z) == 1:
        a = input('ar norite zaisti dar karta t/n: ')
        if a == 't':
            return Sarasas == ('7 8 9\n4 5 6\n1 2 3')
        elif a == 'n':
            print('Paspauskite "0" jei tikrai norite baigti')
            return s


Sarasas = ('7 8 9\n4 5 6\n1 2 3')
print(Sarasas)

zaidejas = 'X'
while True:
    while True:
        try:
            ivedimas = int(input('iveskite kuri skaiciu norite pasirinkiti | 1-9|: '))
            if ivedimas in range(0, 10):
                break
            else:
                print('Iveskite tinkama skaiciu !')
        except:
            print('Tai nera skaicius')

    Sarasas = Sarasas.replace(str(ivedimas), zaidejas)
    match ivedimas:
        case 1:
            Sarasas = Sarasas.replace('1', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)

        case 2:
            Sarasas = Sarasas.replace('2', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)
        case 3:
            Sarasas = Sarasas.replace('3', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)

        case 4:
            Sarasas = Sarasas.replace('4', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)
        case 5:
            Sarasas = Sarasas.replace('5', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)
        case 6:
            Sarasas = Sarasas.replace('6', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)
        case 7:
            Sarasas = Sarasas.replace('7', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)
        case 8:
            Sarasas = Sarasas.replace('8', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)
        case 9:
            Sarasas = Sarasas.replace('9', zaidejas)
            tikrinam_ar_laimejo(Sarasas, zaidejas)
            print(Sarasas)
            pas(tikrinam_ar_laimejo, Sarasas,zaidejas)
        case 0:
            print('Aciu uz zaidima')
            break
    if zaidejas == 'X':
        zaidejas = 'O'
    else:
        zaidejas = 'X'
