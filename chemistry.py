import os


def make_periodic_table():
        
        
        periodic_table_list = {
            'Ac': ['Actinium', 227],
            'Al': ['Aluminum', 26.9815386],
            'Sb': ['Antimony', 121.76],
            'Ar': ['Argon', 39.948],
            'As': ['Arsenic',74.9216],
            'At': ['Astatine', 210],
            'Ba': ['Barium',137.327],
            'Be': ['Beryllium', 9.012182],
            'Bi': ['Bismuth', 208.9804],
            'B' : ['Boron', 10.811],
            'Br': ['Bromine',79.904],
            'Cd': ['Cadmium', 112.411],
            'Ca': ['Calcium', 40.078],
            'C' : ['Carbon', 12.0107],
            'Ce': ['Cerium', 140.116],
            'Cs': ['Cesium', 132.9054,9],
            'Cl': ['Chlorine', 35.453],
            'Cr': ['Chromium', 51.9961],
            'Co': ['Cobalt', 58.933195],
            'Cu': ['Copper', 63.546],
            'Dy': ['Dysprosium', 162.5],
            'Er': ['Erbium', 167.259],
            'Eu': ['Europium', 151.964],
            'F' : ['Fluorine', 18.9984032],
            'Fr': ['Francium', 223],
            'Gd': ['Gadolinium', 157.25],
            'Ga': ['Gallium', 69.723],
            'Ge': ['Germanium', 72.64],
            'Au': ['Gold', 196.966569],
            'Hf': ['Hafnium', 178.49],
            'He': ['Helium', 4.002602],
            'Ho': ['Holmium', 164.93032],
            'H' : ['Hydrogen', 1.00794],
            'In': ['Indium', 114.818],
            'I' : ['Iodine', 126.90447],
            'Ir': ['Iridium', 192.217],
            'Fe': ['Iron', 55.845],
            'Kr': ['Krypton', 83.798],
            'La': ['Lanthanum', 138.90547],
            'Pb': ['Lead', 207.2],
            'Li': ['Lithium', 6.941],
            'Lu': ['Lutetium', 174.9668],
            'Mg': ['Magnesium', 24.305],
            'Mn': ['Manganese', 54.938045],
            'Hg': ['Mercury', 200.59],
            'Mo': ['Molybdenum', 95.96],
            'Nd': ['Neodymium', 144.242],
            'Ne': ['Neon', 20.1797],
            'Np': ['Neptunium', 237],
            'Ni': ['Nickel', 58.6934],
            'Nb': ['Niobium', 92.90638],
            'N' : ['Nitrogen', 14.0067],
            'Os': ['Osmium', 190.23],
            'O' : ['Oxygen', 15.9994],
            'Pd': ['Palladium', 106.42],
            'P' : ['Phosphorus', 30.973762],
            'Pt': ['Platinum', 195.084],
            'Pu': ['Plutonium', 244],
            'Po': ['Polonium', 209],
            'K' : ['Potassium', 39.0983],
            'Pr': ['Praseodymium', 140.90765],
            'Pm': ['Promethium', 145],
            'Pa': ['Protactinium', 231.03588],
            'Ra': ['Radium', 226],
            'Rn': ['Radon', 222],
            'Re': ['Rhenium', 186.207],
            'Rh': ['Rhodium', 102.9055],
            'Rb': ['Rubidium', 85.4678],
            'Ru': ['Ruthenium', 101.07],
            'Sm': ['Samarium', 150.36],
            'Sc': ['Scandium', 44.955912],
            'Se': ['Selenium', 78.96],
            'Si': ['Silicon', 28.0855],
            'Ag': ['Silver', 107.8682],
            'Na': ['Sodium', 22.98976928],
            'Sr': ['Strontium', 87.62],
            'S' : ['Sulfur', 32.065],
            'Ta': ['Tantalum', 180.94788],
            'Tc': ['Technetium', 98],
            'Te': ['Tellurium', 127.6],
            'Tb': ['Terbium', 158.92535],
            'Tl': ['Thallium', 204.3833],
            'Th': ['Thorium', 232.03806],
            'Tm': ['Thulium', 168.93421],
            'Sn': ['Tin', 118.71],
            'Ti': ['Titanium', 47.867],
            'W' : ['Tungsten', 183.84],
            'U' : ['Uranium', 238.02891],
            'V' : ['Vanadium', 50.9415],
            'Xe': ['Xenon', 131.293],
            'Yb': ['Ytterbium', 173.054],
            'Y' : ['Yttrium', 88.90585],
            'Zn': ['Zinc', 65.38],
            'Zr': ['Zirconium', 91.224]
        }

        periodic_table_list
        return periodic_table_list

