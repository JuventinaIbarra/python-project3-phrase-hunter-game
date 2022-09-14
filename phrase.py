import game


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.display_phrase = []


    def __str__(self):
        return self.phrase


    def __iter__(self):
        yield from self.phrase


    def display(self, phrase, guesses):
        if guesses:
            print(f"So far you've tried the follower letters: {', '.join(guesses).upper()}")
        self.display_phrase = []
        for letter in self.phrase:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if letter in alphabet and letter not in guesses:
                letter = "_ "
                self.display_phrase.append(letter)
            else:
                letter = letter + " "
                self.display_phrase.append(letter)
        print(''.join(self.display_phrase))


    def check_letter(self, guesses):
        if guesses in self.phrase:
            return True
        else:
            return False


    def check_complete(self, guesses):
        check_complete_bool_list = []
        for letter in self.phrase.replace(" ",""):
            if letter in guesses:
                check_complete_bool_list.append(True)
            else:
                check_complete_bool_list.append(False)
        #https://stackoverflow.com/questions/31099561/test-if-all-elements-of-a-python-list-are-false
        return all(check_complete_bool_list)
