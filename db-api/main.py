import getpass
from db import connectDb

db = connectDb()

cursor = db.cursor()

cursor.execute('SELECT * FROM agencies;')

for row in cursor:
  print(f"Agencia: {row[2]} - {row[1]}")

number = input("Enter your account_number: ")
cursor.execute(f"SELECT * FROM bank_accounts WHERE number = '{number}'")
row = cursor.fetchone()
if row is None:
  print("Account not found")
else:
  print(row)

res = input("Deseja inserir novo usuário? ")
if (res == 's'):
  try:
    number = input('Insira o numero da conta: ')
    name = input('Insira o nome: ')
    password = getpass.getpass('Insira a senha: ')
    value = input('Insira o saldo: ')
    admin = input('Digite 0 para cliente comum e 1 para admin: ')
    agency = input('Digite o número da agência: ')
    cursor.execute("""INSERT INTO bank_accounts (number, name, password, value, admin, agency_id)
                  VALUES (%s,%s,%s,%s,%s,%s)""", (number, name, password, value, admin, agency))
    db.commit()
  except:
    db.rollback()
db.close()