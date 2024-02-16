from utils import header
from file import open_bank_file, write_money_slips, write_bank_accounts


def create_money_slips(mode:str):
  file = open_bank_file(mode)
  write_money_slips(file)
  file.close()
  print("Money slips successfully stored")

def create_bank_accounts(mode:str):
  file = open_bank_file(mode)
  write_bank_accounts(file)
  file.close()
  print("Bank accounts successfully stored")

def main():
  header()
  create_money_slips('w')
  file = open_bank_file('a')
  file.write('\n')
  file.close()
  create_bank_accounts('a')

main()