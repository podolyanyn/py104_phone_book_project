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

    def get_info(self):
        pass
