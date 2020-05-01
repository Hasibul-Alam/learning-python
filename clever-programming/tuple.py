t = (1, 2, 3)
print(t[1])

credit_card1 = (3485689655846877, 'Hasibul Alam', '12/21', 457)
credit_card2 = (3485689655846899, 'Hasinur Alam', '12/22', 557)

credit_card = [credit_card1, credit_card2]
print(credit_card)

card_no, name, exp_date, pin = credit_card1

print(card_no)
print(name)
print(exp_date)
print(pin)

print('-----------+++++++++++----------')
for card_no, name, exp_date, pin in credit_card:
    print('Card No:',card_no)
    print('Name:',name)
    print('Expire Date:',exp_date)
    print('Pin:',pin)
    print()
