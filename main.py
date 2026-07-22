# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse
# from pydantic import BaseModel
# import sqlite3


# app = FastAPI()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def home():
#     return FileResponse("frontend.html")


# # Database
# conn = sqlite3.connect("school.db", check_same_thread=False)
# cursor = conn.cursor()


# # Students table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER
# )
# """)


# # Courses table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS courses(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     price INTEGER
# )
# """)


# # Enrollments table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS enrollments(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     student_id INTEGER,
#     course_id INTEGER,
#     FOREIGN KEY(student_id) REFERENCES students(id),
#     FOREIGN KEY(course_id) REFERENCES courses(id)
# )
# """)


# conn.commit()


# # Models

# class Student(BaseModel):
#     name: str
#     age: int


# class Course(BaseModel):
#     title: str
#     price: int


# class Enrollment(BaseModel):
#     student_id: int
#     course_id: int


# @app.post("/students")
# def create_student(student: Student):

#     cursor.execute(
#         "INSERT INTO students(name, age) VALUES(?, ?)",
#         (student.name, student.age)
#     )

#     conn.commit()

#     return {"message": "Student Created"}




# @app.get("/students")
# def get_students():

#     cursor.execute("SELECT * FROM students")

#     rows = cursor.fetchall()

#     students = []

#     for row in rows:
#         students.append({
#             "id": row[0],
#             "name": row[1],
#             "age": row[2]
#         })

#     return students




# @app.put("/students/{student_id}")
# def update_student(student_id: int, student: Student):

#     cursor.execute(
#         "SELECT * FROM students WHERE id=?",
#         (student_id,)
#     )

#     old = cursor.fetchone()

#     if not old:
#         raise HTTPException(
#             status_code=404,
#             detail="Student not found"
#         )


#     cursor.execute(
#         "UPDATE students SET name=?, age=? WHERE id=?",
#         (student.name, student.age, student_id)
#     )

#     conn.commit()

#     return {"message": "Student Updated"}




# @app.delete("/students/{student_id}")
# def delete_student(student_id: int):

#     cursor.execute(
#         "SELECT * FROM students WHERE id=?",
#         (student_id,)
#     )

#     old = cursor.fetchone()


#     if not old:
#         raise HTTPException(
#             status_code=404,
#             detail="Student not found"
#         )


#     cursor.execute(
#         "DELETE FROM students WHERE id=?",
#         (student_id,)
#     )

#     conn.commit()

#     return {"message": "Student Deleted"}

#   #Courses#
# @app.post("/courses")
# def create_course(course: Course):

#     cursor.execute(
#         "INSERT INTO courses(title, price) VALUES(?, ?)",
#         (course.title, course.price)
#     )

#     conn.commit()

#     return {"message": "Course Created"}




# @app.get("/courses")
# def get_courses():

#     cursor.execute("SELECT * FROM courses")

#     rows = cursor.fetchall()

#     courses = []

#     for row in rows:
#         courses.append({
#             "id": row[0],
#             "title": row[1],
#             "price": row[2]
#         })

#     return courses




# @app.put("/courses/{course_id}")
# def update_course(course_id: int, course: Course):

#     cursor.execute(
#         "SELECT * FROM courses WHERE id=?",
#         (course_id,)
#     )

#     old = cursor.fetchone()


#     if not old:
#         raise HTTPException(
#             status_code=404,
#             detail="Course not found"
#         )


#     cursor.execute(
#         "UPDATE courses SET title=?, price=? WHERE id=?",
#         (course.title, course.price, course_id)
#     )

#     conn.commit()

#     return {"message": "Course Updated"}




# @app.delete("/courses/{course_id}")
# def delete_course(course_id: int):

#     cursor.execute(
#         "SELECT * FROM courses WHERE id=?",
#         (course_id,)
#     )

#     old = cursor.fetchone()


#     if not old:
#         raise HTTPException(
#             status_code=404,
#             detail="Course not found"
#         )


