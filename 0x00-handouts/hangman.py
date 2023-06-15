import random

def main():
  """Enter point to Hangman"""
  hangman()

def hangman():
  word_list = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grapefruit"]
  word = random.choice(word_list)
  guessed_letters = []
  attept = 6

  print("welcome to hangman!")
  print("_" * len(word))

  while attempts > 0;
      guess = imput("Enter a letter: ").lower
      if len(guess) != 1:
        print("please enter a singal letter. ")
        continue

      if guess in guessed_letter:
        print("you have already guessed that letter. Try Again")
        continue

      if guess not in word:
        attempt -= 1 # attempts = attempts - 1
        print("Incorrect guess. You Have", attempts, "Attempts left")
      else:
          guessed_letters.append(guess)

      word_progress = ""
      for letter in word:
        word_progress += letter + ""
      else:
        word_progress += "_"
        print(word_progress)

      if"_" not in word_progress:
        print("Congregation! you have guess the word correcly. ")
        return
      print("you run out of attempts. The word was, ${word}")

if __name__ == "__main__":

         