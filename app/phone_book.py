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
                self.delete_contact(existing_contact.phone_number)
                self.contacts.append(contact)
                print("New contact was added successfully.")

            elif option == "2":
                self.edit_contact(existing_contact.phone_number, contact)
                print("Contact was edited successfully.")
            else:
                print("Creation of the new contact was cancelled.")
        else:
            self.contacts.append(contact)
            print("Contact was added successfully.")

    def search_contact(self, contact_identifier):
        found_contacts = []

        for contact in self.contacts:
            if contact.phone_number == contact_identifier:
                found_contacts.append(contact)
            elif contact.name.lower() == contact_identifier.lower():
                found_contacts.append(contact)
            elif contact.surname and contact.surname.lower() == contact_identifier.lower():
                found_contacts.append(contact)
            elif contact.locality and contact.locality.lower() == contact_identifier.lower():
                found_contacts.append(contact)
            elif contact.email and contact.email.lower() == contact_identifier.lower():
                found_contacts.append(contact)
            elif contact.social_media and contact.social_media.lower() == contact_identifier.lower():
                found_contacts.append(contact)

        return found_contacts

    def delete_contact(self, contact_identifier):
        contact = self.search_contact(contact_identifier)

        if contact:
            self.contacts.remove(contact)
            print("Contact has been successfully deleted.")
        else:
            print("Contact not found.")

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
            return

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
            print(f"Записи успешно экспортированы в файл {filename}.")
        except IOError:
            print("Ошибка при сохранении файла.")
