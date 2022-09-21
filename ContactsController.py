from Contacts import Contacts

def readContactsFile(filename):
    with open (filename, encoding='utf-8') as f:
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

contactList = readContactsFile('contacts.txt')
def displayContacts(contactlist:list):
    for contact in contactlist:
        print(contact)
        
def displayContactsWithId(contactlist:Contacts):
    contacts_dict = {i: contact for i,contact in enumerate(contactlist)}
    for key,value in contacts_dict.items():
        print(key, ':', value)
    

def findByPhone(contactlist:Contacts, phone_to_find:str) -> Contacts:
    for contact in contactlist:
        contact_phone = contact.getPhone()
        if phone_to_find==contact_phone: return contact
    
    print('Телефон не найден')

def findByEmail(contactlist:Contacts, email_to_find:str) -> Contacts:
    for contact in contactlist:
        contact_email = contact.getEmail()
        if email_to_find==contact_email: return contact
    
    print('Почта не найдена')
        
def findByFullname(contactlist:Contacts, fullname_to_find:str) -> Contacts:
    if len(fullname_to_find.split(' '))==3:
        for contact in contactlist:
            contact_fullname = contact.getFullName()
            if fullname_to_find==contact_fullname: return contact
    if len(fullname_to_find.split(' '))==2:
        for contact in contactlist:
            contact_fullname = f"{contact.getLastName()} {contact.getFirstName()}"
            if fullname_to_find==contact_fullname: return contact
    
    print('Контакт не найден')

def findByMiddleName(contactlist:Contacts, middlename_to_find:str) -> Contacts:
    for contact in contactlist:
        contact_middlename = contact.getMiddleName()
        if middlename_to_find==contact_middlename: return contact
    
    print('Контакт не найден')
    
def findByFirstName(contactlist:Contacts, firstname_to_find:str) -> Contacts:
    for contact in contactlist:
        contact_fistname = contact.getFirstName()
        if firstname_to_find==contact_fistname: return contact
    
    print('Контакт не найден')

def findByLastName(contactlist:Contacts, lastname_to_find:str) -> Contacts:
    for contact in contactlist:
        contact_lastname = contact.getLastName()
        if lastname_to_find==contact_lastname: return contact
    
    print('Контакт')

def BlankPhone(contactlist:Contacts) -> list:
    blank_phone_contacts = []
    for contact in contactlist:
        if len(contact.getPhone())==0: blank_phone_contacts.append(contact)
    return blank_phone_contacts

def BlankEmail(contactlist:Contacts) -> list:
    blank_email_contacts  = []
    for contact in contactlist:
        if len(contact.getEmail())==0: blank_email_contacts.append(contact)
    return blank_email_contacts

def BlankAll(contactlist:Contacts) -> list:
    blank_phone_contacts = BlankEmail(contactlist)
    blank_email_contacts = BlankPhone(contactlist)
    blank_all = list(set(blank_email_contacts+blank_phone_contacts))
    return blank_all



def editContact(contactlist:Contacts, contactid: int, newinfo:dict) -> dict:
    editperson = Contacts(newinfo['name'], newinfo['email'], newinfo['phone'])
    
    contacts_dict = {i: contact for i,contact in enumerate(contactlist)}
    contacts_dict[contactid] = editperson
    
    
    
    
    return contacts_dict 

def writeChanges(contactlist:Contacts, filename:str) -> None:
    with open(filename,'w', encoding='utf-8') as f:
        for contact in contactlist:
            f.write(f"{contact}\n")
    return

        

    
