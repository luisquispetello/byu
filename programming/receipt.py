import csv
from datetime import datetime


def main():
  current_date_and_time = datetime.now().strftime("%c")

  try:
    products_dict = read_dictionary('products.csv', 0)
  except FileNotFoundError:
    print("Error: 'product.csv' not found.")

  try:
    with open('request.csv', 'r') as csv_file:
      csv_reader = csv.reader(csv_file)
      next(csv_reader)

      num_items = 0
      subtotal = 0

      print('Inkom Emporium')
      print('')

      for row in csv_reader:
        product_num = row[0]
        product_quantity = int(row[1])
        if product_num in products_dict:
          product_name = products_dict[product_num][1]
          product_price = float(products_dict[product_num][2])
        else:
          print(f'Error: Product with key {product_num} not found.')
          continue

        num_items = num_items + product_quantity
        total_product_price = product_quantity * product_price
        subtotal = subtotal + total_product_price
        print(f'{product_name}: {product_quantity} @ {product_price}')

      sales_tax = subtotal * 0.06
      total = subtotal + sales_tax

      print('')
      print(f'Number of Items: {num_items}')
      print(f'Subtotal: {subtotal:.2f}')
      print(f'Sales Tax: {sales_tax:.2f}')
      print(f'Total: {total:.2f}')
      print('')
      print('Thank you for shopping at the Inkom Emporium')
      print(f"{current_date_and_time}")
  except FileNotFoundError:
    print("Error: 'request.csv' not found.")
  except PermissionError:
    print("Permission denied.")



def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.

  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """

  dictionary = {}

  with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
      key = row[key_column_index]
      product_num = row[0]
      product_name = row[1]
      product_price = float(row[2])
      
      value = [product_num, product_name, product_price]
      dictionary[key] = value
    
  return dictionary


if __name__ == '__main__':
  main()