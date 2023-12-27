# ===================== CODE TO FIX ============================
# balance = 945.70
#
# num = input('Deposit: ')
#
# balance += num
# print(f'Balance is {balance}')
# ===================================================

balance = 945.70
while True:
    try:
        num = float(input('Deposit: '))
        break
    except ValueError:
        print('Input must be a number')

balance += num
print(f'Balance is {balance}')