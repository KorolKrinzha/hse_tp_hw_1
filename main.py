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
             
            contactlist.append(Contacts(name, email, phone))
        
        return contactlist
        
    return

contactList = readContactsFile('contacts.txt')

def findByPhone(contactlist, phone_to_find):
    for contact in contactlist:
        contact_phone = contact.getPhone()
        if phone_to_find==contact_phone: return contact
    
    raise Exception('Телефон не найден')

def findByEmail(contactlist,email_to_find):
    for contact in contactlist:
        contact_email = contact.getEmail()
        if email_to_find==contact_email: return contact
    
    raise Exception('Почта не найдена')
        
def findByFullname(contactlist, fullname_to_find):
    for contact in contactlist:
        contact_fullname = contact.getFullName()
        if fullname_to_find==contact_fullname: return contact
    
    raise Exception('Контакт не найден')

def findByMiddleName(contactlist:Contacts, middlename_to_find: str) -> Contacts:
    for contact in contactlist:
        contact_middlename = contact.getMiddleName()
        if middlename_to_find==contact_middlename: return contact
    
    raise Exception('Контакт не найден')
    
# print(findByPhone(contactList, '+79966969669'))
# print(findByEmail(contactList, 'kolya@gmail.com'))
print(findByMiddleName(contactList, 'Сергеевич'))
        

    
