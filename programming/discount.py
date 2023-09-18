from datetime import datetime

DISC = 0.10
TAX = 0.06

subtotal = float(input('Please enter the subtotal: '))
current_time = datetime.now()
current_day = current_time.weekday()

discount = (subtotal * DISC)
sales_tax = round(subtotal * TAX)
total = subtotal + sales_tax


if subtotal >= 50 and (current_day == 1 or current_day == 2):
    print(f'Discount amount: {discount:.2f}')
    print(f'Sales tax amount: {sales_tax}')
    print(f'Total: {total - discount}')
else:
    print(f'Sales tax amount: {sales_tax}')
    print(f'Total: {total}')


