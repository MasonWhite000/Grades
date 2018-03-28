
number_of_sets = int(input("How many grade sets would you like to enter?: "))

for i in range(number_of_sets):
    number_of_grades = int(input("How many grades would you like to enter for set " + str(i + 1) + "?: "))
    grades = []
    average = 0
    if number_of_grades == 0:
        print ("A set cannot have 0 grades!")
        exit()
    else:
        for i in range(number_of_grades):
            try:
                x = int(input("Enter a grade: "))
            except ValueError:
                print ("That wasn't an integer!")
                print ("Please retart the program!")
                exit()
            grades.append(x)
            average = average + x
        average = average / number_of_grades

        if average < 60:
            print ("You have an averge of an F :(")
        elif average >= 60 and average < 70:
            print ("You have an average of a D :(")
        elif average >= 70 and average < 80:
            print ("You have an aaverage of a C :(")
        elif average >=80 and average < 90:
            print ("You have an average of a B!")
        elif average >=90:
            print ("You have an average of an A!")
    
        average = ("Average; " ,average)
        print (average)
        grades.append(average)
        print (grades)
