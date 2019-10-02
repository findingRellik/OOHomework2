from animal import Dog
from animal import Wolf
from animal import Lion
from animal import Tiger
from animal import Cat
from animal import Elephant
from animal import Rhino
from animal import Hippo

from animal import AnimalEatMeat
from animal import AnimalEatPreMixedFood
from animal import AnimalEatVegetarian

from zookeeper import Zookeeper
from zooAnnouncer import ZooAnnouncer

def main():
  zoo = []

  #Cats
  Carmen = Cat("Carmen")
  zoo.append(Carmen)
  Chloe = Cat("Chloe")
  zoo.append(Chloe)
  Caidy = Cat("Caidy")
  zoo.append(Caidy)
  #Lions
  Leeroy = Lion("Leeroy")
  Leeroy.setAnimalEat(AnimalEatMeat())
  zoo.append(Leeroy)
  Leon = Lion("Leon")
  Leon.setAnimalEat(AnimalEatMeat())
  zoo.append(Leon)
  #Tigers
  Tony = Tiger("Tony")
  Tony.setAnimalEat(AnimalEatMeat())
  zoo.append(Tony)
  Tom = Tiger("Tom")
  Tom.setAnimalEat(AnimalEatMeat())
  zoo.append(Tom)
  Timmy = Tiger("Timmy")
  Timmy.setAnimalEat(AnimalEatMeat())
  zoo.append(Timmy)
  #Elephants
  Edith = Elephant("Edith")
  Edith.setAnimalEat(AnimalEatVegetarian())
  zoo.append(Edith)
  Erin = Elephant("Erin")
  Erin.setAnimalEat(AnimalEatVegetarian())
  zoo.append(Erin)
  #Rhinos
  Ryan = Rhino("Ryan")
  Ryan.setAnimalEat(AnimalEatVegetarian())
  zoo.append(Ryan)
  Robert = Rhino("Robert")
  Robert.setAnimalEat(AnimalEatVegetarian())
  zoo.append(Robert)
  Ronan = Rhino("Ronan")
  Ronan.setAnimalEat(AnimalEatVegetarian())
  zoo.append(Ronan)
  #Hippos
  Harper = Hippo("Harper")
  Harper.setAnimalEat(AnimalEatVegetarian())
  zoo.append(Harper)
  Hector = Hippo("Hector")
  Hector.setAnimalEat(AnimalEatVegetarian())
  zoo.append(Hector)
  #Dogs
  Douglas = Dog("Douglas")
  Douglas.setAnimalEat(AnimalEatMeat())
  zoo.append(Douglas)
  Damian = Dog("Damian")
  Damian.setAnimalEat(AnimalEatMeat())
  zoo.append(Damian)
  Dominic = Dog("Dominic")
  Dominic.setAnimalEat(AnimalEatMeat())
  zoo.append(Dominic)
  Daisy = Dog("Daisy")
  Daisy.setAnimalEat(AnimalEatMeat())
  zoo.append(Daisy)
  #Wolves
  Wilson = Wolf("Wilson")
  Wilson.setAnimalEat(AnimalEatMeat())
  zoo.append(Wilson)
  Wendy = Wolf("Wendy")
  Wendy.setAnimalEat(AnimalEatMeat())
  zoo.append(Wendy)

  #PROOF OF DYNAMIC BEHAIVOR AT RUN TIME 
  #(All other eat behaivor set at object instatiation above)
  Carmen.setAnimalEat(AnimalEatPreMixedFood())
  Caidy.setAnimalEat(AnimalEatPreMixedFood())
  Chloe.setAnimalEat(AnimalEatPreMixedFood())

  Kanye = Zookeeper(zoo) #Subject
  Kim = ZooAnnouncer(Kanye) #Observer
  Kanye.registerObserver(Kim)
  Kanye.beAZookeeper()
  del Kim
  del Kanye
  for animal in zoo:
    del animal
  
main()