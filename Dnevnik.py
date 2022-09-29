#Srednoaritmetichno za vsichki predmeti
def averageGradeF(z, x, c, v, b, n):
    return (z+x+c+v+b+n)/6

#klas student
class Person:
    #konstruktor
    def __init__(self, name, lastName, age, avg_grade, potential):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.avg_grade = avg_grade
        self.potential = potential

    #print F
    def printFunc(self):
        print("First name: ", self.name, "\n"
        "Last name: ", self.lastName, "\n"
        "Age: ", self.age, "\n"
        "Average Grade: ", self.avg_grade, "\n"
        "Potential: ", self.potential, "\n")

#Header
print("Enter The selected Students info: "
      "Type 'q' if u want to exit. ")

#Main info
first_Names = []
last_Names = []
age = []
avgGrades = []
potential = []

#Student Input Loop
studentNum = 1
while True:

    #All school classes
    math = 0
    english = 0
    history = 0
    geography = 0
    music = 0
    computerScience = 0

    print("Student number ", studentNum)
    print("First Name: ")
    fName = input()
    if fName == "q":
        break
    first_Names.append(fName)

    print("Last Name: ")
    lName = input()
    last_Names.append(lName)

    print("Age: ")
    ageI = int(input())
    age.append(ageI)

    print("Please enter the annual grades for the following classes: ")

    math = float(input("Math: "))
    if math > 6.00 or math < 2.00:
        #dopustimi stoinosti za ocenkite
        print("Invalid Grade. Try Again.")
        break

    english = float(input("English: "))
    if english > 6.00 or math < 2.00:
        print("Invalid Grade. Try Again.")
        break

    history = float(input("History: "))
    if history > 6.00 or math < 2.00:
        print("Invalid Grade. Try Again.")
        break

    geography = float(input("Geography: "))
    if geography > 6.00 or math < 2.00:
        print("Invalid Grade. Try Again.")
        break

    music = float(input("Music: "))
    if music > 6.00 or math < 2.00:
        print("Invalid Grade. Try Again.")
        break
    computerScience = float(input("Computer Science: "))
    if computerScience > 6.00 or math < 2.00:
        print("Invalid Grade. Try Again after restarting the program.")
        break
    avgGrades.append(averageGradeF(math, english, history, geography, music, computerScience))

    print("Enter potential from 'F' to 'A+' with capital letters: ")
    pot = input()
    #dopustimi stoinosti za potenciala
    if pot != "F" and pot != "D" and pot != "C" and pot != "B" and pot != "A":
            print("Invalid Potential. Try Again.")
            break
    potential.append(pot)

    studentNum += 1

#filling the Student list with obj
studentList = []
for x in range(studentNum-1):
    p1 = Person(first_Names[x], last_Names[x], age[x], avgGrades[x], potential[x])
    studentList.append(Person(first_Names[x], last_Names[x], age[x], avgGrades[x], potential[x]))

#Printing The Student list

print("The Student List contains the following people:")
counter = 1
for obj in studentList:
    print("Student number: ", counter)
    obj.printFunc()
    counter += 1