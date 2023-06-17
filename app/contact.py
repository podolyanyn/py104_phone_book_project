class Contact:

    __slots__ = ('phone_number', 'name', 'surname', 'locality', 'email', 'social_media')

    def __init__(self, phone_number = None, name = None,\
                surname = None, locality = None, email = None,\
                social_media = None):
        self.phone_number = phone_number
        self.name = name
        self.surname = surname
        self.locality = locality
        self.email = email
        self.social_media = social_media

        if self.phone_number is None:
            raise AttributeError('Phone number must be provided!')
        if self.name is None:
            raise AttributeError('Name must be provided!')

    def edit_contact(self, phone_number = None, name = None,\
                    surname = None, locality = None, email = None,\
                    social_media = None):
        pass

    def __str__(self):

        return f'phone_number: {self.phone_number}, name: {self.name}, surname: {self.surname}, locality: {self.locality},' \
               f'email: {self.email}, social_media: {self.social_media}'

    def get_info(self):
        print(self.__str__())
