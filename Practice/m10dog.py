class Dog:
    def _init_(self):
        self.dogs = []

    def dog_chechin(self, dog):
        self.dogs.append(dog)

    def dog_chechout(self, dog):
        self.dogs.remove(dog)
        
    def dog_greet(self):
        for dog in self.dogs:
            dog.bark(1)

dog1 = Dog("Max", 2020)
dog2 = Dog("Boi", 2022)
hotel = Hotel()