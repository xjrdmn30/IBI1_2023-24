total_money=float(input("please write the money you have: "))
price=float(input("please write the price of one chocolate bar: "))
def buy_number(total_money, price) :
    number=int(total_money/price)
    return number
number =buy_number(total_money, price)
print(number)
