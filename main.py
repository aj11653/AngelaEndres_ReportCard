# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

  print()


# Gets a valid float grade from the user
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val


# Create a list and dictionary for student names 

studentNames = []
students = {}

# Set variable as blank until further input
option = ""
# Continues through the options until the user selects quit
while(option != "6"):

  # Prompt the user to select an option
  print()
  displayMenu()
  option = input("Select an Option: ")

# This option will involve you adding a student and a collection for their grades to a dictionary!
  if (option == "1"):
    # Acquire new name
    studentName = input("Enter student name: ")
    # Add it to the list of names and create a dictionary entry
    studentNames.append(studentName)
    students[studentName] = []
    print(f"{studentName} as been added!")
# This option will involve you removing a student from the dictionary!
  elif (option == "2"):
    # Acquire name
    studentName = input("Enter student name: ")
    # If they're in the list, remove the key-value pair from the dictionary that has both their name and their grades
    if (studentName in studentNames):
      studentNames.remove(studentName)
      students.remove(studentName)
      print(f"{studentName} removed!")
    # If the student does not exist in the dictionary, it should tell the user other that they don't exist, rather than going through with the prompt
    elif (studentName not in students):
      print(f"{studentName} not in dictionary!")
    
# This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  elif (option == "3"):
    studentName = input("Enter a student name: ")
    if (studentName in students):
      # Input grade for the student
      studentGrade = getNumberGradeFromUser()
      # Add the grade to the student's list of grades
      students[studentName].append(studentGrade)
      # Affirm that the inputted grade was added
      print(f"Added {studentGrade} to {studentName}'s quizzes")
    # If the student does not exist in the dictionary, it should tell the user other that they don't exist, rather than going through with the prompt
    elif (studentName not in students):
      print(f"{studentName} not in dictionary!")
# This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  elif (option == "4"):
    studentName = input("Enter a student name: ")
    if (studentName in students):
      print(f"{studentName}'s Quizzes:")
      # Loop through each grade asssociated with the student name on separate lines
      for grade in students[studentName]:
        print(grade)
      if len(students[studentName]) == 0:
        print("None")
    # If the student does not exist in the dictionary, it should tell the user other that they don't exist, rather than going through with the prompt
    elif (studentName not in students):
      print(f"{studentName} not in dictionary!")
  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  elif (option == "5"):
    studentName = input("Enter a student name: ")
    if (studentName in students):
      # Find the average of all grades in the student's collection
      studentGrade = 0
      numberOfGrades = 0
      for grade in students[studentName]:
        studentGrade += grade
        numberOfGrades += 1
      studentAverage = studentGrade / float(numberOfGrades)
      # Convert the average to a letter grade with the following grading scale
      if(studentAverage >= 90):
        print("A")
      elif(studentAverage >= 80):
        print("B")
      elif(studentAverage >= 70):
        print("C")
      elif(studentAverage >= 60):
        print("D")
      elif(studentAverage >= 50):
        print("E")
      elif(studentAverage < 50):
        print("F")
    # If the student does not exist in the dictionary, it should tell the user other that they don't exist, rather than going through with the prompt
    elif (studentName not in students):
      print(f"{studentName} not in dictionary!")
  # Ends the program
  elif (option == "6"):
    print("Have a nice day!")
  
