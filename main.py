def check_double_zero(*args):
    active = False
    for i in args:
        if i == 0:
            if active == True:
                return True
            else:
                active = True
        else:
            active = False
    return False
            


print(check_double_zero(1, 4, 6, 3, 9, 1, 0, 0, 0, 0, 1, 2, 434, 56, 32))
print(check_double_zero(1, 4, 6, 3, 9, 1, 0, 60, 50, 70, 1, 2, 434, 56, 32))
print(check_double_zero(0, 0, 1, 4, 6, 3, 9, 1, 0, 60, 50, 70, 1, 2, 434, 56, 32))
print(check_double_zero(0, 4, 0, 1, 4, 6, 3, 9, 1, 0, 60, 50, 70, 1, 2, 434, 56, 32))