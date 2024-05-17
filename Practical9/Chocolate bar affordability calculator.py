# Prompt the user to input the total amount of money they have
total_money = float(input("Please write the money you have: "))
# Prompt te user to input the price of one chocolate bar
price = float(input("Please write the price of one chocolate bar: "))
# Define a function to calculate the maximum number of chocolate bars that can be bought
def buy_number(total_money, price):
    # Calculate the maximum number of chocolate bars that can be bought
    number = int(total_money / price)
    # Return the calculated number
    return number
# Call the function and store the result in the 'number' variable
number = buy_number(total_money, price)
# Print the maximum number of chocolate bars that can be bought
print(number)
