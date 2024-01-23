import random

class FootballPlayer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

def choose_random_player():
    players = [
        FootballPlayer("Messi", "Argentina"),
        FootballPlayer("Ronaldo", "Portugal"),
        FootballPlayer("Neymar", "Brazil"),
        FootballPlayer("Mbappe", "France"),
        FootballPlayer("Lewandoski", "Poland"),
        FootballPlayer("De Bruyne", "Belgium"), 
        FootballPlayer("Salah", "Egypt"),
    ]
    return random.choice(players)

def play_guessing_game():
    selected_player = choose_random_player()

    print("Welcome to the Football Player Country Guessing Game!")
    print(f"Guess the country of {selected_player.name}.")

    while True:
        guessed_country = input("Your guess: ")

        if guessed_country.lower() == selected_player.country.lower():
            print(f"Congratulations! You guessed it. {selected_player.name} is from {selected_player.country}.")
            break
        else:
            print("Incorrect. Try again!")

if __name__ == "__main__":
    play_guessing_game()
