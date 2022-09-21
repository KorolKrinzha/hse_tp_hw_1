from ContactsController import *
import sys
print('Добрый день! Это система управления контактами. Пожалуйста, введите имя рабочего файла')
filename = str(input('Файл с контактами: '))
try:
    contactlist = readContactsFile(filename)
except:
    print('Файл не найден')
    sys.exit()
    
print('Отлично! Ваш список контактов загружен  \n Контакты: ')
displayContacts(contactlist)
action_number = 0
while action_number!=12:
    print(""" Выберите действие с контактами: 
                              1 - Все контакты 
                              2 - Поиск по номеру телефона 
                              3 - Поиск по почте 
                              4 - Поиск по ФИО/ФИ 
                              5 - Поиск по имени 
                              6 - Поиск по фамилии 
                              7 - Поиск по отчеству 
                              8 - Все контакты без почты 
                              9 - Все контакты без телефона 
                              10 - Все контакты без телефона и/или почты
                              11 - Редактирование контакта
                              12 - Закрыть программу""")
    
    try:
        action_number = int(input('Номер действия: '))
    except:
        print('Ошибка при введении данных. Повторите ввод')
        continue
    
    if action_number==1:
        displayContacts(contactlist)
    
    elif action_number==2:
        phone_to_find = str(input('Ввдеите номер телефона для поиска: ')).strip()
        print(findByPhone(contactlist, phone_to_find))
        
    elif action_number==3:
        email_to_find = str(input('Введите почту для поиска: ')).strip()
        print(findByEmail(contactlist, email_to_find))
    
    elif action_number==4:
        fullname_to_find = str(input('Введите ФИО/ФИ для поиска: ')).strip()
        print(findByFullname(contactlist, fullname_to_find))
        pass
    
    elif action_number==5:
        firstname_to_find = str(input('Введите имя для поиска: ')).strip()
        print(findByFirstName(contactlist, firstname_to_find))
    
    elif action_number==6:
        lastname_to_find = str(input('Введите фамилию для поиска: ')).strip()
        print(findByLastName(contactlist, lastname_to_find))
    
    elif action_number==7:
        
        middlename_to_find = str(input('Введите отчество для поиска: ')).strip()
        print(findByMiddleName(contactlist, middlename_to_find))
    
    elif action_number==8:
        displayContacts(BlankEmail(contactlist))
    
    elif action_number==9:
        displayContacts(BlankPhone(contactlist))
    
    elif action_number==10:
        displayContacts(BlankAll(contactlist))
    
    elif action_number==11:
        displayContactsWithId(contactlist)
        contactid = int(input('Введите номер контакта: '))
        name = str(input('Введите новый ФИО: '))
        email = str(input('Введите новый email: '))
        phone = str(input('Введите новый телефон: '))
        newinfo = {'name': name, 'email': email, 'phone': phone}
        
        new_contact_dict = editContact(contactlist, contactid, newinfo)
        writeChanges(new_contact_dict.values(), filename)
        contactlist = readContactsFile(filename)
        
        
    elif action_number==12:
        pass
        
        
    else: 
        print('Данное действие не было найдено. Повторите ввод')
        
