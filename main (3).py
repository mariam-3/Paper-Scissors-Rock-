#Mariam
import random



print('Welcome to Human vs. Computer in Scissors, Paper, Rock!')
print('Moves: choose scissors, paper or rock by typing in your selection. Rules: scissors cuts paper, paper covers rock and rock crushes scissors.Good luck!')
rounds = int(input('How many rounds would you like to play?'))

    
class Player():
  def __init__(self, name, move, score):
    self.name = name
    self.move = None
    self.score = 0
  def add_win()
  def set_move(self, new_move):
    self.move = new_move

choice_list=['Scissors','Rock','Paper']
choice = random.choice(choice_list)

for i in range(rounds):
  Computer = Player('computer', choice)
  Computer.set_move(choice)
  Person = Player('Person', None)
  Person.move = input('Choose your move. Will it be rock, paper or scissors?')

  print('computer played', Computer.move)
  print('human played', Person.move)
  
  class Game():
    def __init__(self, Player_1, Player_2):
      self.Player_1 = Player_1
      self.Player_2 = Player_2
      self.Win_moves = {'Scissors':'Paper', 'Paper':'Rock', "Rock":'Scissors'}
  
  game = Game(Person, Computer)
  if Person.move == Computer.move:
    print('There is no winner')
  elif game.Win_moves[Person.move] == Computer.move:
    print(' You win!')
  elif game.Win_moves[Computer.move] == Person.move:
    print('The computer won. Good luck next time!')

print('Thank you for playing!')