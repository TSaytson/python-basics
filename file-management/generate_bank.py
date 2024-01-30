from utils import header
from file import open_bank_file, write_money_slips


def create_money_slips():
  file = open_bank_file('w')
  write_money_slips(file)
  file.close()

def main():
  header()
  create_money_slips()
  print("Money slips successfully stored")

main()