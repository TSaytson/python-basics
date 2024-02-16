import getpass
from bank_data import accounts_list, money_slips, money_slips_user
import file

def auth_account() -> str:
  account_number = input("Enter your account number: ")
  account_password = getpass.getpass("Enter your account password: ")

  if account_number in accounts_list and account_password == accounts_list[account_number]['password']:
    return account_number
  else:
    return False

def get_menu_option(account_number):
    print("Choose one of the options below:")
    print("1 - Balance")
    print("2 - Withdraw")
    if accounts_list[account_number]['admin']:
      print("7 - Insert banknotes")
    return input()

def select_operation(option, account_number):
  if option == '1':
    show_balance(account_number)
  elif option == '2':
    withdraw()
  elif option == '7' and accounts_list[account_number]['admin']:
    insert_money_slips()

def show_balance(account_number):
  print('Your balance is: ', accounts_list[account_number]['balance'])
  press_to_continue()

def get_slips(value, slip_value) -> int:
  input('in get_slips')
  print(value)
  if value // slip_value > 0 and value // slip_value <= money_slips[str(slip_value)]:
    money_slips_user[str(slip_value)] = value // slip_value
    print(f'inside if {slip_value}, value: {value}')
    return (value//slip_value)*slip_value
  else:
    return 0
  
def withdraw():
  value = int(input('Type the value to be withdrawn: '))
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
    file.save_money_slips()
    print("You can pick up your bank notes")
    print(money_slips_user)
    press_to_continue()

def insert_money_slips():
  amount = input('How many banknotes: ')
  print(money_slips.keys())
  note_value = input('Kind of banknote: ')
  money_slips[note_value] += int(amount)
  print(money_slips)
  press_to_continue()

def press_to_continue():
  input('Type <ENTER> to continue')