current_year=int(input("Enter current year:"))
birth_year=int(input("Enter birth year:"))

def age_calculator(current_year,birth_year):
    
   age = current_year - birth_year
   print("The age of the person in years is",age,"years")

age_calculator(current_year,birth_year)
