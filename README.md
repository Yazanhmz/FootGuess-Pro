# Football Quiz
Football countries guessing game
## Setup
- Run the code
- Play the game!
- Guess the countries of the players
- Get your score
- Share the game with your friends.
## Press run to start game

import random

class FootballPlayer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

def choose_random_player(category):
    if category == "current":
        players = [
            FootballPlayer("Messi", "Argentina"),
            FootballPlayer("Ronaldo", "Portugal"),
            FootballPlayer("Neymar", "Brazil"),
            FootballPlayer("Mbappe", "France"),
            FootballPlayer("Haaland", "Norway"),
            FootballPlayer("Lewandoski", "Poland"),
        ]
    elif category == "old":
        players = [
            FootballPlayer("Pele", "Brazil"),
            FootballPlayer("Maradona", "Argentina"),
            FootballPlayer("Zidane", "France"),
            FootballPlayer("Beckenbauer", "Germany"),
            FootballPlayer("Cruyff", "Netherlands"),
        ]
    return random.choice(players)

def play_game(category):
    score = 0
    num_questions = 3 

    print(f"\nPart: {category.capitalize()} Football Player Country Guessing Game!")

    for _ in range(num_questions):
        selected_player = choose_random_player(category)

        print(f"\nGuess the country of {selected_player.name}.")

        guessed_country = input("Your guess: ")

        if guessed_country.lower() == selected_player.country.lower():
            print(f"Congratulations! You guessed it. {selected_player.name} is from {selected_player.country}.")
            score += 1
        else:
            print("Incorrect.")

    return score

if __name__ == "__main__":
    overall_score = 0
    overall_score += play_game("current")
    overall_score += play_game("old")

    print(f"\nOverall Score: {overall_score}")
