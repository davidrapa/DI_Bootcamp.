from game import Game

def get_user_menu_choice():
    while True:
        choice = input("Enter 'p' to play a new game, 's' to show scores or 'q' to quit: ")
        if choice.lower() in ("p", "s", "q"):
            return choice.lower()
        else:
            print("Invalid input. Please select 'p' to play a new game, 's' to show scores or 'q' to quit.")

def print_results(results):
    print("Results:")
    print(f"Win: {results['win']}")
    print(f"Loss: {results['loss']}")
    print(f"Draw: {results['draw']}")
    print("Thanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "p":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "s":
            print_results(results)
        else:
            print_results(results)
            break

if __name__ == "__main__":
    main()
