def evaluate_cost(squareFeets , gallonPrice):
  #Const  labor_per_hour = $20
  labour_per_hour = 20
  #if 115 square_feet = 1 galon and 8 hours. 
  #gallons per square feet  = (1/115)
  gallons_per_feet = 1 / 115

  #Time taken per sqauare feet = 8 / 115
  time_per_squarefeet = 8/115
  
  #check if  value of gallons required is less than 1  and set gallons to one
  if squareFeets * gallons_per_feet < 1: 
    number_of_gallons = 1
  else:
  #If gallon is greater than 1 round, set number of gallons to the nearest whole number. 
    number_of_gallons = round((squareFeets * gallons_per_feet))

  #if hours < 1 round the number of hours to 2 decimal places
  if squareFeets * time_per_squarefeet < 1:
    number_of_hours = round((squareFeets * time_per_squarefeet), 2)
  else:
    #if hours not less than 1 round hours to the nearest whole number
    number_of_hours = round(squareFeets * time_per_squarefeet)
  #formular for cost of paint 
  cost_of_paint = number_of_gallons * gallonPrice
  #formular for cost of labo
  labour_cost = number_of_hours * 20
  #formular for the total cost of labour
  total_labour_cost = ( number_of_gallons * gallonPrice ) + (number_of_hours * labour_per_hour)

  #Print out information
  print(f"\nThe number of gallons of paint required\n{number_of_gallons} gallon(s)\n")
  print(f"The hours of labor required\n{number_of_hours} hours\n")
  print(f"The cost of the paint\n${cost_of_paint:.2f}\n")
  print(f"The labor charges\n${labour_cost:.2f}\n")
  print(f"The total cost of the paint job\n${total_labour_cost:.2f}\n")
