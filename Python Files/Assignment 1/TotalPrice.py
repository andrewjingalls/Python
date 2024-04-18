item_price=float(input('Enter price of the item: '))            #Asking for the price of item
sales_tax=float(input('Enter sales tax rate as decimal: '))     #Asking for sales tax rate
sales_tax_percentage=sales_tax/100                  #Converting sales tax rate to percentage
total_price=item_price*(1+sales_tax_percentage)     #Calculating total price by multiplying the item price by the sales tax percentage +1
total_price_formatted="{:.2f}".format(total_price)    #Formatting total price to 2 decimal places because it's in dollars
print('Total price of item is', total_price_formatted, 'dollars.')       #Outputting formatted total price
