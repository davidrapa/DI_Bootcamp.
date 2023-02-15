import random

def get_random_temp(season):
    if season == "winter":
        lower_limit = -10
        upper_limit = 16
    elif season == "spring":
        lower_limit = 4
        upper_limit = 23
    elif season == "summer":
        lower_limit = 18
        upper_limit = 40
    else:
        lower_limit = 0
        upper_limit = 20

    return round(random.uniform(lower_limit, upper_limit), 1)

def main():
    month = int(input("Enter the number of the month (1-12): "))
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    else:
        season = "autumn"

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp < 24:
        print("The temperature is moderate today.")
    elif temp < 32:
        print("It's quite warm outside.")
    else:
        print("It's very hot outside! Drink plenty of water.")

if __name__ == '__main__':
    main()