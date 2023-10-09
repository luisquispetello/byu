
def main():
  formula = input('Enter the chemical formula: ')
  mass = float(input('Enter the mass in grams of the sample: '))

  periodic_table = make_periodic_table()

  for element in periodic_table:
    symbol, name, atomic_mass = element
    print(f'{name}: {atomic_mass}')




def make_periodic_table():
  periodic_table_list = []

  with open('table.py') as chemistry_table:
    next(chemistry_table)

    for elements in chemistry_table:
      row = elements.split(',')

      symbol = row[0].replace('"', '')
      name = row[1].strip().replace('"', '')
      atomic_mass = float(row[2].strip())

      trimmed_row = [symbol, name, atomic_mass]
      periodic_table_list.append(trimmed_row)
  
  return periodic_table_list


if __name__ == '__main__':
  main()