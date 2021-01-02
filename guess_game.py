class GuessNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = mx

    def get_guesses(self):
        guess = input(f"Please guess a number between ({self.min} - {self.max}): ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number.")
            return self.get_guesses()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False
        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guesses()

            if guess < self.number:
                print("Your guess is too low.")
            elif guess > self.number:
                print("Your guess is too high.")
            else:
                break
        print(f"You guessed the number in {self.guesses} guesses.")


game = GuessNumber(56, 0, 100)
game.play()
