import unittest
from animal import Animal


class Test_animal(unittest.TestCase):
    def test_animal_cat(self):        
        animal1 = Animal('cat')
        self.assertEqual(animal1.name, 'Seymore')
        if animal1.name != 'Seymore':
            print(animal1.name)

    def test_animal_dog(self):
        animal2 = Animal('dog')
        self.assertEqual(animal2.name, 'Spot')
        if animal2.name != 'Spot':
            print(animal2.name)

    def speak(self):
        for size in Animal:
            if size == 'small' and type == 'cat':
                print('meow')
            else: print('MEOW!')
    
    def speak(self):
        for size in Animal:
            if size == 'small' and type == 'dog':
                print ('bow wow')
            elif size =='medium' and type == 'dog':
                print ('Ruff ruff')
            else:
                print('arf arf')
    
    def describe(self):
        for age in Animal:
            if age < 10:
                print('young')
            else:
                print('old')
            



        
