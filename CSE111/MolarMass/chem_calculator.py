
#Import the periodic table
from chem_constants import ELEMENTS

class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """
    pass


def parse_formula(formula, periodic_table):
    """Convert a chemical formula for a molecule into a compound list
    that stores the quantity of atoms of each element in the molecule.
    For example, this function will convert "H2O" to [["H", 2], ["O", 1]]
    and "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]
    """
    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elems, symbol):
        return 0 if symbol not in elems else elems[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elems = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group, index = parse_r(formula, index + 1, level + 1)
                quant, index = parse_quant(formula, index)
                for symbol in group:
                    prev = get_quant(elems, symbol)
                    elems[symbol] = prev + group[symbol] * quant
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table:
                        index += 1
                    else:
                        # Unknown symbol for an element
                        raise FormulaError("invalid formula:", formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elems, symbol)
                elems[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    # Mismatched close parenthesis
                    raise FormulaError("invalid formula:", formula, index)
                level -= 1
                index += 1
                break
            else:
                # Illegal character: [^()0-9a-zA-Z] or decimal digit not
                # preceded by an element symbol or close parenthesis
                raise FormulaError("invalid formula:", formula, index)
        if level > 0 and level >= start_level:
            # Mismatched open parenthesis
            raise FormulaError("invalid formula:", formula, start_index - 1)
        return elems, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elems, _ = parse_r(formula, 0, 0)
    return list(elems.items())


# These are the indexes of the
# elements in the periodic table.


def compute_molar_mass(symbol_quantity_list, periodic_table):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list. Each element in
    symbol_quantity_list is a list in the form: ["symbol", quantity].

    As an example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    molar_mass = 0
    for symbol,number in symbol_quantity_list:
        molar_mass += periodic_table[symbol][1] * number

    return molar_mass

    


def main():
    formula_message = "Please enter the chemical formula:\n>"
    mass_message = "Please enter the sample mass in grams:\n>"

    #Obtain chemical formula from user 
    #Asks for a new formula if the parse_formula function raises an error
    formula_check = True
    while formula_check:
        try:
            formula = input(formula_message)
            parsed_formula = parse_formula(formula, ELEMENTS)
            formula_check = False
        except:
            print("Invalid Formula")

    #Obtain sample mass from the user. 
    #Asks for a different input if the given input is not a floating point number. 
    mass_check = True
    while mass_check:
        try:
            mass = float(input(mass_message))
            mass_check = False
        except:
            print("Invalid mass")

    #Compute molar mass of compound formula and the number of moles in the given mass. 
    formula_mm = compute_molar_mass(parsed_formula,ELEMENTS)
    moles = mass / formula_mm

    #print the output
    print(f"Molar mass of compound: {formula_mm:.5f} grams/mole.\nMoles of sample: {moles:.3e}")
    
main()