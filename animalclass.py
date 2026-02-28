from abc import ABC
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(sef):
        print("i can bark")
class lion(animal):
    def move(self):
        print("i can roar")
R=human()
R.move()
K=snake()
K.move()
R=dog()
R.move()
K=lion()
K.move()