from character import Character
class Battle:

    """Turn-based combat between a hero and an enemy."""

    def __init__(self, hero: Character, enemy: Character) -> None:

        self.hero = hero

        self.enemy = enemy


    def play_round(self) -> None:

        self.hero.attack(self.enemy)

        if self.enemy.is_alive:

            self.enemy.attack(self.hero)


    def simulate_battle(self) -> Character:

        """Run rounds until one dies. Returns the winner."""

        while self.hero.is_alive and self.enemy.is_alive:

            self.play_round()

        return self.hero if self.hero.is_alive else self.enemy