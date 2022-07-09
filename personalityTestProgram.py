def bookClub():
  #Print out book club name
    print("Welcome to Serendipity Book Club".center(60 , " "))
    print("-"  * 60, "\n")
  #Set default score to zero  
    points = 0
  #Print out select options
    print("""Enter the number of books bought within the month:\n
        1.I haven't bought a book this month\n
        2.I have bought 1 book this month\n
        3.I have bought 2 books this month\n
        4.I have bought 3 books this month\n
        5.I have bought 4 or more books this month\n\n""")
    while True:
      #Ask the user to enter the number of books bought within the month
      choice = input("Enter your response : ")
      #Check if number entered is not numerical. Alert user and ask for their input again
      if not choice.isdigit():
        print("Number of books bought must be numerical!")
        continue
      #Else convert choice to int
      choice  = int(choice)
      #if choice is  0 point - 0 
      if choice == 0:
        points = 0
        break
      #if choice is  1 point = 6 
      if choice == 1:
          points = 6
          break 
      #if choice is  2 point = 16
      elif choice == 2 :
          points += 16
          break   
      #if choice is  3 point = 32
      elif choice == 3:
          points +=32
          break
      #if choice is greater than 3 ie 4 or more...set point to 60
      else:
          points +=60
          break
      #Print score
    print("Your points for the month is", points) 
    print("-"  * 60, "\n\n")
