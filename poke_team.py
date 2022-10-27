from pokemon import Charmander, Bulbasaur, Squirtle
from stack_adt import ArrayStack
from queue_adt import CircularQueue

class PokeTeam:
    """
    """
    def __init__(self):
        """
        This method is called when the class is instantiated and creates an object of the class and binds instance variables.

        :returns: None
        """
        self.name = None
        self.team = None
        self.limit = 6
        self.battle_mode = None

    def __correct_team_given(self, charmanders: int, bulbasaurs: int, squirtles: int) -> bool:
        """ This method checks if any inputs are negative and that the total number of pokemon is below self.limit

        :returns: boolean value representing whether the input follows the rules
        """
        if charmanders + bulbasaurs + squirtles > self.limit:
            return False
        if charmanders < 0 or bulbasaurs < 0 or squirtles < 0:
            return False    
        return True

    def __assign_team(self, name:str, charmanders: int, bulbasaurs: int, squirtles:int) -> None:
        """ Loads pokemon onto self.team stack or queue depending on battle battle_mode

        :param charmanders: charmanders >= 0
        :param bulbasaurs: bulbasaurs >= 0
        :param squirtles: squirtles >= 0
        :comp: O(n) where n is charmanders + bulbasaurs + squirtles
        :returns: None
        """
        if charmanders + bulbasaurs + squirtles > self.limit:
            raise ValueError

        if charmanders < 0 or bulbasaurs < 0 or squirtles < 0:
            raise ValueError        

        self.name = name

        if self.battle_mode == 0:
            self.team = ArrayStack(self.limit)
            i = squirtles
            while i > 0:
                self.team.push(Squirtle())
                i -= 1
            i = bulbasaurs
            while i > 0:
                self.team.push(Bulbasaur())
                i -= 1
            i = charmanders
            while i > 0:
                self.team.push(Charmander())
                i -= 1
            
        elif self.battle_mode == 1:
            self.team = CircularQueue(self.limit)
            i = charmanders
            while i > 0:
                self.team.append(Charmander())
                i -= 1
            i = bulbasaurs
            while i > 0:
                self.team.append(Bulbasaur())
                i -= 1
            i = squirtles
            while i > 0:
                self.team.append(Squirtle())
                i -= 1
        

    
    def choose_team(self, name: str, battle_mode: int) -> None:
        """ Reads in numbers of charmanders, bulbasaurs and squirtles and assigns them to self.team with __assign_team__(name, c, b, s) after checking they follow rules with__correct_team_given__(c, b, s) 

        :param battle_mode: battle_mode = 0 or 1
        :comp: O(n) where n is c + b + s
        :returns: None
        """     
        if battle_mode not in range(0,2):
            raise ValueError

        check = False
        while check == False:
            c = input("Number of Charmanders? ")
            b = input("Number of Bulbasaurs? ")
            s = input("Number of Squirtles? ")
            if __correct_team_given__(c, b, s) == True:
                __assign_team__(name, c, b, s)
                check = True
        if self.battle_mode == 0:
            self.team = ArrayStack()
        elif self.battle_mode == 1:
            self.team = CircularQueue()

    def __str__(self) -> str:
        """Returns string detailing health and level of pokemon on the array stack

        :comp: O(n) complexity where n is the length of self.team
        :returns: string with health and level of pokemon on stack
        """
        return str(self.team)


