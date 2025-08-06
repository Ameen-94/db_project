import enum
import csv
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

    def __init__(self):
        self.students: list = []

    def create_student(
        self, name: str, age: int, gpa: float, major: Major, gender: Gender
    ) -> Student:
        """create a new student"""
        truncated_uuid = "".join(filter(str.isdigit, str(uuid.uuid4())))
        truncated_uuid = truncated_uuid[::-1]
        truncated_uuid = truncated_uuid[:6].upper()
        student = Student(
            student_id=truncated_uuid,
            name=name,
            age=age,
            gpa=gpa,
            major=major,
            gender=gender,
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

    def save_db(self, file_name: str):
        """save the database to a file"""
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for student in self.students:
                writer.writerow(
                    [
                        student.student_id,
                        student.name,
                        student.age,
                        student.gpa,
                        student.major,
                    ]
                )

        print(f"Students database saved to {file_name}")

    def load_db(self, file_name: str):
        """load the database from a file"""
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(
                    student_id=row[0],
                    name=row[1],
                    age=int(row[2]),
                    gpa=float(row[3]),
                    major=Major(row[4]),
                )
                self.students.append(student)
        print(f"Students database loaded from {file_name}")


db_1 = StudentDB()
db_2 = StudentDB()
student_1 = db_1.create_student(
    name="Ameen Jaradat",
    age=22,
    gpa=3.99,
    major=Major.COMPUTER_ENGINEERING,
    gender=Gender.MALE,
)
print(db_1.read_student(student_1.student_id))
student_2 = db_1.create_student(
    name="Mohammad Jaradat",
    age=20,
    gpa=3.38,
    major=Major.DATA_SCIENCE,
    gender=Gender.MALE,
)
student_3 = db_1.create_student(
    name="Ahmad Mousa",
    age=21,
    gpa=2.98,
    major=Major.COMPUTER_SCIENCE,
    gender=Gender.MALE,
)
db_1.save_db("students.csv")
db_2.load_db("students.csv")
print(db_2.students[0])
print(db_2.read_student(student_1.student_id))
print(db_2.read_student(student_1.student_id))
db_2.delete_student(student_2.student_id)
db_2.save_db("students.csv")
