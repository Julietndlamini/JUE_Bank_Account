from random import randint

acc_type = {
        'savings': 11,
        'current': 12,
        }

print('Enter your desired account type')
print('1. savings\n2. current')
userInput = input('Account type: ')
if userInput == '1' or userInput == 'savings':
    accNo = '{}{}'.format(acc_type['savings'], randint(11111110, 99999999))
print(f'congrats!!! your savings account number is {accNo}')
elif userInput == '2' or userInput == 'current':
    accNo = '{}{}'.format(acc_type['current'], randint(11111110, 99999999))
print(f'congrats!!! your current account number is {accNo}')

else:
    print('invalid option, choose 1 for savings or 2 for current')

print('Thank you for choosing JUE bank')
