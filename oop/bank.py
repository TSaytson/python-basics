class CheapAccount(object):

  def __init__(self, number) -> None:
    self.number = number
    self.__total = 0

  def deposit(self, value):
    self.__total += value

  def withdraw(self, value):
    self.__total -= value + 1

  def total(self):
    return self.__total
  
class ExpensiveAccount(CheapAccount):
  def __init__(self, number, cvv) -> None:
    super(ExpensiveAccount, self).__init__(number)
    self.cvv = cvv
    
  def withdraw(self, value):
    self._CheapAccount__total -= value + 2
