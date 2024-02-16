import os
import bank_data


file_path = os.path.dirname(os.path.abspath(__file__))

def open_bank_file(mode:str):
  return open(f"{file_path}/_bank_file.dat", mode)

def write_money_slips(file):
  for money_bill, value in bank_data.money_slips.items():
    file.write(f"{money_bill}={str(value)};")

def write_bank_accounts(file):
  for account, account_data in bank_data.accounts_list.items():
    file.writelines((
      account, ';',
      account_data['name'], ';',
      account_data['password'], ';',
      str(account_data['balance']), ';',
      str(account_data['admin']), ';'
      '\n'
    ))

def read_money_slips(file):
  line = file.readline()
  print(line)
  while line.find(';') != -1:
    semicolon_position = line.find(';')
    money_bill_value = line[0:semicolon_position]
    set_money_bill_value(money_bill_value)
    if semicolon_position+1 == len(line):
      break
    else:
      line = line[semicolon_position+1:len(line)]

def set_money_bill_value(money_bill_value):
  equal_position = money_bill_value.find("=")
  money_bill = money_bill_value[0:equal_position]
  print(f"equal position: {equal_position}")
  value = money_bill_value[equal_position+1:len(money_bill_value)]
  print(f"money bill: {money_bill}")
  print(f"value: {value}")
  bank_data.money_slips[money_bill] = int(value)

def read_bank_accounts(file):
  lines = file.readlines()
  lines = lines[1:len(lines)]
  for account_line in lines:
    extract_bank_account(account_line)

def extract_bank_account(account_line):
  account_data = []
  while account_line.find(';') != -1:
    semicolon_pos = account_line.find(';')
    data = account_line[0:semicolon_pos]
    account_data.append(data)
    if semicolon_pos+1 == len(account_line):
      break
    else:
      account_line = account_line[semicolon_pos+1:len(account_line)]
  add_bank_account(account_data)

def add_bank_account(account_data):
  bank_data.accounts_list[account_data[0]] = {
    'name': account_data[1],
    'password': account_data[2],
    'balance': account_data[3],
    'admin': True if account_data[4] == 'True' else False
  }

def load_bank_data():
  file = open_bank_file('r')
  read_money_slips(file)
  file.close()
  file = open_bank_file('r')
  read_bank_accounts(file)

def save_money_slips():
  file = open_bank_file('r')
  lines = file.readlines()
  file.close()
  file = open_bank_file('w')
  lines[0] = ""
  for money_bill, value in bank_data.money_slips.items():
    lines[0] += money_bill + '=' + str(value) + ';'
  lines[0] += '\n '
  file.writelines(lines)
  file.close()