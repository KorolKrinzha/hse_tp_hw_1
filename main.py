from Contacts import Contacts

def readContactsFile(filename):
    with open (filename, encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        
        persons = []
        for line in lines:
            
            name = line.split(',')[0]
            email = line.split(',')[1]
            phone = line.split(',')[2]
            person = Contacts(name, email, phone)
            persons.append(person)
        
        return persons
        
    return

readContactsFile('contacts.txt')