def get_symbol_of_the_table(ask,quantify):

        #If one element of the library is the same to the choose
        if ask in make_periodic_table():
        
            ################################## Get values ##############################################  
            list_of_values = make_periodic_table()[ask]
            symbol = ask
            name = list_of_values[0]
            atomic_mass = list_of_values[1]
            ################################################################################################    

            result = atomic_mass * int(quantify)
            print('')
            print(f"The symbol of the element is: {symbol}")
            print(f"The name of the element is: {name}")
            print(f"The atomic mass of the element is: {atomic_mass}")
            print('')
            #Return the atomic_mass
            return result  
class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule. For example, this function will convert
    "H2O" to [["H", 2], ["O", 1]] and
    "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]

    Parameters
        formula: a string that contains a chemical formula
        periodic_table_dict: the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index<len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elem_dict, symbol):
        return 0 if symbol not in elem_dict else elem_dict[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula,index+1,level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    curr = prev + group_dict[symbol] * quant
                    elem_dict[symbol] = curr
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError("invalid formula, "
                            f"unknown element symbol: {symbol}",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError("invalid formula, "
                        "unmatched close parenthesis",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError("invalid formula, "
                "unmatched open parenthesis",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


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
    
    # Do the following for each each inner list in the
    # compound symbol_quantity_list:
    total_mass_between_atoms = 0
    for element in symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        symbol = element[0]
        quantity_of_atoms = element[1]
        # Get the atomic mass for the symbol from the dictionary.
        atomic_mass = periodic_table_dict[symbol][1]
        # Multiply the atomic mass by the quantity.
        multiply_the_atoms = quantity_of_atoms * atomic_mass
        # Add the product into the total molar mass.
        total_mass_between_atoms = total_mass_between_atoms + multiply_the_atoms
    # Return the total molar mass.
    return total_mass_between_atoms

def main():
    make_periodic_table()

    os.system('cls')
    print('')
    print("Welcome to the number of mole's calculator")
    print('')
            
    #Total of the atoms (atomic mass)
    total_mass_between_atoms = 0
    #Default values
    molar_mass = 0
    sample_mass_kg = 0
    number_of_moles = 0

    #Loop to sum the total of the atom's mass that the scientific needs
    another_choose = input("Do you like to add an element? [Yes/No] ").capitalize()
    while another_choose != "No":
        
        if another_choose =="Yes":
            ask = input("Choose the symbol of the element? (Example: 'Zn'): ").capitalize() #Preguntar por un elemento de la lista 
            quantify = input("Choose the number of the atoms: ")
            total_mass_between_atoms = total_mass_between_atoms + get_symbol_of_the_table(ask,quantify) 
            print(f'The total atomic mass is: {total_mass_between_atoms:.5f} grams/mole')
            another_choose = input("Do you like to add another element? [Yes/No] ").capitalize()

        elif another_choose != "Yes" or another_choose != "No":
            print('')
            print("Wrong answer. Try again.")
            another_choose = input("Do you like to add another element? [Yes/No] ").capitalize()
        
    #Change the variable's name and get the rest of the formula
    print('')
    molar_mass = total_mass_between_atoms
    sample_mass = float(input("Choose the sample mass of the molecule in kilograms: [example: 15] ")) 
    sample_mass_kg = sample_mass * 1000
    number_of_moles =  sample_mass_kg / molar_mass

    #Print the result
    print('')
    print(f"The number of moles in {sample_mass_kg:.5f} grams of that molecule is: {number_of_moles:.5f} moles")
    print('')
    reset = (input("Do you like to use again?")).capitalize()
    
    #Loop to reset the program with the values in 0 or not
    while reset != "No":
        
        if reset =="Yes":
            main()
            break

        elif reset != "Yes" or reset != "No":
            print('')
            print("Wrong answer. Try again.")
            reset = (input("Do you like to use again?")).capitalize()
    
    #When the user decided to quit the program
    print("Thanks for use our number of mole's calculator")



# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()