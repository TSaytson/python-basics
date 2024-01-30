import utils
import operations

def main():
  utils.clear_screen()
  utils.header()
  
  account_number = operations.auth_account()
  if account_number:
    utils.clear_screen()
    utils.header()

    option = operations.get_menu_option(account_number)
    operations.select_operation(option, account_number)
  else:
    print('Account not found')

    input('Type <ENTER> to continue')
    
while True:
  main()