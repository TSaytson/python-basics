def call_numbers_with_limit(x, limit=10):
  list = range(0,10)
  for number in list[0:limit]:
    print("number.__index__: ", number.__index__())
    if (number.__index__() == list.__len__()-1):
      return x
    print(number)

result = call_numbers_with_limit(x=2, limit=3) # returns none because list.__len__() > limit
print(result)
result = call_numbers_with_limit(x=3, limit=10) # returns x because limit >= list.__len__()
print(result)