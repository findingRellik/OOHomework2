from outPrint import outPrint
import random

class AnimalInterface:
  def wakeUp():
    print("ERROR: NOT IMPLEMENTED")
  def respondToCall():
    print("ERROR: NOT IMPLEMENTED")
  def eat():
    print("ERROR: NOT IMPLEMENTED")
  def roam():
    print("ERROR: NOT IMPLEMENTED")
  def sleep():
    print("ERROR: NOT IMPLEMENTED")

class Animal(AnimalInterface):
  def setAnimalEat(self, a): #Strategy set-up happens here
    self.animalEat = a
  def eat(self): #Strategy call happens here
    outPrint(self.name, self.animalType, self.animalEat.eat())
  def wakeUp(self):
    outPrint(self.name, self.animalType, "am waking up.")
  def roam(self):
    outPrint(self.name, self.animalType, "am roaming as long as the zookeeper lets me.")
  def sleep(self):
    outPrint(self.name, self.animalType, "am going to sleep for a good night's rest.")

#STRATEGY PATTERN CLASSES
class AnimalEat:
  def eat(self):
    outPrint(self.name, self.animalType, self.animalEat.eat())
class AnimalEatMeat(AnimalEat):
  def eat(self):
    return "ate a healthy portion of meat."
class AnimalEatVegetarian(AnimalEat):
  def eat(self):
    return "ate a healthy portion of vegetarian diet."
class AnimalEatPreMixedFood(AnimalEat):
  def eat(self):
    return "ate a healthy portion of some pre-mixed food."

#CANINES
class Canine(Animal):
  def sleep(self):
    outPrint(self.name, self.animalType, "found my favorite spot of comfort and went to sleep.")
class Dog(Canine):
  def __init__(self, n):
    self.name = n
    self.animalType = "dog"
  def respondToCall(self):
    outPrint(self.name, self.animalType, "barked and barked and barked and barked and...")
class Wolf(Canine):
  def __init__(self, n):
    self.name = n
    self.animalType = "wolf"
  def respondToCall(self):
    outPrint(self.name, self.animalType, "howled loudly, causing every other wolf to howl.")

#FELINES
class Feline(Animal):
  def sleep(self):
    outPrint(self.name, self.animalType, "walked in circles for a bit, and then went to bed.")
class Tiger(Feline):
  def __init__(self, n):
    self.name = n
    self.animalType = "tiger"
  def respondToCall(self):
    outPrint(self.name, self.animalType,"roared much louder than the lions out of spite.")
  def roam(self):
    outPrint(self.name, self.animalType, "tried attacking a few animals while roaming.")
class Lion(Feline):
  def __init__(self, n):
    self.name = n
    self.animalType = "lion"
  def respondToCall(self):
    outPrint(self.name, self.animalType,"said 'long live the king' but it only came out as a roar.")
class Cat(Feline):
  def __init__(self, n):
    self.name = n
    self.animalType = "cat"
  def __beACat(self, numberOfOptions): #Random integer returner for Cat-like behaivor
    random.seed(random.randint(0, 50))
    return random.randint(0, numberOfOptions - 1)
  def wakeUp(self):
    options = ["kept sleeping...", "scratched the poor soul who tried to wake me up.", "woke up and meowed."]
    responceIndex = self.__beACat(len(options))
    outPrint(self.name, self.animalType, options[responceIndex])
  def respondToCall(self):
    options = ["meowed.", "stared longingly at the horizon."]
    responceIndex = self.__beACat(len(options))
    outPrint(self.name, self.animalType, options[responceIndex])
  def roam(self):
    options = ["walked around in a friendly manner.", "walked around looking for a fight..."]
    responceIndex = self.__beACat(len(options))
    outPrint(self.name, self.animalType, options[responceIndex])
  def sleep(self):
    options = ["went to sleep in my cat bed.", "meowed in the hallway until 4 in the morning."]
    responceIndex = self.__beACat(len(options))
    outPrint(self.name, self.animalType, options[responceIndex])

#PACHYDERM
class Pachyderm(Animal):
  def wakeUp(self):
    outPrint(self.name, self.animalType, "slowly wake up.")
class Elephant(Pachyderm):
  def __init__(self, n):
    self.name = n
    self.animalType = "elephant"
  def respondToCall(self):
    outPrint(self.name, self.animalType, "did that thing that elephants do with their trunk.")
class Rhino(Pachyderm):
  def __init__(self, n):
    self.name = n
    self.animalType = "rhino"
  def respondToCall(self):
    outPrint(self.name, self.animalType, "grunted.")
  def roam(self):
    outPrint(self.name, self.animalType, "scared everything around me while roaming around.")
class Hippo(Pachyderm):
  def __init__(self, n):
    self.name = n
    self.animalType = "hippo"
  def respondToCall(self):
    outPrint(self.name, self.animalType, "snorted.")