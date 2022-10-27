from pokemon_base import PokemonBase

class Charmander(PokemonBase):
    """
    This class creates an object of type 'Charmander' which inherits from the PokemonBase class
    
    The best and worst case complexity of methods is O(1) (Constant Time) 
    unless stated otherwise in the methods
    """
    effectiveness = {"WATER": 0.5, "GRASS": 2, "FIRE": 1}

    def __init__(self):
        """
        This method is called when the class is instantiated and creates an object of the class and binds instance variables.

        :returns: None
        """
        PokemonBase.__init__(self, 7, "FIRE")
        self.speed = 8 + self.level
        self.attack_damage = 6 + self.level
        self.defence = 4

    def get_speed(self) -> int:
        """
        This method returns the speed of the pokemon saved in the instance variable

        :returns: speed of pokemon
        """
        self.speed = 8 + self.level
        return self.speed

    def get_attack_damage(self) -> int:
        """
        This method returns the attack damage of the pokemon saved in the instance variable

        :returns: attack damage of pokemon
        """
        self.attack_damage = 6 + self.level
        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method returns the defence of the pokemon saved in the instance variable

        :returns: integer representing defence of pokemon
        """
        return self.defence
        
    def defend(self, damage: int) -> None:
        """
        This method updates the pokemon's hp based on the damage done to it by an opposing pokemon.

        :param damage: damage that opposing pokemon does, damage >= 0
        :returns: None
        """
        if damage > Charmander.get_defence(self): # checks if 
            self.hp -= damage
        else:
            self.hp -= (damage // 2)

    def get_poke_name(self) -> str:
        """
        This method returns the name of the pokemon saved in the instance variable

        :returns: string representing name of pokemon
        """
        return "Charmander"
    

class Bulbasaur(PokemonBase):
    """
    This class creates an object of type 'Charmander' which inherits from the PokemonBase class
    
    The best and worst case complexity of methods is O(1) (Constant Time) 
    unless stated otherwise in the methods
    """
    effectiveness = {"WATER": 2, "GRASS": 1, "FIRE": 0.5}

    def __init__(self):
        """
        This method is called when the class is instantiated and creates an object of the class and binds instance variables.

        :returns: None
        """
        PokemonBase.__init__(self, 9, "GRASS")
        self.speed = 7 + self.level // 2
        self.attack_damage = 5
        self.defence = 5

    def get_speed(self) -> int:
        """
        This method returns the speed of the pokemon saved in the instance variable

        :returns: speed of pokemon
        """
        self.speed = 7 + self.level // 2
        return self.speed

    def get_attack_damage(self) -> int:
        """
        This method returns the attack damage of the pokemon saved in the instance variable

        :returns: attack damage of pokemon
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method returns the defence of the pokemon saved in the instance variable

        :returns: integer representing defence of pokemon
        """
        return self.defence

    def defend(self, damage: int) -> None:
        """
        This method updates the pokemon's hp based on the damage done to it by an opposing pokemon.

        :param damage: damage that opposing pokemon does, damage >= 0
        :returns: None
        """
        if damage > (Bulbasaur.get_defence(self) + 5):
            self.hp -= damage
        else:
            self.hp -= (damage // 2)

    def get_poke_name(self) -> str:
        """
        This method returns the name of the pokemon saved in the instance variable

        :returns: string representing name of pokemon
        """
        return "Bulbasaur"

class Squirtle(PokemonBase):
    """
    This class creates an object of type 'Charmander' which inherits from the PokemonBase class
    
    The best and worst case complexity of methods is O(1) (Constant Time) 
    unless stated otherwise in the methods
    """
    effectiveness = {"WATER": 1, "GRASS": 0.5, "FIRE": 2}

    def __init__(self):
        """
        This method is called when the class is instantiated and creates an object of the class and binds instance variables.

        :returns: None
        """
        PokemonBase.__init__(self, 8, "WATER")
        self.speed = 7
        self.attack_damage = 4 + self.level // 2
        self.defence = 6 + self.level

    def get_speed(self) -> int:
        """
        This method returns the speed of the pokemon saved in the instance variable

        :returns: speed of pokemon
        """
        return self.speed

    def get_attack_damage(self) -> int:
        """
        This method returns the attack damage of the pokemon saved in the instance variable

        :returns: attack damage of pokemon
        """
        self.attack_damage = 4 + self.level // 2
        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method returns the defence of the pokemon saved in the instance variable

        :returns: integer representing defence of pokemon
        """
        self.defence = 6 + self.level
        return self.defence

    def defend(self, damage: int) -> None:
        """
        This method updates the pokemon's hp based on the damage done to it by an opposing pokemon.

        :param damage: damage that opposing pokemon does, damage >= 0
        :returns: None
        """
        if damage > (Squirtle.get_defence(self) * 2):
            self.hp -= damage
        else:
            self.hp -= (damage // 2)

    def get_poke_name(self) -> str:
        """
        This method returns the name of the pokemon saved in the instance variable

        :returns: string representing name of pokemon
        """
        return "Squirtle"

