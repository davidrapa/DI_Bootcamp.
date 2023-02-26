import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Select rock, paper or scissors: ")
            if user_item.lower() in ("rock", "paper", "scissors"):
                return user_item.lower()
            else: https://github.com/camveff/DI-Bootcamp-Stage1/tree/main/week+8/day+3
                print("Invalid input. Please select rock, paper or scissors!.")

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        return random.choice(items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or (user_item == "paper" and computer_item == "rock") or (user_item == "scissors" and computer_item == "paper"): # there is no need for the elif, please change it with if because we are doing return line before
            return "win"
        else: # it's redundant, please remove
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}!")
        return result
