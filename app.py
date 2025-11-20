from prototype import Tournament
from storage import Repository
import time
import sys


#let's create a tournament by creating a Tournament object

t1 = Tournament("swimming contest",["Srinjoy","Olivia","Samuel","Jacob","Hieu","QM"])


def display_delayed_msg(msg:str):
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()
    print(msg)
    

def start_tournament():

    display_delayed_msg(
        '''
To get started, enter a list of single player names seperated by single spaces. The maximum number of players is 24. 
Alternatively, type the command "$load" to reopen saved tournaments.
        '''
        )
    user_input = input('>>')
    list_of_players = user_input.split()
    while True:
        if len(list_of_players)>len(set(list_of_players)):
        #set removes repeated items. If the length of set(LOP) is less than LOP, then there's repeated items.
            print('Duplicate player names are not permitted, please try again.')
            user_input = input('>>')
            list_of_players = user_input.split()#split string filled with names into a list
        else:
            print('Please state the name of this tournament.')
            time.sleep(0.5)
            t_name = input('>>')
            t = Tournament(t_name,list_of_players) #creating a tournament class object based on inputs given
            break
    display_delayed_msg(
        '''
Tournament generatedly successfully. Type "begin" in the command line to start the tournament.
Alternatively, type "kill" to end the program.
        '''
    )
    while True:
        user_input = input('>>')
        if user_input == "begin":
            t.randomize() #randomize player_list
            match_list = t.pairing() #t.pairing() pairs items inside the randomized player_list
            items = [f"{pair[0]} vs {pair[1]}" if len(pair)==2 else pair[0] for pair in match_list]
            # Convert each matchup list returned by t.pairing() into a readable string:
            # - If the list contains two players, format as "Player1 vs Player2".
            # - If it contains a single player (bye round), use the player name alone.
            break
        elif user_input == "kill":                
            return
        else:
            print('Please make an appropriate selection of the following mentioned above.')
    #first column of matches: even indices
    row1 = items[0::2]
    #second column: odd indices
    row2 = items[1::2]
    '''
    given items (list containing matches) is [A,B,C,D,E]
    items[0::2] start at index 0, step by 2 -> [A,C,E]
    items[1::2] start at index 1, step by 2 -> [B,D] 
    '''
    display_delayed_msg(
f'''
The following pairings have been confirmed for stage {t.stage}. Players without a pair receives a bye.
{"  ".join(row1)}
{"  ".join(row2)}
'''
    )
    for i in match_list:
        time.sleep(1)
        print(f'Round {match_list.index(i)+1}')

    

    

            

text = """
████████╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗███╗   ██╗████████╗
╚══██╔══╝██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
   ██║   ██║   ██║██║   ██║██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
   ██║   ██║   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
   ██║   ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ██╔╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
"""





print(text)

display_delayed_msg('Hello user, welcome to the versatile TOURNAMENT console')
time.sleep(0.5)
print('To begin, type "start" or "help" in the command line')
user_input = input('>>')

while True:
    if user_input.lower() == "start":
        start_tournament()
        break
    elif user_input.lower() == "help":
        print('Are you that dense mate? Just start the program.')
        break
    else:
        print('Please make an appropriate selection. Type "start" or "help" in the command line')
        user_input = input('>>')


