from UI_BlackJack import UI
from art import art
from dictionary_cards import cards_packed

#TODO Add .lower()

game_betting = True

start = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")

if start == 'yes':
    print(art)
    print('Shuffling!')
    Game = UI(1000, 10)
    dealer_cards = []


    def our_game():
        print(f"Your balance = ${Game.Bank}")
        print(f"Your bet = ${Game.Bet}")
        print(f'On the table {Game.Amount_cards} cards')

        Game.take_cards_for_user()
        Game.dealer_take_cards()

        flag_game = True
        temp = Game.user_score
        user_blackjack = False
        computer_blackjack = False

        while flag_game:
            print(f"Your cards are: {Game.user_cards} and score = {Game.user_score}")
            print(f"Dealer cards are: {Game.dealer_cards}")
            print(f'Now, on table {Game.Amount_cards} cards')

            if Game.user_score == 21:
                print()
                print('Blackjack!')
                print()
                user_blackjack = True
                flag_game = False
            else:
                what_to_do = input("If you want to hit, type 'hit', if you want to stand, "
                                   "type 'stand', if you want to x2 your bet, then type 'x2':\n")

                if what_to_do == 'hit':
                    Game.hit_card()
                    if Game.user_score > 21:
                        print(f'You lost, your cards = {Game.user_cards} and '
                              f'score = {Game.user_score} that more than 21')

                        temp = Game.user_score
                        Game.user_score = 0
                        flag_game = False
                    else:
                        temp = Game.user_score

                        print(f'Your score = {temp}')

                elif what_to_do == 'stand':
                    flag_game = False

                elif what_to_do == 'x2':
                    if Game.Bet * 2 > Game.Bank:
                        print(f"You don't have enough funds ${Game.Bet * 2}, you have "
                              f"only ${Game.Bank}")
                    else:
                        Game.x2_bet()
                        if Game.user_score > 21:
                            temp = Game.user_score

                            print(f'You lost, your cards = {Game.user_cards} and '
                                  f'score = {temp} that more than 21')

                            Game.user_score = 0
                            flag_game = False
                        else:
                            print(f'Your score = {Game.user_score}')

                        flag_game = False

                else:
                    print("You've choose wrong command!")

        Game.dealer_takes_second_card()

        if Game.deal_score == 21:
            print()
            print('Computer got blackjack!')
            print()
            computer_blackjack = True

        if user_blackjack and computer_blackjack == False:
            print('Blackjack! You won!')
            Game.Bank += round(Game.Bet*1.5)
            Game.obnulate()

        elif user_blackjack and computer_blackjack:
            print('Both blackjack! Draw.')
            Game.obnulate()

        elif user_blackjack == False and computer_blackjack:
            print('Computer got Blackjack! You lost.')
            Game.Bank -= Game.Bet
            Game.obnulate()

        else:
            Game.dealer_takes_cards()

        if computer_blackjack == False and user_blackjack == False:
            if Game.user_score > Game.deal_score:
                print(f"Your score - {temp}, dealer score - {Game.deal_lose_score}")
                print('You won!')

                Game.Bank += Game.Bet
                Game.obnulate()

            elif Game.user_score == Game.deal_score:
                print(f"Your score - {temp}, dealer score - {Game.deal_lose_score}")
                print('Draw')

                Game.obnulate()

            else:
                print(f"Dealer score - {Game.deal_score}, you lost, because your "
                      f"score - {temp} ")

                Game.Bank -= Game.Bet
                Game.obnulate()


    while game_betting:

        if Game.Amount_cards > 40:
            pass
        else:
            print('Shuffling')
            Game.cards = cards_packed.copy()
            Game.Amount_cards = len(Game.cards)
            print(cards_packed)

        if Game.Bank >= 5:
            pass
        else:
            print(f"You lost all of your money, your bank = {Game.Bank}, game over!")
            game_betting = False

        print(f"Your balance = {Game.Bank}")

        choose = input(f"Your bet = {Game.Bet}, if you want to increase bet, type 'increase',"
                       f" if reduce, type 'reduce', if you want to go all-in, type "
                       f"'all-in', if you want to cash-out, then type 'cash-out', "
                       f"if you want to start game with your bet, type 'start':\n")
        if choose == 'start':
            our_game()
        elif choose == 'increase':
            try:
                number = int(input('How much do you want to increase your bet? $'))
            except Exception:
                print('You must put number!')
            else:
                if (Game.Bet + number) <= Game.Bank:
                    Game.increase(number)
                else:
                    print(f'Your balance = ${Game.Bank} and balance less than your new '
                          f'bet: ${Game.Bet} + ${number} = ${Game.Bet + number}')

        elif choose == 'all-in':
            ask = input("Are you sure that you want to go all-in? Type 'yes' or 'no': ")

            if ask == 'yes':
                Game.Bet = Game.Bank
                our_game()

        elif choose == 'reduce':
            num = int(input('How much do you want to reduce your bet $'))
            Game.reduce(num)

        elif choose == 'cash-out':
            Game.cash_out()
            game_betting = False

else:
    print('If you want to comeback, just reload app!')
