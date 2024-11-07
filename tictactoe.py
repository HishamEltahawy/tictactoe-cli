"""
WELCOME IN TIC-TAC-TOE GAME !

Components of the game:
    1- board
    2- players
    3- menu
    4- game logic
Game Logic:
    1- run the app
    2- main menu
    3- game start, quit the game
    4- player1 name & symbol, player2 name & symbol
    5- board is displayed
    6- game loop until win or draw
    7- restart game, quit game
"""

class Player: # Combosition with Game
    def __init__(self):
        self.name = ""
        self.symbol= ""
    def Choose_name(self):
        while True:
            inputName= input("Type your name: ")
            if inputName.isalpha() and len(inputName) >= 2:
                self.name = inputName
                break
            else:
                print("invalid choice make sure your name is letters only and equal or more than 2 letters")
    def Choose_symbol(self):
        while True:
            inputSymbol= input("Type your symbol: ")
            if inputSymbol.isalpha() and len(inputSymbol) == 1:
                self.symbol = inputSymbol
                break
            else:
                print("invalid choice make sure your symbol is letters only and it's length equals 1")

class Board:
    def __init__(self):
        self.board= [str(i) for i in range(1, 10)] 
    def Display_board(self):
        for i in range(0,len(self.board),3):
            print("|".join(self.board[i:i+3]))
            if i <9:              
                print("-" * 5) 
    def Update_board(self, move, symbol):
        self.board[move- 1] = symbol if self.Is_valid_move() == True else print("This place is busy")
    def Is_valid_move(self, move):
        return self.board[move-1].isdigit()
    def Reset_board(self):
        self.board= [str(i) for i in range(1, 10)]

class Menu(): # Composition with Game
    def Start_menu(self) -> str:
        menu1Choice= input("""1- Start game
2- Quit game""")
        while True:
            if menu1Choice.isdigit() and len(menu1Choice) == 1:
                return
    def End_menu(self) -> str:
        menu1Choice= input("""1- Restart game
2- Quit game""")
        while True:
            if menu1Choice.isdigit() and len(menu1Choice) == 1:
                return        

class Game:
    pass



x = Board.Display_board()

