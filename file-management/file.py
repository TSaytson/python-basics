import os
from bank_data import money_slips

file_path = os.path.dirname(os.path.abspath(__file__))

def open_bank_file(mode):
  return open(f"{file_path}/_bank_file.dat", mode)

def write_money_slips(file):
  for money_bill, value in money_slips.items():
    file.write(f"{money_bill}={str(value)};")

def read_money_slips(file):
  line = file.readline()
  print(line)
  # while line.find(';') != -1:
  #   semicolon_pos = line.find(';')
  #   money_bill_value = line[0:semicolon_pos]

read_money_slips(f"{file_path}/_bank_file.dat")