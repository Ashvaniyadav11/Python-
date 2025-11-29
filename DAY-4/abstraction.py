
#Abstraction
#Hiding internal details & showing only essential features


#Abstract class these classes are blue print of other classes   
# abc module use krke abstracted classes bnate hai

from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar")

lion = Lion()
lion.make_sound()