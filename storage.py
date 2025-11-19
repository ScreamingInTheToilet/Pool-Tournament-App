import json
from prototype import Tournament


class Repository:
    file_list = ["playerfile.json","playerfile2.json","playerfile3.json"]

    @staticmethod
    def save(tournament:Tournament,path:str):
        #we are specifying that tournament is a Tournament object, or an existing instance of Tournament
        #store the resulting dictionary form
        data = tournament.to_dict()
        with open(path,"w") as f:
            json.dump(data,f,indent=2)
        '''
        we can only save 1 file at a time as the function rewrites the entire storage/not allowing 
        multiple tournaments to stack
        '''
    @staticmethod
    def load(name,path:str):
        with open(path,'r') as f:
            data = json.load(f)[name]
        return Tournament.from_dict(data)
