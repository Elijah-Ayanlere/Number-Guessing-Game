import random
import time

def apply_mystery_modifier(number):
    modifier = random.randint(-10, 10)
    modified_number = number + modifier
    return modified_number

def number_guessing_game():
    time.sleep(1)
    print("\nWelcome to the Unique Number Guessing Game!")
    
    time.sleep(0.5)
    difficulty = input("\nSelect difficulty (easy, medium, hard): ").lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        time.sleep(1)
        print("\nInvalid difficulty. Defaulting to medium.")
        difficulty = 'medium'

    while True:
        # Difficulty-specific settings
        difficulty_settings = {
            'easy': (1, 50, 15),
            'medium': (1, 100, 10),
            'hard': (1, 200, 8)
        }

        min_range, max_range, max_attempts = difficulty_settings[difficulty]
        
        time.sleep(1)
        print(f"\nI have chosen a number between {min_range} and {max_range}. Can you guess it?")
        time.sleep(0.5)
        print("\nHere's a unique twist: You have a secret weapon - the 'Hint Coin'!")

        secret_number = apply_mystery_modifier(random.randint(min_range, max_range))
        
        attempts = 0
        start_time = time.time()
        hint_coins = 3

        while attempts < max_attempts:
            try:
                time.sleep(0.5)
                guess = int(input("\nEnter your guess: "))

                if guess == secret_number:
                    end_time = time.time()
                    elapsed_time = round(end_time - start_time, 2)
                    time.sleep(1)
                    print(f"\nCongratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.")
                    time.sleep(0.5)
                    print(f"\nElapsed time: {elapsed_time} seconds.")
                    
                    # Ask if the player wants to play the Wildcard Round
                    time.sleep(0.5)
                    play_wildcard = input("\nDo you want to play the Wildcard Round? (yes/no): ").lower()
                    if play_wildcard == 'yes':
                        wildcard_number = random.randint(min_range, max_range)
                        time.sleep(1)
                        print("\nWelcome to the Wildcard Round!")
                        time.sleep(0.5)
                        print(f"\nI have chosen a second number between {min_range} and {max_range}. Can you guess it for bonus points?")
                        
                        wildcard_attempts = 0
                        while wildcard_attempts < 3:
                            try:
                                time.sleep(0.5)
                                wildcard_guess = int(input("\nEnter your Wildcard guess: "))

                                if wildcard_guess == wildcard_number:
                                    time.sleep(1)
                                    print(f"\nCongratulations! You guessed the Wildcard number {wildcard_number} and earned bonus points!")
                                    break
                                else:
                                    time.sleep(0.5)
                                    print("\nIncorrect! Try again.")
                                
                                wildcard_attempts += 1
                                time.sleep(0.5)
                                print(f"\nAttempts left: {3 - wildcard_attempts}")
                            except ValueError:
                                time.sleep(1)
                                print("\nInvalid input. Please enter a valid number.")

                        else:
                            time.sleep(1)
                            print(f"\nSorry, you've run out of Wildcard attempts. The correct Wildcard number was {wildcard_number}.")
                    
                    # Ask if the player wants to continue
                    time.sleep(0.5)
                    play_again = input("\nDo you want to play again? (yes/no): ").lower()
                    if play_again != 'yes':
                        time.sleep(1)
                        print("\nThanks for playing! Goodbye.")
                        return
                    else:
                        break
                    
                elif guess < secret_number:
                    time.sleep(0.5)
                    print("\nToo low! Try a higher number.")
                else:
                    time.sleep(0.5)
                    print("\nToo high! Try a lower number.")

                attempts += 1
                time.sleep(0.5)
                print(f"\nAttempts left: {max_attempts - attempts}")

                # Offer a hint using the 'Hint Coin'
                if hint_coins > 0:
                    time.sleep(0.5)
                    use_hint = input("\nWould you like to use a Hint Coin? (yes/no): ").lower()
                    if use_hint == 'yes':
                        time.sleep(1)
                        hint_coins -= 1
                        time.sleep(0.5)
                        print(f"\nHint: The correct number is {'even' if secret_number % 2 == 0 else 'odd'}.")
                        time.sleep(0.5)
                        print(f"\nYou have {hint_coins} Hint Coin(s) remaining.")
            
            except ValueError:
                time.sleep(1)
                print("\nInvalid input. Please enter a valid number.")

        else:
            print(f"\nSorry, you've run out of attempts. The correct number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
