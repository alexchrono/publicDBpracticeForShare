from sqlalchemy.orm import aliased
from app.factory import create_app, db
from app.models import Student, Course, Teacher
import warnings
from sqlalchemy.exc import SAWarning
import random
warnings.filterwarnings('ignore', category=SAWarning)

app = create_app()

'''
WELCOME TO OUR EXERCISE.

step 1: If you see a venv file to the side, delete it by entering
rm -r venv in the terminal. Then run: pipenv install -r requirements.txt

step 2: Open the app/models.py file. It tells you what kind of relationship to establish for each one.
Establish those relationships, then come back here and complete the exercises below.
Run python GOHERE.py to test your queries.
'''

############ Make a query to retrieve all students and all courses each student is enrolled in. ####################
def studentsWithCourses():
    # Your code here
    pass

############ Make a query to retrieve all teachers and the courses they teach. ####################
def teachersWithCourses():
    # Your code here
    pass

############ Make a query to retrieve all courses taught by a specific teacher given their name. ####################
def coursesTaughtByTeacher(teacher_name):
    # Your code here
    pass


##### feel free to make your own queries below#####################################



#                      your code here






########## run python GOHERE.py to test your queries.  if they are succesful, they will print out.
# ##############   you will have to add code if you want to print out your custom queries.
















if __name__ == "__main__":
    with app.app_context():  # Wrap your function calls with this
        print('Teachers with courses*****************')
        teachers_result = teachersWithCourses()
        if teachers_result:
            print(teachers_result)
        else:
            print("Incomplete or error in teachersWithCourses function.")
        print(' ')
        print(' ')
        print(' ')

        print('Students with courses*******************')
        students_result = studentsWithCourses()
        if students_result:
            print(students_result)
        else:
            print("Incomplete or error in studentsWithCourses function.")
        print(' ')
        print(' ')
        print(' ')

        # Get all teacher names from the database
        all_teachers = db.session.query(Teacher.name).all()

        # If there are no teachers, print an appropriate message
        if not all_teachers:
            print("No teachers found in the database.")
            exit(0)

        # Randomly choose a teacher's name
        teacher_name_to_query = random.choice(all_teachers)[0]

        # Test the one-to-many relationship between teacher and course
        teacher_courses = coursesTaughtByTeacher(teacher_name_to_query)
        if teacher_courses:
            print(f"Courses taught by {teacher_name_to_query}: {teacher_courses}")
        else:
            print(f"Incomplete or error in coursesTaughtByTeacher function for teacher: {teacher_name_to_query}")
