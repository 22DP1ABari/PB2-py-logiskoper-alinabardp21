def parbaudit(n:float):
    if n > 3.9:
        return True
    else:
        return False

user_input = float(input())
if parbaudit(user_input):
    print('Atrodas diapazonā')
