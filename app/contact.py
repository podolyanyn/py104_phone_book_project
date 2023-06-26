from typing import List, Union
import re


class Contact:
    all_contacts = []
    __slots__ = ('phone_number', 'name', 'surname', 'locality', 'email', 'social_media', 'black_list_status')

    def __init__(self, phone_number: str, name: str, surname: str = None, city: str = None,
                 email: List[str] = None, links: List[str] = None, black_list_status: bool = False):
        self.phone_number = self._validate_phone_number(phone_number)
        self.name = self._validate_name(name)
        self.surname = self._validate_surname(surname)
        self.locality = city
        self.email = self._validate_email(email)
        self.social_media = links
        self.black_list_status = black_list_status
        Contact.all_contacts.append(self)

    def _validate_phone_number(self, phone_number: str) -> str:
        phone_number = re.sub(r'\D', '', phone_number)  # Remove non-digit characters from the phone number
        if phone_number.startswith('0'):  # Remove leading zero
            phone_number = phone_number[1:]

        if len(phone_number) == 10:  # Add country code if missing
            phone_number = '380' + phone_number
        elif len(phone_number) > 12 or not phone_number.isdigit():
            raise ValueError("Invalid phone number format. Use this format: +380123457283")

        return phone_number

    def _validate_name(self, name):
        if " " in name:
            raise ValueError("Name cannot contain spaces.")
        return name

    def _validate_surname(self, surname):
        if surname and " " in surname:
            raise ValueError("Surname cannot contain spaces.")
        return surname

    def _validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if email is not None:
            if isinstance(email, list):
                for e in email:
                    if not re.match(pattern, e):
                        raise ValueError("Invalid email format. Use this format: qwerty@example.com")
                return email
        return None

    def edit_contact(self, phone_number: List[str], name: str, surname: str = None, city: str = None,
                     email: Union[str, List[str]] = None, links: List[str] = None, black_list_status: bool = False):
        pass

    def __str__(self):
        return f'phone_number: {self.phone_number}, name: {self.name}, surname: {self.surname}, ' \
               f'locality: {self.locality}, email: {self.email}, social_media: {self.social_media},' \
               f'black_list_status: {self.black_list_status}'

    def get_info(self):
        print(self.__str__())

    def add_to_black_list(self):
        self.black_list_status = True
        return self.black_list_status

    def remove_from_black_list(self):
        self.black_list_status = False
        return self.black_list_status

    @staticmethod
    def _check_unique_number(number):
        for contact in Contact.all_contacts:
            if number in contact.phone_number:
                return contact
        return True