#     cursor.execute(
#         "DELETE FROM courses WHERE id=?",
#         (course_id,)
#     )

#     conn.commit()

#     return {"message": "Course Deleted"}  


#   #Enrollments#
# @app.post("/enrollments")
# def create_enrollment(enrollment: Enrollment):

#     cursor.execute(
#         "INSERT INTO enrollments(student_id, course_id) VALUES(?, ?)",
#         (enrollment.student_id, enrollment.course_id)
#     )

#     conn.commit()

#     return {"message": "Student enrolled successfully"}




# @app.get("/enrollments")
# def get_enrollments():

#     cursor.execute("SELECT * FROM enrollments")

#     rows = cursor.fetchall()

#     enrollments = []

#     for row in rows:
#         enrollments.append({
#             "id": row[0],
#             "student_id": row[1],
#             "course_id": row[2]
#         })

#     return enrollments




# @app.delete("/enrollments/{enrollment_id}")
# def delete_enrollment(enrollment_id: int):

#     cursor.execute(
#         "SELECT * FROM enrollments WHERE id=?",
#         (enrollment_id,)
#     )

#     old = cursor.fetchone()


#     if not old:
#         raise HTTPException(
#             status_code=404,
#             detail="Enrollment not found"
#         )


#     cursor.execute(
#         "DELETE FROM enrollments WHERE id=?",
#         (enrollment_id,)
#     )

#     conn.commit()

#     return {"message": "Enrollment deleted"}  



# @app.get("/students/{student_id}/courses")
# def get_student_courses(student_id: int):

#     cursor.execute("""
#         SELECT students.name, courses.title
#         FROM students
#         JOIN enrollments
#         ON students.id = enrollments.student_id
#         JOIN courses
#         ON courses.id = enrollments.course_id
#         WHERE students.id = ?
#     """, (student_id,))

#     rows = cursor.fetchall()

#     if not rows:
#         raise HTTPException(
#             status_code=404,
#             detail="No courses found"
#         )

#     return {
#         "student": rows[0][0],
#         "courses": [row[1] for row in rows]
#     }



# @app.get("/courses/{course_id}/students")
# def get_course_students(course_id: int):

#     cursor.execute("""
#         SELECT courses.title, students.name
#         FROM courses
#         JOIN enrollments
#         ON courses.id = enrollments.course_id
#         JOIN students
#         ON students.id = enrollments.student_id
#         WHERE courses.id = ?
#     """, (course_id,))

#     rows = cursor.fetchall()

#     if not rows:
#         raise HTTPException(
#             status_code=404,
#             detail="No students found"
#         )

#     return {
#         "course": rows[0][0],
#         "students": [row[1] for row in rows]
#     }

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from pydantic import BaseModel

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session, relationship


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return FileResponse("frontend.html")



# Database ORM

DATABASE_URL = "sqlite:///./school.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()




# Models


class Student(Base):

    __tablename__ = "students"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String
    )

    age = Column(
        Integer
    )


    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )




class Course(Base):

    __tablename__ = "courses"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    title = Column(
        String
    )


    price = Column(
        Integer
    )


    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )





class Enrollment(Base):

    __tablename__ = "enrollments"


    id = Column(
        Integer,
        primary_key=True
    )


    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )


    course_id = Column(
        Integer,
        ForeignKey("courses.id")
    )


    student = relationship(
        "Student",
        back_populates="enrollments"
    )


    course = relationship(
        "Course",
        back_populates="enrollments"
    )




Base.metadata.create_all(bind=engine)




# Schemas


class StudentSchema(BaseModel):

    name: str
    age: int



class CourseSchema(BaseModel):

    title: str
    price: int



class EnrollmentSchema(BaseModel):

    student_id: int
    course_id: int




# Students CRUD


@app.post("/students")
def create_student(
    student: StudentSchema,
    db: Session = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        age=student.age
    )


    db.add(new_student)
    db.commit()
    db.refresh(new_student)


    return {
        "message": "Student Created"
    }





