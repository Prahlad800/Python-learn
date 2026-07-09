"""
Topic: OOP Mini Project
Chapter: 16
Level: Advanced

Description:
    A comprehensive mini-project that brings together all the Object-Oriented Programming 
    concepts learned in this chapter: Classes, Inheritance, Polymorphism, Encapsulation, 
    Class/Static Methods, Dunder Methods, and Composition.

Project: Simple Role-Playing Game (RPG) Battle System
    We will build a system with different character classes (Warrior, Mage), items, 
    and a battle sequence.

Key Concepts:
    - Full System Design using OOP
    - Composition (Characters HAS-A Weapon)
    - Inheritance (Warrior IS-A Character)
    - Polymorphism (Different attack implementations)
"""

# ============================================================
# SECTION 1: SYSTEM COMPONENTS (COMPOSITION)
# ============================================================
import random
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    @abstractmethod
    def use(self, target) -> str:
        pass

class Weapon(Item):
    def use(self, target) -> str:
        damage = self.value + random.randint(0, 5)
        target.take_damage(damage)
        return f"attacks with {self.name} for {damage} damage!"

class Potion(Item):
    def use(self, target) -> str:
        target.heal(self.value)
        return f"drinks {self.name} and heals for {self.value} HP!"

# ============================================================
# SECTION 2: BASE CHARACTER CLASS (ENCAPSULATION & DUNDER)
# ============================================================

class Character(ABC):
    def __init__(self, name: str, hp: int, weapon: Weapon):
        self.name = name
        self._max_hp = hp
        self._current_hp = hp
        self.weapon = weapon # Composition
        
    @property
    def is_alive(self) -> bool:
        return self._current_hp > 0
        
    def take_damage(self, amount: int):
        self._current_hp -= amount
        if self._current_hp < 0:
            self._current_hp = 0
            
    def heal(self, amount: int):
        self._current_hp += amount
        if self._current_hp > self._max_hp:
            self._current_hp = self._max_hp

    def __str__(self):
        return f"{self.name} [HP: {self._current_hp}/{self._max_hp}]"

    @abstractmethod
    def action(self, target) -> str:
        """Determines the specific action the character takes in a turn."""
        pass

# ============================================================
# SECTION 3: SPECIFIC CHARACTERS (INHERITANCE & POLYMORPHISM)
# ============================================================

class Warrior(Character):
    def action(self, target) -> str:
        # Polymorphism: Warrior just uses their weapon
        return self.weapon.use(target)

class Mage(Character):
    def __init__(self, name: str, hp: int, weapon: Weapon, mana: int):
        super().__init__(name, hp, weapon)
        self.mana = mana
        
    def action(self, target) -> str:
        # Polymorphism: Mage can cast spells if they have mana, else attack
        if self.mana >= 10:
            self.mana -= 10
            damage = 20
            target.take_damage(damage)
            return f"casts Fireball for {damage} damage! (Mana left: {self.mana})"
        else:
            return f"is out of mana! {self.weapon.use(target)}"

# ============================================================
# SECTION 4: THE BATTLE ENGINE (STATIC METHODS & LOGIC)
# ============================================================

class BattleEngine:
    
    @staticmethod
    def fight(char1: Character, char2: Character):
        print(f"--- BATTLE START: {char1.name} vs {char2.name} ---")
        
        round_num = 1
        while char1.is_alive and char2.is_alive:
            print(f"\nRound {round_num}")
            print(char1)
            print(char2)
            
            # Char 1 attacks Char 2
            print(f"{char1.name} {char1.action(char2)}")
            if not char2.is_alive:
                break
                
            # Char 2 attacks Char 1
            print(f"{char2.name} {char2.action(char1)}")
            
            round_num += 1
            
        print("\n--- BATTLE OVER ---")
        if char1.is_alive:
            print(f"{char1.name} is victorious!")
        elif char2.is_alive:
            print(f"{char2.name} is victorious!")
        else:
            print("It's a draw!")

# ============================================================
# SECTION 5: RUNNING THE PROJECT
# ============================================================

def run_project():
    # Setup Weapons (Composition)
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Wooden Staff", 5)
    
    # Setup Characters (Inheritance)
    conan = Warrior("Conan", hp=50, weapon=sword)
    gandalf = Mage("Gandalf", hp=40, weapon=staff, mana=20)
    
    # Run Battle
    BattleEngine.fight(conan, gandalf)

if __name__ == "__main__":
    run_project()
