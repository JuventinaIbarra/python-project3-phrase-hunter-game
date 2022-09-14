import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
        "I love winter",
        "Now or never",
        "Just be you",
        "Dream but dont sleep",
        "Girls just wanna have fun"
        ]
        self.active_phrase = None
        self.user_phrase = []
        self.guesses = []
        self.continue_game = True


    def start(self):
        self.get_random_phrase()
        self.welcome()
        while self.continue_game:
            self.active_phrase.display(self.user_phrase, self.guesses)
            self.get_guess()
            #the len(self.guesses)-1 checks whether the last letter added to the list is in the active_phrase
            if self.active_phrase.check_letter(self.guesses[len(self.guesses)-1]):
                self.user_phrase.append(self.guesses[len(self.guesses)-1])
                if self.active_phrase.check_complete(self.guesses):
                    self.active_phrase.display(self.user_phrase, self.guesses)
                    self.game_over()
                else:
                    print("wow, another letter down, let's go for the win\n")
            else:
                self.missed += 1
                self.num_lives_left(self.missed)


    def get_random_phrase(self):
        self.active_phrase = Phrase(self.phrases[random.randint(0,4)])
        return self.active_phrase


    def welcome(self):
        print("*********************************************************************")
        print("*******                                                       *******")
        print("*******              Welcome to PHRASE HUNTERSSS              *******")
        print("*******                                                       *******")
        print("*******  Where all your favorite game quotes can kill you ;)  *******\n")


    def get_guess(self):
        try:
            user_letter_guess = input("What letter would you like to try?\n").lower()
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            #this is the validation to make sure the user input is:
            #1 letter long, it is a letter and it hasn't been tried before
            if len(user_letter_guess) == 1 and user_letter_guess in alphabet and user_letter_guess not in self.guesses:
                self.guesses.append(user_letter_guess)
                self.guesses.sort()
            else:
                raise ValueError
        except:
            print("OPSS.... that doesn't seem to be a single letter or you've tried this letter already, please try again\n")
            self.get_guess()


    def num_lives_left(self, missed):
        if self.missed < 4:
            print(f"Ouch, that hurt, only {5-self.missed} lives left\n")
        elif self.missed == 4:
            print(f"Ouch, that hurt, only {5-self.missed} life left, make it count!\n")
        else:
            self.game_over()


    def game_over(self):
        if self.missed < 5:
            print("Congratulations you've won!\n")
            self.continue_game = False
            self.try_again()
        else:
            #https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
            print ("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
You just died!!!\n""")
            self.continue_game = False
            self.try_again()


    def try_again(self):
        try:
            try_again = input("Would you like to play again... (y)es or (n)o\n").lower()
            if try_again in ["y", "yes"]:
                self.missed = 0
                self.active_phrase = None
                self.user_phrase = []
                self.guesses = []
                self.continue_game = True
                self.start()
            elif try_again in ["n" or "no"]:
                print("Thank you very much for playing Phrase Hunters")
            else:
                raise ValueError
        except:
            print("You seem to have filled in something other than (y)es or (n)o. Please try again")
            self.try_again()