@app.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    students = db.query(Student).all()


    return [
        {
            "id": s.id,
            "name": s.name,
            "age": s.age
        }

        for s in students
    ]





@app.put("/students/{student_id}")
def update_student(
    student_id:int,
    student:StudentSchema,
    db:Session=Depends(get_db)
):

    old = db.query(Student).filter(
        Student.id == student_id
    ).first()


    if not old:
        raise HTTPException(
            404,
            "Student not found"
        )


    old.name = student.name
    old.age = student.age


    db.commit()


    return {
        "message":"Student Updated"
    }





@app.delete("/students/{student_id}")
def delete_student(
    student_id:int,
    db:Session=Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()


    if not student:
        raise HTTPException(
            404,
            "Student not found"
        )


    db.delete(student)
    db.commit()


    return {
        "message":"Student Deleted"
    }
    # Courses CRUD


@app.post("/courses")
def create_course(
    course: CourseSchema,
    db: Session = Depends(get_db)
):

    new_course = Course(
        title=course.title,
        price=course.price
    )


    db.add(new_course)
    db.commit()
    db.refresh(new_course)


    return {
        "message": "Course Created"
    }





@app.get("/courses")
def get_courses(
    db: Session = Depends(get_db)
):

    courses = db.query(Course).all()


    return [
        {
            "id": c.id,
            "title": c.title,
            "price": c.price
        }

        for c in courses
    ]





@app.put("/courses/{course_id}")
def update_course(
    course_id:int,
    course:CourseSchema,
    db:Session=Depends(get_db)
):

    old = db.query(Course).filter(
        Course.id == course_id
    ).first()


    if not old:
        raise HTTPException(
            404,
            "Course not found"
        )


    old.title = course.title
    old.price = course.price


    db.commit()


    return {
        "message":"Course Updated"
    }





@app.delete("/courses/{course_id}")
def delete_course(
    course_id:int,
    db:Session=Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()


    if not course:
        raise HTTPException(
            404,
            "Course not found"
        )


    db.delete(course)
    db.commit()


    return {
        "message":"Course Deleted"
    }





# Enrollments CRUD


@app.post("/enrollments")
def create_enrollment(
    enrollment: EnrollmentSchema,
    db: Session = Depends(get_db)
):

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )


    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)


    return {
        "message":"Student enrolled successfully"
    }





@app.get("/enrollments")
def get_enrollments(
    db: Session = Depends(get_db)
):

    enrollments = db.query(Enrollment).all()


    return [
        {
            "id": e.id,
            "student": e.student.name,
            "course": e.course.title
        }

        for e in enrollments
    ]





@app.delete("/enrollments/{enrollment_id}")
def delete_enrollment(
    enrollment_id:int,
    db:Session=Depends(get_db)
):

    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()


    if not enrollment:
        raise HTTPException(
            404,
            "Enrollment not found"
        )


    db.delete(enrollment)
    db.commit()


    return {
        "message":"Enrollment deleted"
    }





# Student courses


@app.get("/students/{student_id}/courses")
def get_student_courses(
    student_id:int,
    db:Session=Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()


    if not student:
        raise HTTPException(
            404,
            "Student not found"
        )


    courses = []


    for enrollment in student.enrollments:

        courses.append(
            enrollment.course.title
        )


    if not courses:
        raise HTTPException(
            404,
            "No courses found"
        )


    return {
        "student": student.name,
        "courses": courses
    }





# Course students


@app.get("/courses/{course_id}/students")
def get_course_students(
    course_id:int,
    db:Session=Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()


    if not course:
        raise HTTPException(
            404,
            "Course not found"
        )


    students = []


    for enrollment in course.enrollments:

        students.append(
            enrollment.student.name
        )


    if not students:
        raise HTTPException(
            404,
            "No students found"
        )


    return {
        "course": course.title,
        "students": students
    }