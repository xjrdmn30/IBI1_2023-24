# Prompt the user to input their birth year
born_year = input("Write your birth year: ")
# Define a function to determine the favorite James Bond actor based on the user's birth year
def favorite_james_bond(born_year):
    # Dictionary containing James Bond actors and the years they played the role
    james_bond = {
        "Roger Moore": (1973, 1986),
        "Timothy Dalton": (1987, 1994),
        "Pierce Brosnan": (1995, 2005),
        "Daniel Craig": (2006, 2021)
    }
    # Iterate through the dictionary
    for actor, (start_year, end_year) in james_bond.items():
        # Check if the user would have been 18 or older when the actor played Bond
        if start_year <= int(born_year) + 18 < end_year:
            # Return the name of the actor as the user's favorite Bond actor
            return f"Your favorite Bond actor is {actor}."
    
    # If no suitable actor is found, return a default message
    return "No favorite Bond actor."
# Call the function and print the result
print(favorite_james_bond(born_year))
