#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animal:
    def eat(self):
        print("This animal is eating.")
        
    def sleep(self):
        print("This animal is sleeping.")

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Fish(Animal):
    pass

class Dog(Mammal):
    def eat(self):
        print("The dog is eating dog food.")

class Cat(Mammal):
    def eat(self):
        print("The cat is eating cat food.")

class Eagle(Bird):
    def eat(self):
        print("The eagle is eating fish.")


def feed_animal(animal):
    animal.eat()


dog = Dog()
cat = Cat()
eagle = Eagle()

for animal in [dog, cat, eagle]:
    feed_animal(animal)


# In[ ]:




