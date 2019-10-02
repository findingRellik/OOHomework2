from observers import Subject

class Zookeeper(Subject):
  zoo = []
  __seperator = "----------------" #Used to make it a bit more clear when the zookeeper does something...
  def __init__(self, z):
    self.__state = 0
    self.zoo = z #Zookeepers has a zoo (array of Animal objects)
  def beAZookeeper(self):
    self.changeState(1)
    self.__wakeAnimals() #__ for private methods
    self.changeState(2)
    self.__rollCall()
    self.changeState(3)
    self.__feedAnimals()
    self.changeState(4)
    self.__exerciseAnimals()
    self.changeState(5)
    self.__shutDownZoo()
  def __wakeAnimals(self):
    print(self.__seperator)
    print("The zookeeper is starting their day, and waking up all the animals.")
    print(self.__seperator)
    for animal in self.zoo:
      animal.wakeUp()
  def __rollCall(self):
    print(self.__seperator)
    print("The Zookeeper is making sure every animal is awake and around.")
    print(self.__seperator)
    for animal in self.zoo:
      animal.respondToCall()
  def __feedAnimals(self):
    print(self.__seperator)
    print("The Zookeeper is feeding their animals.")
    print(self.__seperator)
    for animal in self.zoo:
      animal.eat()
  def __exerciseAnimals(self):
    print(self.__seperator)
    print("The Zookeeper is letting their animals roam and excersize.")
    print(self.__seperator)
    for animal in self.zoo:
      animal.roam()
  def __shutDownZoo(self):
    print(self.__seperator)
    print("The Zookeeper is ending their day and putting the animals to rest.")
    print(self.__seperator)
    for animal in self.zoo:
      animal.sleep()