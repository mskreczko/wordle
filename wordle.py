import random
import typing
import string


class Wordle:
  def __init__(self, words_filename):
    self.words = open(words_filename, 'r').read().splitlines()
  
  def get_word(self) -> str:
    return random.choice(self.words).lower()

  def validate_user_input(self, guess: str) -> bool:
    if len(guess) != 5:
      return False
    return True

  def get_word_from_user(self) -> str:
    x = input("Your guess: ")
    while self.validate_user_input(x) is False:
      print("Invalid input, try again!")
      x = input("Your guess: ")
    return x.lower()
 
  def find_all_char_positions(self, word: str, char: str) -> typing.List[int]:
    positions = []
    pos = word.find(char)
    while pos != -1:
      positions.append(pos)
      pos = word.find(char, pos + 1)
    return positions
  
  # _ is empty space
  # * is correct letter but in the incorrect place
  def play(self):
    won = False
    guess = ['_', '_', '_', '_', '_']
    counted_pos = set()
    win_word = self.get_word()
    print(win_word)
    for i in range(0, 6):
      user_guess = self.get_word_from_user()
      if user_guess == win_word:
        won = True
        print("Bravo! You have won!")
        break

      for i, (expected, guessed) in enumerate(zip(win_word, user_guess)):
        if expected == guessed:
          guess[i] = expected
          counted_pos.add(i)
      
      for i, guessed in enumerate(user_guess):
        if guessed in win_word and guess[i] not in string.ascii_lowercase:
          positions = self.find_all_char_positions(win_word, guessed)
          for pos in positions:
            if pos not in counted_pos:
              guess[i] = '*'
              counted_pos.add(pos)
              break
      print("".join(guess))
    if won is False:
      print(f"You lost!\nCorrect word was: {win_word}")


game = Wordle("sgb-words.txt")
game.play()
      

