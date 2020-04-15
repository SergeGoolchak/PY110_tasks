import numpy as np
print("Привет! Это игра крестики-нолики!")

def func_repeat(y, t):
    for i in y:
        if t == i:
            t = 100
    return t

def func_move(x):
    try:
        if x % 2 == 0:
            sim = "O"
        else:
            sim = "X"
        choise = int(input("Введите номер поля для хода "))
        choise = func_repeat(bank, choise)
        bank.append(choise)
        if 0 < choise < 10:
            for i in pground:
                for j in range(len(i)):
                    if i[j] == str(choise):
                        i[j] = sim
        else:
            print("Введено не корректное значение")
            choise = int(input("Введите номер поля для хода "))
            for i in pground:
                for j in range(len(i)):
                    if i[j] == str(choise):
                        i[j] = sim
        print(pground)
    except Exception as ex:
        print("Введено не корректное значение")
        choise = int(input("Введите номер поля для хода "))
        for i in pground:
            for j in range(len(i)):
                if i[j] == str(choise):
                    i[j] = sim
        print(pground)
    return pground, bank

def func_control():
    d = 1
    if pground[0][0] == pground[0][1] == pground[0][2]:
        d = 0
        print(pground[0][0], " WIN ")
    if pground[1][0] == pground[1][1] == pground[1][2]:
        d = 0
        print(pground[1][0], " WIN ")
    if pground[2][0] == pground[2][1] == pground[2][2]:
        d = 0
        print(pground[2][0], " WIN ")
    if pground[0][0] == pground[1][0] == pground[2][0]:
        d = 0
        print(pground[0][0], " WIN ")
    if pground[0][1] == pground[1][1] == pground[2][1]:
        d = 0
        print(pground[0][1], " WIN ")
    if pground[0][2] == pground[1][2] == pground[2][2]:
        d = 0
        print(pground[0][2], " WIN ")
    if pground[0][0] == pground[1][1] == pground[2][2]:
        d = 0
        print(pground[0][0], " WIN ")
    if pground[0][2] == pground[1][1] == pground[2][0]:
        d = 0
        print(pground[0][2], " WIN ")
    else:
        pass
    return d

pground = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
print(pground)
bank = []
step = 1
d = 1
while d == 1:
    func_move(step)
    step += 1
    d = func_control()
    if d == 0:
        break
    if step > 9:
        print("Победила дружба")
        break


