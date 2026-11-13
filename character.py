from items import Weapon


class Character:
    """Represents a character in the RPG."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None) -> None:

        if hp_max <= 0:
            raise ValueError("Maximum HP must be greater than 0")

        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target: "Character") -> None:
        """Attack target. Uses weapon damage if equipped, else base damage."""
        if self.weapon is not None:
            amount = self.weapon.roll_damage()
        else:
            amount = self.damage

        target.take_damage(amount)

    def take_damage(self, amount: int) -> None:
        """Reduce own HP, never below 0."""
        if amount < 0:
            raise ValueError("Damage cannot be negative")

        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Increase own HP, never above hp_max."""
        if amount < 0:
            raise ValueError("Healing cannot be negative")

        self._hp = min(self._hp + amount, self.hp_max)

    def introduce(self) -> None:
        print(f"Hi, my name is {self.name}!")

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def is_alive(self) -> bool:
        return self._hp > 0

    def __repr__(self) -> str:
        return (f"<{type(self).__name__} name={self.name} "
                f"hp={self.hp} damage={self.damage}>")

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.name} with {self.hp} HP and {self.damage} damage"


class Warrior(Character):
    """Defensive specialist: armor reduces incoming damage."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, armor: int = 5) -> None:

        super().__init__(name, hp_max, damage, weapon)

        if armor < 0:
            raise ValueError("Armor cannot be negative")

        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce incoming damage using armor."""

        if amount < 0:
            raise ValueError("Damage cannot be negative")

        reduced = max(amount - self.armor, 0)
        super().take_damage(reduced)


class Mage(Character):
    """Resource-based attacker: spells cost mana."""

    SPELL_COST = 10
    MANA_RESTORE = 5

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None,
                 mana: int = 30, mana_max: int = 30) -> None:

        super().__init__(name, hp_max, damage, weapon)

        if mana_max < 0:
            raise ValueError("Maximum mana cannot be negative")

        if mana < 0 or mana > mana_max:
            raise ValueError("Mana must be between 0 and maximum mana")

        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """Use magic if enough mana, otherwise use normal attack."""

        if self.mana >= self.SPELL_COST:
            self.mana -= self.SPELL_COST
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            self.mana = min(self.mana + self.MANA_RESTORE, self.mana_max)
