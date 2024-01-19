class Car:

  classAttribute = 'This is a class attribute'
  def __init__(self, color, name, year, manufacturer):
    self.color = color
    self.name = name
    self.year = year
    self.manufacturer = manufacturer

  def drive(self):
    print(f"{self.name} is moving")

  @staticmethod
  def static():
    print("This is a static method")

  @classmethod
  def classMet(cls):
    print(cls.classAttribute)
