# py104_phone_book_project

# Team 1

# Team 2

For class Contact with atributes:
  - phone_number  - required
  - name          - required
  - surname				- not required
  - locality      - not required
  - email         - not required
  - social_media  - not required

1.1.2.3 Add new contact. If contact exist give user options: 
  - remove old one and create new one
  - edit contact
  - or cancel creation of new contact

1.1.2.4 Edit contact

1.1.2.5 Get contact info
  - search should work for all fields and be case-insensitive

4.1 Create interface for adding new contact in main menu

# Team 3 

### **1.2 Phone number (Performer - Stanislav Zelinskyi (Volodymyr Levchenko))**

**Description of the _validate_phone_number method:**

The _validate_phone_number(phone_number) method in the Contact class is for validating and formatting a contact's phone number.

**Parameters:**

phone_number (string): The phone number to be validated and formatted.

**Returned value:**

phone_number (string): The formatted phone number.

**Description:**

The _validate_phone_number method performs the following steps to validate and format the phone number:

Removes all non-numeric characters from the phone number using the re.sub() method and the regular expression r'\D'. This removes all characters except digits.
If a phone number starts with a zero (0), the method removes the leading zero by assigning phone_number = phone_number[1:].
Checks the length of phone_number. If length is 10, the method appends "380" prefix to phone number to indicate a country code.
If phone_number is longer than 12, or if phone_number does not contain digits only, the method throws a ValueError exception with "Invalid phone number format. Use this format: +380123457283".
Returns the formatted phone number phone_number.

### 1.1.2.6 Delete contact (Performer - Stanislav Zelinskyi)

**Description of the delete_contact method:**

The delete_contact(contact) method in the PhoneBook class is designed to delete the specified contact from the phonebook.

**Parameters:**

contact (Contact object): The contact to be deleted from the phonebook.

**Description:**

The delete_contact method checks if the specified contact is present in the self.contacts list of the phonebook. If the contact is present in the list, it is removed using the remove() method. A message "Contact has been successfully deleted" is then displayed. If the contact is not found in the phonebook, the message "Contact not found" is output.

### 1.1.2.7 Export records (in json format) (Performer - Stanislav Zelinskyi)

**Description of how the export_records_to_json method works:**

The export_records_to_json(filename) method in the PhoneBook class is designed to export contact records in JSON format and save them to the specified file.

**Parameters:**

filename (string): The name of the file into which the contact records will be exported.

**Returned value:**

True (boolean value): If the export of contact records is successful and the file is saved successfully.
False (logical value): If there are no entries to export in the phonebook or an error has occurred while saving the file.

**Description:**

The export_records_to_json method checks if there are any contact records in the phonebook. If there are no contact records, the method outputs "No records to export" message and returns False.

Then method creates json_data list where each contact is converted to a dictionary containing contact attributes (phone number, first name, last name, location, email address and social media links).

The method then tries to open the specified filename file in write mode. If the file is successfully opened, the method uses json.dump function to write data from json_data list to an indented JSON file.

If writing to file succeeds, method outputs "Records exported successfully to file {filename}" and returns True.

If file saving error occurs, method outputs message "File saving error" and returns False value.

### 4.2 Search for contact (Performer - Stanislav Zelinskyi)
    
**Description of the search_contact method:**

The search_contact(contact_identifier) method in the PhoneBook class allows you to search for contacts in the phonebook by a given identifier.

**Parameters:**

contact_identifier (string): Identifier to search for contacts. Can be phone number, first name, last name, location, email address or social media link.

**Returned value:**

found_contacts (list): A list of contacts that match the given search ID. Each element in the list is an object of the Contact class.

**Description:**
The search_contact method searches for contacts in the phonebook based on the given search ID. It checks each contact in the book and compares it to the ID, using multiple checks for different contact attributes.

* The method first removes the "+" character from the beginning of the ID, if present, and then checks the format of the phone number ID. If identifier consists of 9 digits, method adds "380" prefix to number, if it consists of 10 digits - prefix "38". If the ID does not begin with "380", the prefix "380" is also added.

* The method then iterates through all contacts in the phonebook and compares each contact to the search ID. If the contact matches the ID, it is added to the found_contacts list.

* Finally, the method returns the found_contacts list containing all found contacts matching the search ID.
