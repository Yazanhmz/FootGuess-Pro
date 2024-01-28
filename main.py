import random

def choose_random_player():
    players = [
        {"name": "Messi", "country": "Argentina", "club": "Inter Miami"},
        {"name": "Ronaldo", "country": "Portugal", "club": "Al Nassr"},
        {"name": "Neymar", "country": "Brazil", "club": "Al Hilal"},
        {"name": "Mbappe", "country": "France", "club": "Paris"},
        {"name": "Lewandoski", "country": "Poland", "club": "Barcelona"},
        {"name": "De Bruyne", "country": "Belgium", "club": "Manchester City"}, 
        {"name": "Salah", "country": "Egypt", "club": "Liverpool"},
        {"name": "Pedri", "country": "Spain", "club": "Barcelona"},
    ]
    return random.choice(players)

def ask_for_guess(attribute, player):
    max_attempts = 2
    for attempt in range(max_attempts, 0, -1):
        guess = input(f"Guess the {attribute} of {player['name']}: ").lower()
        if guess == player[attribute].lower():
            print(f"Congratulations! You guessed it. {player['name']}'s {attribute} is {player[attribute]}.")
            return 1
        else:
            print(f"Incorrect. {'Attempts' if attempt > 1 else 'Attempt'} left: {attempt - 1}")

    print(f"Sorry, you've run out of attempts. The correct answer is {player[attribute]}.")
    return 0

def play_guessing_game():
    score_part1 = score_part2 = 0
    total_questions = 3  

    print("Welcome to FootGuess-Pro!")

    for _ in range(total_questions):
        selected_player = choose_random_player()

        score_part1 += ask_for_guess('country', selected_player)
        score_part2 += ask_for_guess('club', selected_player)

    print(f"\nGame Over!\nPart 1 Score: {score_part1}/{total_questions}\nPart 2 Score: {score_part2}/{total_questions}")

if __name__ == "__main__":
    play_guessing_game()
