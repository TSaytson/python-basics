import getpass
import os

def header():
  print('****************************************')
  print("****************MT - ATM****************")
  print('****************************************')

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def get_slips(value, slip_value) -> int:
  print(value)
  if value // slip_value > 0 and value // slip_value <= money_slips[str(slip_value)]:
    money_slips_user[str(slip_value)] = value // slip_value
    print(f'inside if {slip_value}, value: {value}')
    return (value//slip_value)*slip_value
  else:
    return 0

money_slips = {
  '2' : 5,
  '5': 5,
  '10': 5,
  '20' : 5,
  '50' : 5,
  '100': 5,
  '200': 5
}

accounts_list = {
  '0001-01' : {
    'password': '1234',
    'name': 'Thiago Saytson',
    'balance': 370028030,
    'admin': False
  },
  '0001-02' : {
    'password' : '1234',
    'name': 'Mariana Silva de Carvalho',
    'balance' : 82380402,
    'admin' : False
  },
  '0001-00' : {
    'password' : 'fofis',
    'name' : 'Domzinho Saytson Carvalho',
    'balance' : 1000000000000,
    'admin' : True
  }
}

option = ''

while option.lower() != 's':
  clear_screen()
  header()
  account_number = input("Enter your account number: ")
  account_password = getpass.getpass("Enter your account password: ")

  if account_number in accounts_list and account_password == accounts_list[account_number]['password']:
    clear_screen()
    header()
    
    print("1 - Balance")
    print("2 - Withdraw")
    if accounts_list[account_number]['admin']:
      print("7 - Insert banknotes")
    print("s - Exit")
    option = input()
    if option == '1':
      print('Your balance is', accounts_list[account_number]['balance'])
    elif option == '2':
      value = int(input('Type the value to be withdrawn: '))
      money_slips_user = {}
      value -= get_slips(value, 200)
      value -= get_slips(value, 100)
      value -= get_slips(value, 50)
      value -= get_slips(value, 20)
      value -= get_slips(value, 10)
      value -= get_slips(value, 5)
      value -= get_slips(value, 2)

      if value != 0:
        print('This value cannot be withdrawn')
      else:
        for money_bill in money_slips_user:
          money_slips[money_bill] -= money_slips_user[money_bill]
        print("You can pick up your bank notes")
        print(money_slips_user)
    elif option == '7' and accounts_list[account_number]['admin']:
      amount = input('How many banknotes: ')
      print(money_slips.keys())
      note_value = input('Kind of banknote: ')
      money_slips[note_value] += int(amount)
      print(money_slips)
  else:
    print('Account not found')
  if option.lower() != 's':
    print('Type <ENTER> to continue or <s> to exit')
    option = input()
    
