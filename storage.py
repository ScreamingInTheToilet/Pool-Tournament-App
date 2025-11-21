import json
from prototype import Tournament


class Repository:
    
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
    def load(path:str):
        with open(path,'r') as f:
            data = json.load(f)
        return Tournament.from_dict(data)
    
    @staticmethod
    def check():
        file_list = ["playerfile.json","playerfile2.json","playerfile3.json"]
        f_list = []
        e_list = []
        for i in file_list:
            with open(i,'r') as f:
                data = json.load(f)
            if data: #checking if dictionary is not empty i.e True
                f_list.append(i)
            else:
                e_list.append(i)
        return e_list, f_list
    #f_list is a list full of filepaths to occupied files with Tournament data
    #e_list is a list full of filepaths to empty files to store Tournament data.


