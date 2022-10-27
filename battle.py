""" Class to perform battle between 2 teams of Pokemon in set mode battle format or rotating mode battle format

__author__ = "Neev Bhandari"
__last_modified__ = 18.09.2021
"""
from poke_team import PokeTeam

class Battle:
    """ This class 
    """

    def set_mode_battle(self, player_one: str, player_two: str) -> int:
        """ This method initialises 2 pokemon teams and calls on __conduct_combat so they can battle

        :comp: 
        :returns: 0, 1 or 2 depending on outcome of battle
        """
        team1 = choose_team(player_one, 0)
        team2 = choose_team(player_two, 0) 
        
        return __conduct_combat(self, team1, team2, 0)
    
    def rotating_mode_battle(self, player_one: str, player_two: str) -> int:
        """ This method initialises 2 pokemon teams and calls on __conduct_combat so they can battle

        
        :returns: 0, 1 or 2 depending on the outcome of the battle
        """
        team1 = choose_team(player_one, 1)
        team2 = choose_team(player_two, 1) 

        return __conduct_combat(self, team1, team2, 1)

    def __conduct_combat(self, team1: PokeTeam, team2: PokeTeam, battle_mode: int) -> int:
        """ This method facilitates battle between 2 teams in a set ot rotating mode format depending on the battle_mode. 

        :param battle_mode: battle_mode = 0 or 1
        """
        if battle_mode == 0:
            while team1.team.is_empty() == False and team2.team.is_empty() == False:
                P1 = team1.team.pop()
                P2 = team2.team.pop()

                if P2.get_speed() > P1.get_speed():
                    P1.defend(P2.get_attack_damage() * P2.effectiveness[P1.get_poke_class()])

                elif P1.get_speed() > P2.get_speed():
                    P2.defend(P1.get_attack_damage() * P1.effectiveness[P2.get_poke_class()])

                elif P1.get_speed() == P2.get_speed():
                    P1.defend(P2.get_attack_damage() * P2.effectiveness[P1.get_poke_class()])
                    P2.defend(P1.get_attack_damage() * P1.effectiveness[P2.get_poke_class()])

                if P1.is_fainted() == True and P2.is_fainted() == False:
                    P2.level_up()
                    team2.team.push(P2)

                if P2.is_fainted() == True and P1.is_fainted() == False:
                    P1.level_up()
                    team1.team.push(P1)

                if P1.is_fainted() == False and P2.is_fainted() == False:
                    P1.lose_hp(1)
                    if P1.hp > 0:
                        team1.team.push(P1)
                    else:
                        P2.level_up()
                    P2.lose_hp(1)
                    if P2.hp > 0:
                        team2.team.push(P2)
                    else:
                        P1.level_up()

        if battle_mode == 1:
            while team1.team.is_empty() == False and team2.team.is_empty() == False:
                P1 = team1.team.serve()
                P2 = team2.team.serve()

                if P2.get_speed() > P1.get_speed():
                    P1.defend(P2.get_attack_damage() * P2.effectiveness[P1.get_poke_class()])

                elif P1.get_speed() > P2.get_speed():
                    P2.defend(P1.get_attack_damage() * P1.effectiveness[P2.get_poke_class()])

                elif P1.get_speed() == P2.get_speed():
                    P1.defend(P2.get_attack_damage() * P2.effectiveness[P1.get_poke_class()])
                    P2.defend(P1.get_attack_damage() * P1.effectiveness[P2.get_poke_class()])

                if P1.is_fainted() == True and P2.is_fainted() == False:
                    P2.level_up()
                    team2.team.append(P2)

                if P2.is_fainted() == True and P1.is_fainted() == False:
                    P1.level_up()
                    team1.team.append(P1)

                if P1.is_fainted() == False and P2.is_fainted() == False:
                    P1.lose_hp(1)
                    if P1.hp > 0:
                        team1.team.append(P1)
                    else:
                        P2.level_up()
                    P2.lose_hp(1)
                    if P2.hp > 0:
                        team2.team.append(P2)
                    else:
                        P1.level_up()
                
                
        
        if team1.team.is_empty() == True and team2.team.is_empty() == True:
            return 0

        if team2.team.is_empty() == True:
            return 1
        
        if team1.team.is_empty() == True:
            return 2
