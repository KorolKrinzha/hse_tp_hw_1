from Contacts import Contacts

# Read DB with contacts
# Function returns contacts as a list of Contacts class objects


def readContactsFile(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]

        contactlist = []
        for line in lines:
            name = line.split(',')[0].strip()
            phone = line.split(',')[1].strip()
            email = line.split(',')[2].strip()

            contactlist.append(Contacts(name, phone, email))

        return contactlist

    return

# Print out contacts the way displayed in DB


def displayContacts(contactlist: list):
    for contact in contactlist:
        contact_name = contact.getFullName()
        contact_email = contact.getEmail() if len(
            contact.getEmail()) > 0 else 'Мэйл не указан'
        contact_phone = contact.getPhone() if len(
            contact.getPhone()) > 0 else 'Теле не указан'

        print(
            contact_name +
            '\t||\t' +
            contact_email +
            '\t||\t' +
            contact_phone)

# Functions that find contacts by specified fields


def displayContactsWithId(contactlist: list):
    contacts_dict = {i: contact for i, contact in enumerate(contactlist)}
    for key, value in contacts_dict.items():
        print(key, ':', value)


def findByPhone(contactlist: list, phone_to_find: str) -> Contacts:
    for contact in contactlist:
        contact_phone = contact.getPhone()
        if phone_to_find == contact_phone:
            return contact

    raise Exception('Телефон не найден')


def findByEmail(contactlist: list, email_to_find: str) -> Contacts:
    for contact in contactlist:
        contact_email = contact.getEmail()
        if email_to_find == contact_email:
            return contact

    raise Exception('Почта не найдена')


def findByFullname(contactlist: list, fullname_to_find: str) -> Contacts:
    if len(fullname_to_find.split(' ')) == 3:
        for contact in contactlist:
            contact_fullname = contact.getFullName()
            if fullname_to_find == contact_fullname:
                return contact
    if len(fullname_to_find.split(' ')) == 2:
        for contact in contactlist:
            contact_fullname = f"{contact.getLastName()} {contact.getFirstName()}"
            if fullname_to_find == contact_fullname:
                return contact

    raise Exception('Контакт не найден')


def findByMiddleName(contactlist: list, middlename_to_find: str) -> Contacts:
    for contact in contactlist:
        contact_middlename = contact.getMiddleName()
        if middlename_to_find == contact_middlename:
            return contact

    raise Exception('Отчество не найдено')


def findByFirstName(contactlist: list, firstname_to_find: str) -> Contacts:
    for contact in contactlist:
        contact_fistname = contact.getFirstName()
        if firstname_to_find == contact_fistname:
            return contact

    raise Exception('Контакт не найден')


def findByLastName(contactlist: Contacts, lastname_to_find: str) -> Contacts:
    for contact in contactlist:
        contact_lastname = contact.getLastName()
        if lastname_to_find == contact_lastname:
            return contact

    raise Exception('Контакт')

# Display contacts with one or several fields missing


def BlankPhone(contactlist: Contacts) -> list:
    blank_phone_contacts = []
    for contact in contactlist:
        if len(contact.getPhone()) == 0:
            blank_phone_contacts.append(contact)
    return blank_phone_contacts


def BlankEmail(contactlist: Contacts) -> list:
    blank_email_contacts = []
    for contact in contactlist:
        if len(contact.getEmail()) == 0:
            blank_email_contacts.append(contact)
    return blank_email_contacts


def BlankAll(contactlist: Contacts) -> list:
    blank_phone_contacts = BlankEmail(contactlist)
    blank_email_contacts = BlankPhone(contactlist)
    blank_all = list(set(blank_email_contacts + blank_phone_contacts))
    return blank_all


# Edit one contact by rewriting it completely
def editContact(contactlist: Contacts, contactid: int, newinfo: dict) -> dict:
    # Rewrote one person in contacts
    editperson = Contacts(newinfo['name'], newinfo['email'], newinfo['phone'])

    # Get the whole contacts DB with serial IDs
    # We will rewrite one value and return the dict so it can be new DB
    contacts_dict = {i: contact for i, contact in enumerate(contactlist)}

    # Change contact with specified id by adding new object instead of old one
    contacts_dict[contactid] = editperson

    # Return dictionary of contacts with one changed value
    return contacts_dict

# Write editted contact among others to DB


def writeChanges(contactlist: Contacts, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for contact in contactlist:
            f.write(f"{contact}\n")
    return
