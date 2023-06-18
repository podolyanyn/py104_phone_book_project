from typing import List


class Contact:

    __slots__ = ('phone_number', 'name', 'surname', 'locality', 'email', 'social_media')

    def __init__(self, phone_number: List[str], name: str, surname: str = None, city: str = None,
                 email: List[str] = None, links: List[str] = None, black_list_status: bool = False):
        self.phone_number = self._validate_phone_number(phone_number)
        self.name = self._validate_name(name)
        self.surname = self._validate_surname(surname)
        self.locality = city
        self.email = self._validate_email(email)
        self.social_media = links
        self.black_list_status = black_list_status

    def _validate_phone_number(self, phone_number):
        for number in phone_number:
            if not number.startswith("+380") or len(number) != 13:
                raise ValueError("Invalid phone number format. Use this format: +380123457283 ")
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
        if email and ("@" not in email or "." not in email):
            raise ValueError("Invalid email format. Use this format: qwerty@example.com")
        return email

    def edit_contact(self, phone_number: List[str], name: str, surname: str = None, city: str = None,
                     email: List[str] = None, links: List[str] = None, black_list_status: bool = False):
        pass

    def __str__(self):

        return f'phone_number: {self.phone_number}, name: {self.name}, surname: {self.surname}, ' \
               f'locality: {self.locality},' f'email: {self.email}, social_media: {self.social_media}'

    def get_info(self):
        print(self.__str__())
