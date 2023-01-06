import random

def check_double_zero(*args):
    active = False
    for i in args:
        if i == 0:
            if active:
                return True
            else:
                active = True
        else:
            active = False
    return False
            
def check_double_zero2(aleatorios):
    active = False
    for i in aleatorios:
        if i == 0:
            if active:
                return True
            else:
                active = True
        else:
            active = False
    return False

def check_double_zero3(*args):
    contador = 0
    for i in args:
        if i == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1
    return False

print(check_double_zero3(1, 4, 6, 3, 9, 1, 0, 0, 0, 0, 1, 2, 434, 56, 32))
print(check_double_zero3(1, 4, 6, 3, 9, 1, 0, 60, 50, 70, 1, 2, 434, 56, 32))
print(check_double_zero3(0, 0, 1, 4, 6, 3, 9, 1, 0, 60, 50, 70, 1, 2, 434, 56, 32))
print(check_double_zero3(0, 4, 0, 1, 4, 6, 3, 9, 1, 0, 60, 50, 70, 1, 2, 434, 56, 32))


aleatorios = [random.randint(0,99) for _ in range(1000)]

print(check_double_zero2(aleatorios))