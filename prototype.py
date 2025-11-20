import random

class Tournament:

    saved_tournaments = {}

    def __init__(self,name,player_list):
        self.name = name #name of the tournament
        self.player_list = player_list #list of current players
        self.final = False
        self.stage = 0
        self.winner = None
    
    def randomize(self):
        random.shuffle(self.player_list)
        return self.player_list
    
    def pairing(self):
        match_list = []
        if len(self.player_list) == 2:
            self.final = True #the tournament is now reaching its final stage

        for i in range(0,len(self.player_list),2):
            if i+1>len(self.player_list)-1:
                match_list.append([self.player_list[i]])
            else:
                match_list.append([self.player_list[i],self.player_list[i+1]])
        return match_list
    def declare_winner(self,pair,player_name):
        self.player_list = []
        if player_name in pair:
            self.player_list.append(player_name)
            if self.final == True:
                '''
                If the tournament is in final stage, the declared winner of this match is the
                winner of the entire tournament.
                '''
                self.winner = player_name

    @classmethod
    def from_dict(cls,data):#getting a class instance from a dictionary (data)
        return cls(
            name=data["name"],
            player_list=data["player_list"]
        )
    
    


        


        

    

    