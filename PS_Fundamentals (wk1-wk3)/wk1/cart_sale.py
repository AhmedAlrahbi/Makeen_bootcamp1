#PS_in-class-activity, cart sale problem
total_sum=0
while True:
    number = int(input("Enter the item values of your purchases (If done enter 0): $"))
    if number == 0:
        break
    total_sum += number
    shoppingCartTotal = total_sum

if shoppingCartTotal > 100 :
    sale  = shoppingCartTotal* (90 / 100)

else:
    sale  = shoppingCartTotal* (95 / 100)
print("Your total is", shoppingCartTotal,", And the new sale is $", sale)