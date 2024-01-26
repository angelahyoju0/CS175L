#Angela An
#CS 175L 02
#26 January 2024

#Stocks Assignment

commission_rate = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
commission_sale = float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
shares_purchased = float(input("Enter number of shares purchased: "))
shares_sold = float(input("Enter number of shares sold: "))
purchase_price = float(input("Enter purchase price per share: "))
sell_price = float(input("Enter sell price per share: "))

stock_price = shares_purchased * purchase_price
commission_purchase = commission_rate * stock_price
amount_sold = sell_price * shares_sold
commission_paid = commission_sale * amount_sold
profit_or_loss = amount_sold - stock_price - commission_purchase - commission_paid


print()
print(f'Amount paid for the stock: ${stock_price:,.2f}')
print(f'Commission paid on the purchase: ${commission_purchase:,.2f}')
print(f'Amount the stock sold for: ${amount_sold:,.2f}')
print(f'Commission paid on the sale: ${commission_paid:,.2f}')
print(f'Profit (or loss if negative): ${profit_or_loss:,.2f}')
