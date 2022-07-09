import datetime

def door_locker():
  print("Door lock system".center(60, " ")) 
  print("-"  * 60, "\n")
  #Ask the user to enter a password
  username = input("Enter your Username: ")
  password = input("Enter your Password : ")
  confirm_password = ""
  password_attempt = 1
  is_locked = False
  
  while confirm_password != password and not(is_locked):#this condition checks if the password and password confirmation matches, it also checks if is_locked is false.
      if password_attempt <=3:#Number of attempts one has when entering their password
          confirm_password = input("Confirm your password: ")
          if confirm_password != password:
              print('Wrong Password try again')
      else:
          is_locked = True #when the password is wrong, password_attempt increases by one, when it hits three, the system is locked due to too many attemts
      password_attempt = password_attempt + 1
  
  if is_locked:
      print("Door is locked due to too many attempts")
    #if password attempts are exceeded, this the message output, but if password matches, the else part is executed
  else:    
      print("Login Successfull")  
      print("Click to open the door")
      
  while True:#this while condition executes the preceeding block of open and close door, if one wants to exit, the choose the quit optin in the last if part 
      click =input("Enter 'open' for door to open: ") 
      if click == 'open': 
          print("The door is now open")
          login_time = datetime.datetime.today()
          print(username,"just opened the door at",login_time)
  
  
      elif click == "open open":
          print("The door is already opened")
          login_time = datetime.datetime.today()
          print("you just opened the door at",login_time)
      else:
          print("You have entered the wrong input,Please try again")
          break  #if unepected input is given, the loop is exited  
  
      close_door = input("Enter 'close' to lock the door:")
      if close_door.lower() == 'close':
          print("The door is now locked")
          locked_time = datetime.datetime.today()
          print("The door was locked at",locked_time)
          
      elif close_door.lower() == "close close":
          print("The door is already locked")
          locked_time = datetime.datetime.today()
          print("The door was locked at",locked_time)
          print("The door was locked at",locked_time)
      else:
          print("You have entered the wrong input,Please try again")
          break  #if unepected input is given, the loop is exited   
      choice =input("would you like to quit?? 1.No 2.Yes: ")#this code allows one to either continue being in the loop or exit the entire proogram
      if choice == '1':
          print("Well you already in Enjoy your stay")
      elif choice== '2':
          print("you made your choice")     
          break 
      else:
          print("Wrong input") 
  print("Thanks for passing by, visit soon!")
  print("-"  * 60, "\n")



