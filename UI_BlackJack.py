from random import choice
from dictionary_cards import cards_packed
from dictionary_cards import dictionary_of_cards_packed



class UI:
    cards = cards_packed.copy()
    dictionary_of_cards = dictionary_of_cards_packed

    user_cards = []
    dealer_cards = []

    user_score = 0
    deal_score = 0
    deal_lose_score = 0

    Amount_cards = len(cards)

    def __init__(self, bank, bet):
        self.Bank = bank
        self.Bet = bet

    def increase(self, value):
        if self.Bet + value <= self.Bank:
            self.Bet += value
        else:
            pass

    def reduce_bet(self, value):
        if self.Bank >= self.Bet:
            self.Bet -= value
        else:
            print("You don't have enough funds")

    def reduce(self, value):
        if self.Bet - value >= 5:
            self.Bet -= value
        else:
            print('Minimum bet is $5! Now your bet = $5')
            self.Bet = 5

    def all_in(self):
        self.Bet = self.Bank
        print(f'Your bet = ${self.Bet}')
        return self.Bet

    def cash_out(self):
        if self.Bank >= 1000:
            print(f"You've cashed out and increased Bank to ${self.Bank}, your "
                  f"profit is ${self.Bank-1000} ")
        else:
            print(f"You've cashed out and reduced the Bank to ${self.Bank}, your "
                  f"lose is ${1000-self.Bank}$ ")

    def take_card(self):
        a = choice(self.cards)
        self.cards.remove(a)
        self.Amount_cards -= 1
        return a

    def take_second_deal_card(self):
        a = choice(self.cards)
        self.cards.remove(a)
        return a

    def check_card(self, card):
        try:
            card.isalpha()
        except:
            temporary = card
        else:
            temporary = self.dictionary_of_cards.get(card)
        return temporary

    def take_cards_for_user(self):
        first = self.take_card()
        second = self.take_card()

        self.user_cards.append(first)
        self.user_cards.append(second)

        b = self.check_card(first)
        c = self.check_card(second)

        self.user_score += b
        self.user_score += c

    def dealer_take_cards(self):
        deal_first = self.take_card()
        self.dealer_cards = [deal_first, '_']
        df = self.check_card(deal_first)
        self.deal_score += df
        self.Amount_cards -= 1

    def hit_card(self):
        new_card = self.take_card()
        self.user_cards.append(new_card)
        temp = self.check_card(new_card)
        self.user_score += temp

    def x2_bet(self):
        self.Bet *= 2
        x2_deal = self.take_card()
        self.user_cards.append(x2_deal)
        b = self.check_card(x2_deal)
        self.user_score += b

        print(f"Your cards are: {self.user_cards} and score = {self.user_score}")

    def dealer_takes_second_card(self):
        deal_second = self.take_second_deal_card()
        self.dealer_cards[1] = deal_second
        ds = self.check_card(deal_second)
        self.deal_score += ds

    def obnulate(self):
        self.dealer_cards = []
        self.deal_score = 0
        self.user_score = 0
        self.user_cards = []
        self.Bet = 10

    def dealer_takes_cards(self):
        print(f"Dealer cards are: {self.dealer_cards} with score = {self.deal_score}")

        if self.deal_score < 11:
            temp1 = self.take_card()
            self.dealer_cards.append(temp1)
            temp2 = self.check_card(temp1)
            self.deal_score += temp2
            self.deal_lose_score = self.deal_score

        elif 11 <= self.deal_score < 16:
            temp1 = self.take_card()
            self.dealer_cards.append(temp1)
            temp2 = self.check_card(temp1)

            if temp2 == 11:
                temp2 = 1

            self.deal_score += temp2
            print(f"Dealer takes card and his cards: {self.dealer_cards} with score = {self.deal_score}")
            self.deal_lose_score = self.deal_score
            self.dealer_takes_cards()

        elif 16 <= self.deal_score <= 21:
            self.deal_lose_score = self.deal_score

        else:
            self.deal_lose_score = self.deal_score
            print(f"Dealer takes card and his cards: {self.dealer_cards} with score = {self.deal_score}")
            self.deal_score = 0

    def checker(self):
        if self.user_score > 21:
            print(f'You lost, your cards = {self.user_cards} and '
                  f'score = {self.user_score} that more than 21')
            self.user_score = 0

        else:
            print(f'Your score = {self.user_score}')