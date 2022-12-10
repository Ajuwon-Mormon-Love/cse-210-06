from game.casting.actor import Actor

class Artifact(Actor):

    def __init__(self):
        super().__init__()

    def calc_points(self):
        """Calculate points based on gem(*) or stone(O) collision
        """""
        points = 0 

        if (self.get_text() == '*'):
            points = 1
        else:
            points = -1
        
        return points

    
