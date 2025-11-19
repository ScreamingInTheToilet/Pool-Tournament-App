from prototype import Tournament
from storage import Repository
import time
import sys


#let's create a tournament by creating a Tournament object

t1 = Tournament("swimming contest",["Srinjoy","Olivia","Samuel","Jacob","Hieu","QM"])

def start_tournament():
    
    pass

text = """
████████╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗███╗   ██╗████████╗
╚══██╔══╝██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
   ██║   ██║   ██║██║   ██║██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
   ██║   ██║   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
   ██║   ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ██╔╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
"""
print(text)

for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print() #move the cursor to the next line
print('Hello user, welcome to the versatile TOURNAMENT console')

time.sleep(0.5)
print('To begin, type "start" or "help" in the command line')
user_input = input('>>')

while True:
    if user_input.lower() == "start":
        start_tournament()
        break
    elif user_input.lower() == "help":
        print('Are you that dense mate? Just start the tournament.')
        break
    else:
        print('Please make an appropriate selection. Type "start" or "help" in the command line')
        user_input = input('>>')

