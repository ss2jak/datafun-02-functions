"""
Jakiel David  1/21/2023

Always start with a docstring that describes what the module does.
Include your name and the date.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
###Write and call 3 functions here atleast 1 should use math module eg math.fsum()
import math
def monthly_visitors(yearly_visitors,month):
    """"Calculates the monthly visitors to Trinidad based on stastic 1.562m pop"""
    return math.ceil(yearly_visitors/12 * month)

def population_density(population, area):
    """Calculates the population density of Trinidad"""
    return population / area

def usd_to_ttd(amount, rate):
    """Convert US dollar  to Trinidad & Tobago Dollar"""
    try:
        result = amount * rate
    except Exception as ex:
        print()
        print(f"Error: {ex}")
        return None
    finally:
        print("Currency conversion complete.")
    return result









# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()
    print(f"math.comb(5,3) = {math.comb(5,3)}")
    print(f"math.perm(5,3) = {math.perm(5,3)}")
    print()
    print("area of lot")
    print(get_area_of_lot(6, 2))
    print()
    print("Trinidad_monthly_visitors:", monthly_visitors(1526000,1))
    print()
    print("Population density:", population_density(1526000, 1920))
    print()                             
    print("Convert USD to Trinidad & Tobago Dollars")
    print(usd_to_ttd(1,6.79))
    print(usd_to_ttd("1",6.79))
                     
   