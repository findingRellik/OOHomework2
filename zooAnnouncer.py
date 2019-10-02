from observers import Observer

class ZooAnnouncer(Observer):
  def __announce(self, s):
    print("|||||||||||||||")
    print(s + "   - The Zoo Announcer")
    print("|||||||||||||||")
  def notify(self, s):
    self.__stateOfObserver = s
    if s == 1:
      self.__announce("The Zookeeper is about to wake up the animals!")
    elif s == 2:
      self.__announce("The Zookeeper is taking attendance of the animals!")
    elif s == 3:
      self.__announce("The Zookeeper is feeding the animals!")
    elif s == 4:
      self.__announce("The Zookeeper is letting the animals roam about!")
    else:
      self.__announce("The Zookeeper is putting the animals to bed.")