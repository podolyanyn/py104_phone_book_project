# Import the classes
from contact import Contact
from phone_book import PhoneBook

# Create a PhoneBook instance
phone_book = PhoneBook()

# Create some contacts
contact1 = Contact("+380123456789", "John", "Doe", "New York", ["john.doe@example.com"], ["facebook.com/johndoe"])
contact2 = Contact("+380987654321", "Jane", "Smith", "London", ["jane.smith@example.com"], ["twitter.com/janesmith"])
# Test the functionality of the PhoneBook

# Create contacts
contact4 = Contact("+380951234567", "John", "Doe", "New York", email=["john.doe@example.com"], links=["linkedin.com/johndoe"])
contact5 = Contact("+380961234567", "Jane", "Smith", "London", email=["jane.smith@example.com"], links=["linkedin.com/janesmith"])
contact3 = Contact("+380971234567", "Bob", "Johnson", "Paris", email=["bob.johnson@example.com"], links=["linkedin.com/bobjohnson"])


# Add contacts to the phone book
phone_book.add_contact(contact1)
phone_book.add_contact(contact2)
phone_book.add_contact(contact3)
phone_book.add_contact(contact4)
phone_book.add_contact(contact5)

# Get contact information
phone_book.get_contact_info()

# Delete a contact
phone_book.delete_contact(contact1)

# Export records to JSON file
phone_book.export_records_to_json("contacts.json")


# Search for a contact
results = phone_book.search_contact("Jane")
print(results)  # Expected: [contact5]

# Delete a contact
phone_book.delete_contact("380987654321")


# Get contact information
phone_book.get_contact_info()

# Add a contact to the black list
contact1.add_to_black_list()

# Remove a contact from the black list
contact1.remove_from_black_list()
# Test phone number validation
try:
    contact6 = Contact("80987654321", "Jane", "Smith", "London", ["jane.smith@example.com"], ["twitter.com/janesmith"])
    print(contact6.phone_number)
except ValueError as e:
    print(str(e))

try:
    contact7 = Contact("987654321", "Jane", "Smith", "London", ["jane.smith@example.com"], ["twitter.com/janesmith"])
    print(contact7.phone_number)
except ValueError as e:
    print(str(e))

try:
    contact8 = Contact("0987654321", "Jane", "Smith", "London", ["jane.smith@example.com"], ["twitter.com/janesmith"])
    print(contact8.phone_number)
except ValueError as e:
    print(str(e))

try:
    contact9 = Contact("+380987654321", "Jane", "Smith", "London", ["jane.smith@example.com"], ["twitter.com/janesmith"])
    print(contact9.phone_number)
except ValueError as e:
    print(str(e))
