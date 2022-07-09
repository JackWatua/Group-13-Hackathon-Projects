career = ['Lawyer','Doctor/Pharmacist','Architecture/Physical Planner','Teacher/lecturer','Psychology','Lab Technician/Scientist']
career_questions = ['Which field interest you most\n1.Law and Philosophy\n2.Public Health and Medecine\n3.Built Environment and Real Estate Management\
    \n4.Early Chilhood Education and Teaching\n5.Understanding Human Behaviour\n6.chemical reactions','Favourite subjects\n1.maths\n2.sciences\n3.Humanities\n4.Languages']
def careerPath():
    print("Career planner".center(60, " "))
    print("-"  * 60, "\n")
    while True:
        print(career_questions[0])
        choice = eval(input("Enter your choice: "))
        print(career_questions[1])
        choice2 = eval(input("Enter your choice: "))
        if choice  == 1:
            if choice2  == 3 and 4:
                print("Your best career path is",career[0])
            else:
                print('The above Subject is not suitable for this course,\
                \nthis course takes Humanity and Languages')    
            break

        elif choice == 2:
            if choice2 == 2 and 1:
                print("Your best career path is",career[1])
            else:
                print('The above Subject is not suitable for this course,\
                \nthis course takes Sciences and Maths')     
            break
        elif choice == 3:
            if choice2 == 3 and 1 and 2:
                print("Your best career path is",career[2])
            else:
                print('The above Subject is not suitable for this course,\
                \nthis course takes Humanities,sciences and Maths')     
            break
        elif choice == 4:
            if choice2 == 4 and 3:
                print("Your best career path is",career[3])
            print('The above Subject is not suitable for this course,\
                \nthis course takes Humanities and Languages')    
            break
        elif choice == 5:
            if choice2 == 2 and 3:
                print("Your best career path is",career[4])
            print('The above Subject is not suitable for this course,\
                \nthis course takes Humanities and sciences.')    
            break
        elif choice == 6:
            if choice2 == 2 and 1:
                print("Your best career path is",career[5])
            print('The above Subject is not suitable for this course,\
                \nthis course takes sciences and Maths')    
            break
        else:
            print('Error!!Wrong input')    

    print("Thank you for consulting us,you are welcomed again")
    print("-"  * 60, "\n\n")
