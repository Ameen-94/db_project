import enum
import collections
import dataclasses
import typing
import uuid

class Gender(str, enum.Enum):
    """enum to store values of genders"""

    MALE = "MALE"
    FEMALE = "FEMALE"

class Major(str, enum.Enum):
    """enum to store values of majors"""

    COMPUTER_SCIENCE = "COMPUTER_SCIENCE"
    DATA_SCIENCE = "DATA_SCIENCE"
    COMPUTER_ENGINEERING = "COMPUTER_ENGINEERING"
    SOFTWARE_ENGINEERING = "SOFTWARE_ENGINEERING"
    NETWORK_ENGINEERING = "NETWORK_ENGINEERING"
    INFORMATION_SYSTEMS = "INFORMATION_SYSTEMS"

@dataclasses.dataclass
class Student:
    """A dataclass to store a single student"""
    student_id: str = None
    name: str = "John Doe"
    age: int = 18
    gpa: float = None
    major: Major = Major.COMPUTER_SCIENCE
    gender: Gender = Gender.MALE

@dataclasses.dataclass
class Students:
    """A list of students"""
    Students: typing.List[Student] = dataclasses.field(default_factory=list)

class StudentDB:
    """a database containing the students"""
    students: Students = []

    def create_student(self, name: str, age: int, gpa: float, major: Major, gender: Gender) -> Student:
        """create a new student"""
        truncated_uuid = ''.join(filter(str.isdigit, str(uuid.uuid4())))
        truncated_uuid = truncated_uuid[::-1]
        truncated_uuid = truncated_uuid[:6].upper()
        student = Student(
            student_id=truncated_uuid,
            name=name,
            age=age,
            gpa=gpa,
            major=major,
            gender= gender
        )
        self.students.append(student)
        print(f"Student {student.name} created with ID {student.student_id}")
        return student
    
    def read_student(self, student_id: str) -> Student:

        for student in self.students:

            if student.student_id == student_id:

                return student

        return f"Student ID {student_id} does not exist"
    
    def delete_student(self, student_id: str):
        for idx, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[idx]
                print(f"Student with Student ID {student_id} deleted successfully.")
                return
        raise ValueError(f"Student ID {student_id} does not exist.")

    
db = StudentDB()
student_1 = db.create_student(name= "Ameen Jaradat", age= 22, gpa= 3.99, major= Major.COMPUTER_ENGINEERING, gender=Gender.MALE)
print(db.read_student(student_1.student_id))
db.delete_student(student_1.student_id)
