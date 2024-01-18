list = [2, 4, 6, 8, 10]

for item in list:
  if (list.index(item) == list.__len__()-1):
    print(item)
    break
  print(str(item) + ", ", end="")