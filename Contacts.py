class Contacts:

    # Created a constructor for class Contacts with all private attributes
    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name},{self.email},{self.phone}"


# Created getters for every attribute

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getFullName(self):
        return self.name

    def getLastName(self):
        lastname = self.name.split(' ')[0]
        return lastname

    def getFirstName(self):
        try:
            firstname = self.name.split(' ')[1]
        except:
            return ''
        return firstname

    def getMiddleName(self):
        try:
            middlename = self.name.split(' ')[2]
            return middlename
        except:
            return ''
