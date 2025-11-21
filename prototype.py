import random

class Tournament:

    def __init__(self,name,player_list:list,final=None,stage=None,winner=None):#making final, stage, and winner __init__ args optional by setting default to None
        self.name = name #name of the tournament
        self.player_list = player_list #list of current players
        self.final = final if final is not None else False 
        #assign __init__ argument final to self.final if argument final is not None, otherwise self.final is False
        self.stage = stage if stage is not None else 1
        #assign __init__ argument stage to self.stage if argument stage is not None, otherwise self.stage is 0
        self.winner = winner if winner is not None else None 
        #self.winner is None unless __init__ argument winner is not None
    
    def randomize(self):#randomly shuffle the list of players to get randomized pairing
        random.shuffle(self.player_list)
    
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
        if player_name in pair:
            self.player_list.append(player_name)
            if self.final == True:
                '''
                If the tournament is in final stage, the declared winner of this match is the
                winner of the entire tournament.
                '''
                self.winner = player_name
    def to_dict(self):
        '''
        converting existing instance attributes into a dictionary
        '''
        return {
            "name":self.name,
            "player_list":self.player_list,
            "final":self.final,
            "stage":self.stage,
            "winner":self.winner
        }
        

    @classmethod
    def from_dict(cls,data):#creating a class instance from a stored dictionary (data)
        return cls(
            name=data["name"],
            player_list=data["player_list"],
            final = data["final"],
            stage = data["stage"],
            winner = data["winner"],
        )
    
    


        


        

    

    