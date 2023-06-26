import json


class PhoneBook:
    __slots__ = ('contacts',)

    def __init__(self, contacts=None):
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts

    def add_contact(self, contact=None):

        existing_contact = self.search_contact(contact.phone_number)

        if existing_contact:
            # Contact already exists, give user options
            print("Contact already exists. Choose an option:")
            print("1. Remove old contact and create new one")
            print("2. Edit contact")
            print("3. Cancel creation of new contact")
            option = input("Enter option number: ")

            if option == "1":
                self.delete_contact(existing_contact)
                self.contacts.append(contact)
                print("New contact was added successfully.")

            elif option == "2":
                self.edit_contact(existing_contact, contact)
                print("Contact was edited successfully.")
            else:
                print("Creation of the new contact was cancelled.")
        else:
            self.contacts.append(contact)
            print("Contact was added successfully.")

    def search_contact(self, contact_identifier):
        found_contacts = []

        # Удаление символа "+" из введенного номера, если присутствует
        if contact_identifier.startswith('+'):
            contact_identifier = contact_identifier[1:]
        # Проверка формата введенного номера
        if len(contact_identifier) == 9:
            # Добавление префикса "380" к введенному номеру
            contact_identifier = '380' + contact_identifier
        elif len(contact_identifier) == 10:
            # Добавление префикса "38" к введенному номеру
            contact_identifier = '38' + contact_identifier
        elif not contact_identifier.startswith('380'):
            contact_identifier = '380' + contact_identifier

        for contact in self.contacts:
            if contact.phone_number == contact_identifier or \
                    contact.phone_number.startswith(contact_identifier) or \
                    contact.name == contact_identifier or \
                    contact.surname == contact_identifier or \
                    contact.locality == contact_identifier or \
                    (contact.email and contact_identifier in contact.email) or \
                    (contact.social_media and contact_identifier in contact.social_media):
                found_contacts.append(contact)

        return found_contacts

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            print("Contact has been successfully deleted.")
        else:
            print("Contact not found.")

    def edit_contact(self, existing_contact, new_contact):
        self.contacts.remove(existing_contact)
        self.contacts.append(new_contact)

    def get_contact_info(self):

        print("To get contact's information please enter contact parameter "
              "to search: phone number, name, surname, locality, email or social_media")
        search_data = input("Enter the parameter to search: ")

        rez = self.search_contact(search_data)

        if rez is None:
            print('Nothing found')
        else:
            for cont in rez:
                print(cont)

    def export_records_to_json(self, filename):
        if not self.contacts:
            print("Нет записей для экспорта.")
            return False

        json_data = []
        for contact in self.contacts:
            contact_data = {
                "phone_number": contact.phone_number,
                "name": contact.name,
                "surname": contact.surname,
                "locality": contact.locality,
                "email": contact.email,
                "social_media": contact.social_media
            }
            json_data.append(contact_data)

        try:
            with open(filename, "w") as file:
                json.dump(json_data, file, indent=4)
            print(f"Records successfully exported to a file {filename}.")
            return True
        except IOError:
            print("Error when saving the file.")
            return False

