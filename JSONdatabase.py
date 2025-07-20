import enum
import json
import collections
import dataclasses
from typing import List
from uuid import uuid4


class Country(enum.Enum):
    """enum to store values of countries"""

    JORDAN = enum.auto()
    SAUDI_ARABIA = enum.auto()
    EGYPT = enum.auto()


class Gender(enum.Enum):
    """enum to store values of genders"""

    FEMALE = enum.auto()
    MALE = enum.auto()


@dataclasses.dataclass
class Contact:
    """a dataclass to store a single contact"""

    contact_id: str = None
    name: str = "John Doe"
    contact_number: str = None
    country: Country = Country.EGYPT
    gender: Gender = Gender.MALE


@dataclasses.dataclass
class Contacts:
    """a list of contacts"""

    contacts = List[Contact]


class UpdateParameter(enum.Enum):
    NAME = enum.auto()
    COUNTACT_NUMBER = enum.auto()
    GENDER = enum.auto()
    COUNTRY = enum.auto()


class ContactsDB:
    """a database containing my contacts"""

    contacts: Contacts = []

    def create_contact(
        self, name: str, contact_number: str, country: Country, gender: Gender
    ):
        truncated_uuid = str(uuid4())
        truncated_uuid = truncated_uuid[::-1]
        truncated_uuid = truncated_uuid[:4].upper()
        contact = Contact(
            contact_id=truncated_uuid,
            name=name,
            contact_number=contact_number,
            country=country,
            gender=gender,
        )
        self.contacts.append(
            Contact(
                contact_id=truncated_uuid,
                name=name,
                contact_number=contact_number,
                country=country,
                gender=gender,
            )
        )
        print(f"Contact ID {truncated_uuid} created successfully.")
        return contact

    def read_contacts(self) -> Contacts:
        return self.contacts

    # def update_contacts(self, contact_id: str, update_parameter: UpdateParameter)-> Contacts:
    #    match update_parameter:
    #        case UpdateParameter.NAME:


db = ContactsDB()
contact = db.create_contact(
    name="Ameen Jaradat",
    contact_number="+962795907266",
    country=Country.JORDAN,
    gender=Gender.MALE,
)
print(db.read_contacts())
print(contact)
