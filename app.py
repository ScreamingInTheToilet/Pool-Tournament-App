import json
import random

with open("playerfile.json",'r') as f:
    data = json.load(f)

tournament_list = []
player_list = []
match_list = []

#insert data
def insert_player(player_ID, player_name):
    if player_ID not in data["list_of_ID"]:
        data["players"].append({"ID":player_ID,"name":player_name})
        data["list_of_ID"].append(player_ID)
    else:
        pass

def insert_spreadsheet(file_of_players):
    pass

insert_player(8372,"Sofia")
insert_player(3482,"Emma")
insert_player(2948,"Isabel")
insert_player(3292,"Gabriel")
insert_player(1649,"Angus")
insert_player(6839,"Alkut")
insert_player(3458,"Olivia")
insert_player(2394,"Scarlett")
insert_player(6688,"Jacob")
insert_player(4758,"Sophie")
insert_player(2283,"Isabel")
insert_player(1283,"Hamish")
insert_player(5378,"Alec")



#pairing system

def randomize(list_bravo):
    for i in list_bravo:
        player_list.append(i["ID"])
    random.shuffle(player_list)
    for i in range(0,len(player_list),2):
        if i+1 > len(player_list)-1:
            match_list.append([player_list[i]])
        else:
            match_list.append([player_list[i],player_list[i+1]])
    return match_list


def pairing(list_bravo):
    match_list
    for i in range(0, len(list_bravo),2):
        if i+1 > len(list_bravo)-1:
            match_list.append([list_bravo[i]])
        else:
            match_list.append([list_bravo[i],list_bravo[i+1]])
    return match_list




            





with open('playerfile.json','w') as f:
    json.dump(data,f,indent=2)


player_list = []



'''

functions:

randomizer - randomly assigning numbers to the player, 
before inserting them into list indexes corresponding to the player's assigned number

pairing - pairs players next to each other in a list order.

view - view player's status and background info by providing their ID

eliminate - give the user the choice to eliminate players.

session_error - If an error occurs, this function handles the error.

insert_playerdata - If the User wishes to insert a premade excel sheet, 
they can do so through this function

rounds - proceed to another round.
'''


def randomizer(list):
    pass


def pairing(list):
    '''
    creating match ups with players next to each other.
    '''
    pass

def view(player_ID):
    pass

def eliminate(player_ID=None, player_nun=None):
    '''
    In each match, the user gets to choose what player they want to eliminate.
    '''
    pass

def rounds():
    pass


