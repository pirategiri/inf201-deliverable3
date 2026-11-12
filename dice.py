import random

class Dice:

    def __init__(self, sides: int = 6):

        """defining number of dice sides"""

        if sides<=2:
            raise ValueError("Dice must have more than 2 sides")

        self.sides=sides


    def roll(self)->int:
        """Roll the dice and Return a number from 1 to number of sides"""

        return random.randint(1, self.sides)


    def __str__(self)->int :
        """Alow d20() as a shortcut for d20().roll"""
        return self.roll()


    def __call__(self)-> str:
        return f"Dice (sides ={self.sides})"

    
 