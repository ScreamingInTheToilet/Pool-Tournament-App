from prototype import Tournament
from storage import Repository
import time


#let's create a tournament by creating a Tournament object

#generate file report
def generate_report(empty_list, occupied_list):
    # Column labels for the system report (you can rename these)
    left_label = "Unassigned Records"
    right_label = "Active Records"

    # If a list is empty, replace it with ["None"] so the report shows something
    left_items = empty_list if empty_list else ["None"]
    right_items = occupied_list if occupied_list else ["None"]

    # Determine how many rows to print based on the longer list
    max_rows = max(len(left_items), len(right_items))

    # Print the header row with fixed-width columns (25 characters each)
    print(f"{left_label:<25} {right_label:<25}")
    # Print a separation line for readability
    print("-" * 50)

    # Loop over all rows needed
    for i in range(max_rows):
        # If the index exists, use the item; otherwise use an empty string
        left_val = left_items[i] if i < len(left_items) else ""
        right_val = right_items[i] if i < len(right_items) else ""

        # Print both values in aligned columns
        print(f"{left_val:<25} {right_val:<25}")

def verify_saving(tournament_obj:Tournament, path:str):
    '''
    check if the tournament-class object has the same name and stage as the loaded tournament object from the save file,
    to determine if the tournament-class object has been successfully saved.
    '''
    if tournament_obj.name == Repository.load(path).name:
        if tournament_obj.stage == Repository.load(path).stage:
            if tournament_obj.player_list == Repository.load(path).player_list:
                return True



#sending delayed dialogue
def display_delayed_msg(msg:str):
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()
    print(msg)



#running the matches (two players against each other)
def match_process(match_list_:list,match_list_2:list, tournament_obj:Tournament):
    tournament_obj.player_list = []#clear player_list to reconstruct with winning players from current stage

    #match_list_ is the readable version, match_list_2 is the nonreadable version (nested list)
    for i in match_list_2:#looping thru each list of paired players inside the nested list
        if len(i) == 1:
        #if the match items is odd i.e containing single players on bye,
            tournament_obj.player_list.append(i[0])#adding the single player into player_list.
            continue
        time.sleep(1)
        print(f'Round {match_list_2.index(i)+1}, '+match_list_[match_list_2.index(i)])
        time.sleep(0.5)
        print('Please declare this round\'s winner.')
        winner = input('>>')
        if winner in i:#if the selected winner is in the individual match list items
            tournament_obj.declare_winner(i,winner)
    #once every match item in the match_list is processed, the winners of the current tournament stage will be declared.
    display_delayed_msg(f'The remainining player(s) of stage {tournament_obj.stage} is {', '.join(tournament_obj.player_list)}')
    tournament_obj.stage += 1




def start_tournament():
    global t
    display_delayed_msg(
        '''
To get started, enter a list of single player names seperated by single spaces. The maximum number of players is 24.
Alternatively, type the command "$load" to reopen saved tournaments.
        '''
        )
    user_input = input('>>')
    if user_input == '$load':#checking if User wants to load the file
        print('Make a selection on the given files. To load saved tournament data, files chosen must be assigned.')
        a,b = Repository.check() #getting a list of occupied playerfiles and a list of empty playerfiles
        display_delayed_msg('')
        generate_report(a,b)
        while True:
            user_input_2 = input('>>')
            if user_input_2 in a:
                print('Chosen file does not contain any saved tournament data')
            elif user_input_2 in b:
                t = Repository.load(user_input_2)
                if t.final == True:#checking if the loaded tournament has ended or not
                    print(f'The {t.name} has ended, please choose another tournament.')
                else:
                #if the tournament has not ended, break the loop to end the function and proceed.
                    break
            else:
                print('File chosen is either invalid or does not exist. Please try again')


    else:
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


def continue_tournament():#continues the tournament after tournament data is created or loaded
    display_delayed_msg(
            '''
Tournament generated successfully. Type "begin" in the command line to start the tournament.
Alternatively, type "kill" to end the program.
            '''
    )

    while True:
        user_input = input('>>')
        #initialize phase (when we randomize the playerlist and begin the tournament)
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
    match_process(items, match_list, t)
    #continuation phase (continue pairing players for matches until the end)
    while True:
        time.sleep(1)
        if len(t.player_list) == 1:
            #if length of player list is 1 at the end of a stage, there's a clear winner
            display_delayed_msg(
                    f'''
The final winner of the {t.name} tournament is {t.player_list[0]}. Congratulations on making it through
{t.stage} stage(s) of the tournament.
'''
                )
            break#Kill the while loop and end the entire continue_tournament function

        print(
'''
Next tournament stage commences. If you wish to continue, type "continue" otherwise type "kill".
If you wish to save tournament until later, type "save".
'''
            )
        user_input = input('>>')
        if user_input == "continue":
            if len(t.player_list) != 1:#if the length of the player list is not 1

                match_list = t.pairing()
                items = [f"{pair[0]} vs {pair[1]}" if len(pair)==2 else pair[0] for pair in match_list]
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
                match_process(items, match_list,t)#processing the match


        elif user_input == "kill":
            break
        elif user_input == "save":
            print('Make a selection on the given files.')
            a,b = Repository.check() #getting a list of occupied playerfiles and a list of empty playerfiles
            display_delayed_msg('')
            generate_report(a,b)
            while True:
                user_input = input('>>')
                if user_input in a:
                    Repository.save(t,user_input)
                    print('File saved successfully. Closing in 1.5 seconds')
                    display_delayed_msg('')
                    return #stops the function, break all loops
                elif user_input in b:
                    print('File chosen already contains tournament data. Would you like to replace it?')
                    user_input = input('>>')
                    if user_input.lower() == 'yes':
                        Repository.save(t,user_input)
                        if verify_saving(t,user_input):#verifying if file has been saved correctly
                            print('File saved successfully.')
                        return
                else:
                    print('Please make a valid file choice.')

        else:
            print('Please make an appropriate selection of the following mentioned above.')





#main while-loop
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
print('To begin, type "start", "help", or "view" in the command line')
user_input = input('>>')

while True:
    if user_input.lower() == "start":
        start_tournament()
        continue_tournament()
        #once continue_tournament() ends, the while loop breaks and the whole program ends.
        break
    elif user_input.lower() == "help":
        print('Are you that dense mate? Just start the program.')
        break
    elif user_input.lower() == "view":
        #continue working here.
        pass
    else:
        print('Please make an appropriate selection. Type "start" or "help" in the command line')
        user_input = input('>>')


