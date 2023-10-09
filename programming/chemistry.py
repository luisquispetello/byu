from formula import parse_formula


def main():
  # Get a chemical formula for a molecule from the user.

  # Get the mass of a chemical sample in grams from the user.

  # Call the make_periodic_table function and
  # store the periodic table in a variable.

  # Call the parse_formula function to convert the
  # chemical formula given by the user to a compound
  # list that stores element symbols and the quantity
  # of atoms of each element in the molecule.

  # Call the compute_molar_mass function to compute the
  # molar mass of the molecule from the compound list.

  # Compute the number of moles in the sample.

  # Print the molar mass.

  # Print the number of moles.

  formula = input('Enter the chemical formula: ')
  mass = float(input('Enter the mass in grams of the sample: '))

  periodic_table = make_periodic_table()
  symbol_quantity = parse_formula(formula, periodic_table)

  total_molar_mass = compute_molar_mass(symbol_quantity, periodic_table)
  number_moles_sample = mass / total_molar_mass

  print(f'{total_molar_mass} grams/mole')
  print(f'{number_moles_sample:.5f} moles')


def make_periodic_table():
  periodic_table_list = {}

  with open('periodic_table.py') as chemistry_table:
    next(chemistry_table)

    for elements in chemistry_table:
      row = elements.split(',')

      symbol = row[0].strip('"')
      name = row[1].strip().strip('"')
      atomic_mass = float(row[2].strip())

      array_atomic = [name, atomic_mass]
      periodic_table_list[symbol] = array_atomic
  
  return periodic_table_list


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
  """Compute and return the total molar mass of all the
  elements listed in symbol_quantity_list.

  Parameters
      symbol_quantity_list is a compound list returned
          from the parse_formula function. Each small
          list in symbol_quantity_list has this form:
          ["symbol", quantity].
      periodic_table_dict is the compound dictionary
          returned from make_periodic_table.
  Return: the total molar mass of all the elements in
      symbol_quantity_list.

  For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
  this function will calculate and return
  atomic_mass("H") * 2 + atomic_mass("O") * 1
  1.00794 * 2 + 15.9994 * 1
  18.01528
  """
  # Do the following for each inner list in the
  # compound symbol_quantity_list:
      # Separate the inner list into symbol and quantity.
      # Get the atomic mass for the symbol from the dictionary.
      # Multiply the atomic mass by the quantity.
      # Add the product into the total molar mass.

  total_molar_mass = 0

  for letter, number in symbol_quantity_list:
    name_atom = periodic_table_dict[letter]
    molar_mass = name_atom[1] * number
    total_molar_mass += molar_mass

  # Return the total molar mass.
  return total_molar_mass


if __name__ == '__main__':
  main()