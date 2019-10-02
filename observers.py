#Here is a generic Python setup for Observer/Subject relationship.
#Inspiration taken from sourcemaking.com's article on Observers in Python, along with the UML and python in the slides
class Subject:
  __observers = []
  __state = None
  def registerObserver(self, o):
    o.__subject = self
    self.__observers.append(o)
  def removeObserver(self, o):
    o.__subject = None
    self.__observers.remove(o)
  def __notifyObservers(self):
    for observer in self.__observers:
      observer.notify(self.__state)
  def returnState(self):
    return self.__state
  def changeState(self, s):
    self.__state = s
    self.__notifyObservers()

class Observer:
  __subject = None
  __stateOfObserver = None
  def __init__(self, sub):
    self.__subject = sub
    self.__stateOfObserver = sub.returnState()
  def notify(self, s):
      self.__stateOfObserver = s