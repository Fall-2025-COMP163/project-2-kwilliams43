"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """Base character class with common attributes and methods"""
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """Basic attack based on strength"""
        damage = self.strength
        target.take_damage(damage)

    def take_damage(self, amount):
        """Reduces health by damage amount"""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def display_stats(self):
        """Display character stats"""
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")


class Player(Character):
    """Middle-level class inheriting from Character"""
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1

    def display_stats(self):
        """Extended display to include class and level"""
        print(f"{self.character_class} - {self.name} (Level {self.level})")
        super().display_stats()


class Warrior(Player):
    """Strong physical fighter"""
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)

    def attack(self, target):
        """Attack using strength"""
        damage = self.strength + 5
        target.take_damage(damage)

    def power_strike(self, target):
        """Special warrior ability: powerful attack"""
        damage = self.strength * 2
        target.take_damage(damage)


class Mage(Player):
    """Magic-based character"""
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
        """Magic attack using magic power"""
        damage = self.magic // 2
        target.take_damage(damage)

    def fireball(self, target):
        """Special mage ability: fireball spell"""
        damage = self.magic
        target.take_damage(damage)


class Rogue(Player):
    """Agile and sneaky fighter"""
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 8)

    def attack(self, target):
        """Quick attack with chance-based flavor (simplified)"""
        damage = self.strength + 3
        target.take_damage(damage)

    def sneak_attack(self, target):
        """Special rogue ability: high-damage sneak attack"""
        damage = self.strength * 2
        target.take_damage(damage)


class Weapon:
    """Weapon class for composition with characters"""
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """Display weapon details"""
        print(f"Weapon: {self.name} (Damage Bonus: {self.damage_bonus})")
if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create characters
    warrior = Warrior("Marcus")
    mage = Mage("Aria")
    rogue = Rogue("Shadow")

    # Display stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Test polymorphism
    print("\n⚔️ Polymorphism Test: Different attacks, same method name")
    dummy = Character("Training Dummy", 100, 0, 0)
    for char in [warrior, mage, rogue]:
        print(f"\n{char.name} attacks:")
        char.attack(dummy)
        dummy.health = 100

    # Test special abilities
    print("\n✨ Special Ability Showcase:")
    warrior.power_strike(Character("Goblin", 50, 0, 0))
    mage.fireball(Character("Skeleton", 50, 0, 0))
    rogue.sneak_attack(Character("Bandit", 50, 0, 0))

    # Test composition
    print("\n🗡️ Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Arcane Staff", 12)
    dagger = Weapon("Shadow Dagger", 8)
    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Test battle system
    print("\n⚔️ Simple Battle Test:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()

    print("\n✅ All manual tests complete!")
