
def callories_calculator():
  print("Check your calories".center(60, " "))
  print("-"  * 60, "\n")
  while True:
    #ask the user to enter grams of fats
    fat_grams = input("Enter the amont of fats (in grams) consumed : ")
    #ask the user to enter gramms of carbs
    cabrbohydrate_grams = input("Enter the amount of carbohydrates (in grams) consumed: ")
    #check if user input is not numerical
    if not fat_grams.isdigit() or not cabrbohydrate_grams.isdigit():
      print("Fat and Carbohydrates grams must be numerical")
      continue
    fat_grams = int(fat_grams)
    cabrbohydrate_grams = int(cabrbohydrate_grams)
    #formula for calculating calories from fats
    calories_from_fats = fat_grams * 9
    #fornula for calculating calories fron carbs
    calories_from_carbohydrates =  cabrbohydrate_grams * 4
    print(f"\nCalories from fat")
    print(f"{calories_from_fats} calories\n")
    print(f"\nCalories from carbohydartes")
    print(f"{calories_from_carbohydrates} calories\n")
    print(f"\nTotal calories")
    print(f"{calories_from_fats + calories_from_carbohydrates} calories\n\n")
    print("-"  * 60,"\n")
    break


