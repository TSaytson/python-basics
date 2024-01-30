import os

def header():
  print('****************************************')
  print("****************MT - ATM****************")
  print('****************************************')

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')