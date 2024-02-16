import utils
import operations
import file
from bank_data import accounts_list

def main():
  file.load_bank_data()
  utils.clear_screen()
  utils.header()
  print(accounts_list)
  account_number = operations.auth_account()
  if account_number:
    utils.clear_screen()
    utils.header()

    option = operations.get_menu_option(account_number)
    operations.select_operation(option, account_number)
  else:
    print('Account not found')

    input('Type <ENTER> to continue')
    
if __name__ == '__main__':
  while True:
    main()