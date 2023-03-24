# 0 1 2
# 3 4 5
# 6 7 8




# a = int(input('iveskite skaiciu'))
def tikrinam():
    if sarasas[0] == sarasas[3] == sarasas[6]:
        print("Laimejote")
    if sarasas[1] == sarasas[4] == sarasas[7]:
        print("Laimejote")
    if sarasas[2] == sarasas[5] == sarasas[8]:
        print("Laimejote")
    if sarasas[0] == sarasas[1] == sarasas[2]:
        print("Laimejote")
    if sarasas[3] == sarasas[4] == sarasas[5]:
        print("Laimejote")
    if sarasas[6] == sarasas[7] == sarasas[8]:
        print("Laimejote")
    if sarasas[0] == sarasas[4] == sarasas[8]:
        print("Laimejote")
    if sarasas[2] == sarasas[4] == sarasas[6]:
        print("Laimejote")




Sarasas = ('7 8 9 \n4 5 6 \n1 2 3')
sarasas = Sarasas

while True:
    ivedimas = int(input('iveskite pasirinkima: '))

    match ivedimas:
        case 1:
            sarasas = sarasas.replace('1', 'X')
            print(sarasas)
        case 2:
            sarasas = sarasas.replace('2', 'X')
            print(sarasas)
        case 3:
            sarasas = sarasas.replace('3', 'X')
            print(sarasas)
        case 4:
            sarasas = sarasas.replace('4', 'X')
            print(sarasas)
        case 5:
            sarasas = sarasas.replace('5', 'X')
            print(sarasas)
        case 6:
            sarasas = sarasas.replace('6', 'X')
            print(sarasas)
        case 7:
            sarasas = sarasas.replace('7', 'X')
            print(sarasas)
        case 8:
            sarasas = sarasas.replace('8', 'X')
            print(sarasas)
        case 9:
            sarasas = sarasas.replace('9', 'X')
            print(sarasas)
        case 0:
            break

