from dice import Dice
class Weapon:
    """A weapon whose damage is decided by a dice roll."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        return f"Weapon(name={self.name!r}, damage_dice={self.damage_dice!r})"