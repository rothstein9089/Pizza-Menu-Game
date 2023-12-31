
print('Welcome To The Pizza Game. Make an order and get a final price! \n')

pepp = input('Do you want pepperoni? Y or N?: ').lower()
extra_cheese = input('Extra cheese? Y or No?: ').lower()
s_m_or_large = input('S, M or L pizza?: ').lower()


final_price = 0

if s_m_or_large == 's':
    final_price += 10

elif s_m_or_large == 'm':
    final_price += 15

else:
    final_price += 20

if extra_cheese == 'y':
    final_price += 1
else:
    pass

if pepp == 'y':
    final_price += 3
else:
    pass

print(f'Your final price will be ${final_price}')
