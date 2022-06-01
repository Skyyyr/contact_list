class ContactList():
    """This class is essentially our phonebook, each instance is a group of contacts within the phone book.
    """

    # Initialize the class instance
    def __init__(self, group_name, array_of_contacts):
        self.contact_list = array_of_contacts
        self.group_name = group_name

    # Dunder string setup
    def __str__(self):
        return f"{self.contact_list}"

    # Add a contact to the instanced array of contacts
    def add_contact(self, contact_to_add):
        self.contact_list.append(contact_to_add)
        # Don't forget to sort, could probably use decorators instead?
        self.sort_contacts()

    # Remove contact from the instanced array of contacts
    def remove_contact(self, contact_to_remove):
        # For index in range of the length of the array
        for i in range(len(self.contact_list)):
            # If the name value is equal to the contact to remove
            if self.contact_list[i]['name'] == contact_to_remove:
                # Remove it, and stop searching for it
                del self.contact_list[i]
                break

    # Find shared contacts between the two arrays
    def find_shared_contacts(self, contacts_to_search):
        # Variable setup for ease of reading
        search_list = contacts_to_search.contact_list
        current_list = self.contact_list
        shared_contacts = []
        # For each contact in the current list
        for contact_a in current_list:
            # For each contact in the search list
            for contact_b in search_list:
                # Variable setup for ease of reading
                b_name = contact_b['name']
                a_name = contact_a['name']
                # If the name values are the same, then add to an array of shared values
                if a_name == b_name:
                    shared_contacts.append(contact_a)
        # Don't forget to sort them!
        self.sort_contacts()
        return shared_contacts

    # Sort contacts
    def sort_contacts(self):
        self.contact_list = sorted(self.contact_list, key=lambda x: x['name'])

# OUTPUTS
work_contacts = ContactList('work', [{'name':'Clare','number':'867-5309'},{'name':'Dobby', 'number':'555-5555'}, {'name':'Bob', 'number':'555-5555'}])
work_buddies = ContactList('friends', [{'name':'Dobby', 'number':'555-5555'}, {'name':'Alice','number':'867-5309'}])
work_contacts.add_contact({'name':'Alice', 'number':'555-5555'})
print(work_contacts)
work_contacts.remove_contact('tester1')
print("WORK ",work_contacts.find_shared_contacts(work_buddies))
