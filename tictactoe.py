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
    6- game loop until win or draw (Play_game() method in Game class)
    7- restart game, quit game
"""
import os
import time

def Clean_screen():
    os.system("cls" if os.name == "nt" else "clean")

class Player: # Combosition with Game
    usedNameAndSymbol= []
    def __init__(self):
        self.name = ""
        self.symbol= ""
    def Choose_name(self):
        while True:
            inputName= input("Type your name: ")
            if inputName not in Player.usedNameAndSymbol and inputName.isalpha() and len(inputName) >= 2 :
                self.usedNameAndSymbol.append(inputName)
                self.name = inputName
                break
            else:
                print("invalid choice make sure your name is letters only and equal or more than 2 letters")
    def Choose_symbol(self):
        while True:
            inputSymbol= input("Type your symbol: ")
            if inputSymbol not in Player.usedNameAndSymbol and inputSymbol.isalpha() and len(inputSymbol) == 1 :
                self.usedNameAndSymbol.append(inputSymbol)
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
        # return (self.board.__setitem__(move - 1, symbol) or True) if self.Is_valid_move() else (print("This place is busy") or False)
        if self.Is_valid_move(move):
            self.board[move - 1] = symbol
            return True
        else:            
            return False
    def Is_valid_move(self, move):
        return self.board[move-1].isdigit()
    def Reset_board(self):
        self.board= [str(i) for i in range(1, 10)]

class Menu(): # Composition with Game
    def Start_menu(self) -> str:
        menu1Choice= input("""1- Start game
2- Quit game: """)
        while True:
            if menu1Choice.isdigit() and len(menu1Choice) == 1:
                return menu1Choice
    def End_menu(self) -> str:
        menu1Choice= input("""1- Restart game
2- Quit game: """)
        while True:
            if menu1Choice.isdigit() and len(menu1Choice) == 1:
                return menu1Choice    

class Game:
    def __init__(self):
        self.players= [Player(), Player()]
        self.board= Board()
        self.menu= Menu()
        self.currentPlayerIndex= 0
    def Start_game(self):
        getStartMenu= self.menu.Start_menu()    
        if getStartMenu == "1":
            self.Setup_players()
            self.Play_game()
        elif getStartMenu == "2":
            self.Quit_game()
        else:
            print("Invalid input just (1 or 2)")
    def Setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number} enter your details:")
            player.Choose_name()
            player.Choose_symbol()
            Clean_screen()
    def Play_game(self):
        while True:
            self.Play_turn()
            if self.Check_win() or self.Check_draw():
                getEndGamemenu= self.menu.End_menu()               
                if getEndGamemenu == "1":
                    self.Restart_game()     
                elif getEndGamemenu == "2":
                    self.Quit_game()
                    break   # back
                else:
                    print("invalid choice, make sure you input 1 or 2 only !")

    def Play_turn(self):
        Clean_screen()
        player = self.players[self.currentPlayerIndex]
        self.board.Display_board()
        print(f"{player.name} this is your turn >>")
        while True:
            try:
                choice = int(input("Choose a number (1-9)"))
                if 1<= choice  <= 9 and self.board.Update_board(choice, player.symbol):
                    break
            except ValueError:
                print("Invalid move, try again")
        self.Switch_player()
    def Switch_player(self):
        self.currentPlayerIndex = 1 - self.currentPlayerIndex
    def Check_win(self)-> bool:
        winsProbabilities= [
            [0,1,2], [3,4,5], [6,7,8], # rows
            [0,3,6], [1,4,7], [2,5,8], # colomn
            [0,4,8], [2,4,6]            #diagonals
        ]
        if True:
            for combo in winsProbabilities:
                if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                    print(f">> Congratulations '{self.board.board[combo[0]]}' you wins <<")
                    return True
        else:
            return False
        
    def Check_draw(self)-> bool:
        checkBoardList= [i for i in self.board.board if i.isdigit()]
        if len(checkBoardList) == 0:
            print(">> What! no one wins <<")
            return True
    def Restart_game(self):
        self.currentPlayerIndex= 0
        self.board.board= [str(i) for i in range(1, 10)]
        self.Play_game()
    def Quit_game(self):
        Clean_screen()
        print("Quiting The Game .")
        time.sleep(1)
        Clean_screen()
        print("Quiting The Game ..")
        time.sleep(1)
        Clean_screen()       
        print("Quiting The Game ...")
        time.sleep(1)
        Clean_screen()
        

OJ = Game().Start_game()
