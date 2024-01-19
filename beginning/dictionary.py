cars = {}
cars['BYD Seal'] = "black"
cars['Panamera'] = "blue"
cars['X4'] = "pink"

print("cars['BYD Seal']:", cars['BYD Seal'])
print(cars.keys())
print(cars.values())

family = dict(Thiago="Papi", Mariana="Mami", Donzinho="firo")

print(family)

for key, value in family.items():
  print(key + " is " + value)

if "Donzinho" in family:
  print("best firo", end="")
