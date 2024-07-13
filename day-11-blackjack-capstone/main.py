import random
from replit import clear
from drawing import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(card_list):
    score = sum(card_list)
    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)
    return score

def blackjack(balance):
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    game_end = False 
    while not game_end:
        if user_score >= 21:
            game_end = True
        else:
            user_choice = input("Type 'y' to get another card or type 'n' to pass: ")
            if user_choice == 'n':
                game_end = True
            else:
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")

        while computer_score < 17 and not game_end:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            if computer_score >= 21:
                game_end = True

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if user_score > 21:
        print("You went over. You lose.\U0001F622")
        return -1
    elif computer_score > 21 or user_score > computer_score:
        print("You win!!!\U0001F600")
        return 1
    elif user_score < computer_score:
        print("You lose.\U0001F622")
        return -1
    else:
        print("It's a draw.\U0001F610")
        return 0

def manage_money(balance, result, bet):
    if result == 1:
        balance += bet
    elif result == -1:
        balance -= bet
    return balance

user_choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'no': ")
if user_choice == 'y':
    clear()
    print(logo)
    balance = 100  # Initial balance
    playing = True
    while playing:
        bet = int(input(f"Your current balance is ${balance}. How much would you like to bet? "))
        if bet > balance:
            print("You don't have enough money to make that bet.")
            continue
        result = blackjack(balance)
        balance = manage_money(balance, result, bet)
        print(f"Your new balance is ${balance}.")
        if balance <= 0:
            print("You have run out of money! Game over.")
            playing = False
        else:
            playing = input("Do you want to play another round? Type 'y' or 'no': ") == 'y'
else:
    print("FINE!!! Don't play\U0001F620")
