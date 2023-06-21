from contact import *


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
        for contact in self.contacts:
            if contact.phone_number == contact_identifier:
                return contact
            if contact.name.lower() == contact_identifier.lower():
                return contact
            if contact.surname.lower() == contact_identifier.lower():
                return contact
            if contact.locality.lower() == contact_identifier.lower():
                return contact
            if contact.email.lower() == contact_identifier.lower():
                return contact
            if contact.social_media.lower() == contact_identifier.lower():
                return contact

        return None

    def delete_contact(self, contact_identifier):
        contact = self.search_contact(contact_identifier)

        if contact:
            self.contacts.remove()
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
