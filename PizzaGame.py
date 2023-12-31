print('Welcome to Pizza Game\n')

class Pizza:
    def __init__(self) -> None:
        self.price = 10

    def add_money(self, amount):
        add = int(amount)
        self.price += add


class Start:
    def choices(self) -> None:

        pizza = Pizza()
        user_choice1 = input('Pepp? ').lower()
        if user_choice1 == 'y':
          pizza.add_money(3)
        else:
          pass
        user_choice2 = input('Extra cheese? ').lower()
        if user_choice2 == 'y':
          pizza.add_money(1)
        else:
          pass
        user_choice3 = input('S, M, or L? ').lower()
        if user_choice3 == 'm':
          pizza.add_money(5)
        elif user_choice3 == 'l':
          pizza.add_money(10)
        else:
          pass
          
        print(f'Your final price will be {pizza.price}')


main = Start()
main.choices()
