from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




###############################SAVE THESE TWO TABLES FOR LAST#################################################


# enrollments:  make a Many-to-Many association table between students and courses named enrollments
# please enter your foreign key in the variable below for the seeder file.
STUDENT_COURSE_FK = "your_foreign_key_here"




###                                         your code here.






#Make a  Many-to-Many association table between teachers and students named teacher_student_association
#note- it is not plural



###                                             your code here.






#students should have a many to many relationship with courses.
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)





##############courses should have a One-to-Many relationship with teacher##########################
#fill out the table as normal, then update line immediately below for the seeders.
COURSE_TEACHER_FK = "your_other_foreign_key_here"


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)




#teachers have a one to many relationship with courses. (think of each course as "algebra 101 taught at 8 am, etc.)
# teachers should also have a many to many relationship with students


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
