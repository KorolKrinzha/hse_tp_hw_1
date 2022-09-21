from ContactsController import *
print('Добрйы день! Это система управления контактами. Пожалуйста, введите имя рабочего файла')
filename = str(input('Файл с контактами: '))
contact_list = readContactsFile(filename)
print('Отлично! Ваш список контактов загружен  \n Контакты: ')
displayContacts(contact_list)
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
                              11 - Редактирование телефона
                              12 - закрыть программу""")
    
    action_number = int(input('Номер действия: '))
    if action_number==1:
        displayContacts(contact_list)
    elif action_number==2:
        
        phone_to_find = str(input('Ввдеите номер телефона'))
        contact = findByPhone(contactlist, phone_to_find)
        print(contact)
    elif action_number==3:
        email_to_find = str(input('Введите почту'))
        contact = findByEmail(contactlist, email_to_find)
        print(contact)
    elif action_number==4:
        pass
    elif action_number==5:
        pass
    elif action_number==6:
        pass
    elif action_number==8:
        displayContacts(BlankEmail(contact_list))
    elif action_number==9:
        displayContacts(BlankPhone(contact_list))
    elif action_number==10:
        displayContacts(BlankAll(contact_list))
    elif action_number==11:
        pass
        
    # actions = {
    #     1: displayContacts(contactlist)
            
    # }