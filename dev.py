from enum import IntEnum


class Action(IntEnum): # Action here could be anything.  
    Rock = 0 
    Paper = 1
    Scissors = 2

victories = {
        Action.Rock: [Action.Scissors],  # Rock beats scissors
        Action.Paper: [Action.Rock],  # Paper beats rock
        Action.Scissors: [Action.Paper]  # Scissors beats paper
    }

def determine_winner(user_action):
    defeats = victories[user_action]
    print(defeats)

determine_winner(1)