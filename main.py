import datetime
from bus_fare_challenge import determine_fare
from sales_tax import evaluate_cost
from personalityTestProgram import bookClub
from careerChallenge import careerPath
from doorChallenge import door_locker
from day_3_challange import callories_calculator

def challange_navigator():
  #A function that prints out all challanges
  def display_main_menu():
      print("""Main Menu\n
        1. Day 1  challenges
        2. Day 2 challenges
        3. Day 3 challanges
        4. Exit
        """)

  #A function that dislays soecific challanges for each day
  def display_specific_menu(menu):
    if menu == "Day 1":
      print("""
      1. Bus_fare challenge
      2. Sales tax challenge
      3. Exit
      """)
    elif menu == "Day 2":
      print("""
      1. Personality test program
      2. Career program
      3. Exit
      """)
    else:
      print("""
      1. Door lock system 
      2. Callories calculator
      3. Exit
      """)  
  #Print group logo 
  print(f"{'_' * 30}Group 13 (254Corders){'_' * 30}\n")
  #call display main options 
  

  
  while True:
    display_main_menu()
    choice  = input("Choose an option to navigate : ")
    if choice not in ['1', '2', '3', '4']:
      print("Invalid choice. Choose 1, 2 or 3 or 4")
      continue
    if choice == '1':    
      print("Day one Challenges")
      display_specific_menu("Day 1")
      while True:
        choice  = input("Choose an option to navigate : ")
        if choice not in ['1', '2', '3']:
          print("Invalid choice. Choose 1, 2, or 3")
          display_specific_menu("Day 1")
          continue
        if choice == "1":
          day_1 = datetime.date.today()
          determine_fare(day_1)
        elif choice == "2":
          print("Evaluate cost of paintinng".center(60, " "))
          print("-"  * 60, "\n")
          while True:
            #Ask the user to enter square feets and number of gallons
            squareFeets = input("Enter the square feets you wish to paint : ")
            gallons = input("Enter the price of one gallon : ")

            if not squareFeets.isdigit() or not gallons.isdigit():
              print("Square feet and gallons must be numerical")
              continue
            squareFeets =int(squareFeets)
            gallons = int(gallons)
            #call evealuate cost function and pass user input ( square feets and price per gallon)
            evaluate_cost(squareFeets, gallons)
            break
        else:
          print("You exited day 3 challenges\n")
        break
        print("Evaluate cost of paintinng".center(60, " "))
      print("-"  * 60, "\n")
        
    elif choice == '2':
      print("Day two Challenges")
      display_specific_menu("Day 2")
      while True:
        choice  = input("Choose an option to navigate : ")
        if choice not in ['1', '2', '3']:
          print("Invalid choice. Choose 1, 2, or 3")
          display_specific_menu("Day 2")
          continue
        if choice == "1":
          bookClub()
        elif choice == "2":
          careerPath()
        else:
          print("You exited day 2 challaneges.\n")
        break
    elif choice == '3':
      print("Day three Challenges")
      display_specific_menu("Day 3")
      while True:
        choice  = input("Choose an option to navigate : ")
        if choice not in ['1', '2', '3']:
          print("Invalid choice. Choose 1, 2, or 3")
          display_specific_menu("Day 3")
          continue
        if choice == "1":
          door_locker()
        elif choice == "2":
          callories_calculator()
        else:
          print("You exited day 3 challanges\n")
        break
    else:
      print("Bye bye...")
      break

challange_navigator()
