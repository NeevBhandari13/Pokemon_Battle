from abc import ABC, abstractmethod

class PokemonBase(ABC):
    """
    This class is an abstract class, Pokemon base. The class contains methods to instantiate base attributes and will be inherited by child classes.

    The best and worst case complexity of methods is O(1) (Constant Time) unless stated otherwise in the methods
    """
    # An example of a base value for a stat
    BASE_LEVEL = 1
    def __init__(self, hp: int, poke_class: str) -> None:
        """
        Constructor for the class, binds instance variables to 
        given values.

        :param hp: an integer representing the hp of the pokemon, hp >= 0
        :param poke_class: An string containing the class of the Pokemon, poke_class in ["GRASS", "FIRE", "WATER"]
        :returns: None 
        """
        self.hp = hp # assigns argument hp to variable
        self.poke_class = poke_class # assigns argument poke_class to variable
        self.level = self.BASE_LEVEL #initialises level to the base level

        if self.hp < 0: # Checks that pre condition for hp is met
            raise TypeError
        if self.poke_class not in ["GRASS", "FIRE", "WATER"]: # Checks that pre condition for poke_class is met
            raise TypeError

    def get_hp(self) -> int:
        """
        This method returns the hp of the pokemon saved in the instance variable

        :returns: hp of pokemon
        """
        return self.hp

    def get_level(self) -> int:
        """
        This method returns the level of the pokemon saved in the instance variable

        :returns: level of pokemon
        """
        return self.level

    def get_poke_class(self) -> str:
        """
        This method returns the class of the pokemon saved in the instance variable

        :returns: class of pokemon
        """
        return self.poke_class # returns poke_class

    def is_fainted(self) -> bool:
        """
        This method returns a boolean representing whether the pokemon saved in the instance variable has fainted

        :returns: boolean representing whether the pokemon has fainted
        """
        if self.hp <= 0: # checks if pokemon's hp is less than or equal to 0
            return True # returns True if pokemon is fainted
        return False

    def level_up(self) -> None:
        """
        This method increases the level of the pokemon by 1

        :returns: None
        """
        self.level += 1 # Increments level by 1

    @abstractmethod

    def get_speed(self) -> int:
        """
        Abstract method, to be defined while inheriting the base class

        :returns: integer representing speed of pokemon
        """
        pass

    @abstractmethod

    def get_attack_damage(self) -> int:
        """
        Abstract method, to be defined while inheriting the base class

        :returns: integer representing attack damage of pokemon
        """
        pass

    @abstractmethod

    def get_defence(self) -> int:
        """
        Abstract method, to be defined while inheriting the base class

        :returns: integer representing defence of pokemon
        """
        pass
        
    @abstractmethod

    def defend(self, damage: int) -> None:
        """
        Abstract method, to be defined while inheriting the base class

        :param damage: damage that opposing pokemon does, damage >= 0
        :returns: None
        """
        if damage < 0:
            raise ValueError
            assert damage >= 0
        pass

    def lose_hp(self, lost_hp: int) -> None:
        """ This method subtracts a specified amoount of hp from the pokemon

        :returns: None
        """
        self.hp -= lost_hp

    @abstractmethod

    def get_poke_name(self) -> str:
        """
        Abstract method, to be defined while inheriting the base class

        :returns: string representing Pokemon's name
        """
        pass
    

    def __str__(self) -> str:
        """
        Return's string which states Pokemon's name, health and level

        :returns: string describing Pokemon's hp and level
        """
        return str(self.get_poke_name()) + "'s health = " + str(self.get_hp()) + " and level = " + str(self.get_level())


