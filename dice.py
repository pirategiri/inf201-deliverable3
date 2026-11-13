import random


class Dice:

    def __init__(self, sides: int = 6):
        """Define the number of dice sides."""
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides")

        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random number."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Return the dice representation."""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allow d20() as a shortcut for d20.roll()."""
        return self.roll()
