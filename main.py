# 0 1 2
# 3 4 5
# 6 7 8


def tikrinam(S):
    if S[0] == S[3] == S[6]:
        print("Laimejote")
    if S[1] == S[4] == S[7]:
        print("Laimejote")
    if S[2] == S[5] == S[8]:
        print("Laimejote")
    if S[0] == S[1] == S[2]:
        print("Laimejote")
    if S[3] == S[4] == S[5]:
        print("Laimejote")
    if S[6] == S[7] == S[8]:
        print("Laimejote")
    if S[0] == S[4] == S[8]:
        print("Laimejote")
    if S[2] == S[4] == S[6]:
        print("Laimejote")

Sarasas = ('7 8 9 \n4 5 6 \n1 2 3')


while True:
    ivedimas = int(input('iveskite pasirinkima: '))
    tikrinam(Sarasas)
    match ivedimas:
        case 1:
            Sarasas = Sarasas.replace('1', 'X')
            print(Sarasas)
        case 2:
            Sarasas = Sarasas.replace('2', 'X')
            print(Sarasas)
        case 3:
            Sarasas = Sarasas.replace('3', 'X')
            print(Sarasas)
        case 4:
            Sarasas = Sarasas.replace('4', 'X')
            print(Sarasas)
        case 5:
            Sarasas = Sarasas.replace('5', 'X')
            print(Sarasas)
        case 6:
            Sarasas = Sarasas.replace('6', 'X')
            print(Sarasas)
        case 7:
            Sarasas = Sarasas.replace('7', 'X')
            print(Sarasas)
        case 8:
            Sarasas = Sarasas.replace('8', 'X')
            print(Sarasas)
        case 9:
            Sarasas = Sarasas.replace('9', 'X')
            print(Sarasas)
        case 0:
            print('Aciu uz zaidima')
            break