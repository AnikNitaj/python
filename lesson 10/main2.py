from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def get_name(self):
        pass

    class dog(Animal):
        def make_sound(self):
            print("Ham ham")

dog1 = dog()
dog1.make_sound()
print(dog1.get_name())