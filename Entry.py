import re


class Entry:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.phone = ""
        self.city = ""
        self.email = ""

    def to_string(self):
        fields = vars(self)
        return ', '.join([field + ':' + fields[field] for field in fields])

    def parse(self, text):
        text = re.split(', |:|\n', text)
        self.name = text[1]
        self.surname = text[3]
        self.phone = text[5]
        self.city = text[7]
        self.email = text[9]

    def trySetValue(self, field_name, field_value):
        if field_name == 'name' or field_name == 'surname' or field_name == 'city':
            if Entry.validateField(field_value):
                vars(self)[field_name] = str.title(field_value)
                return True
            return False
        elif field_name == 'phone':
            if Entry.validatePhone(field_value):
                self.phone = field_value
                return True
            return False
        elif field_name == 'email':
            if Entry.validateEmail(field_value):
                self.email = field_value
                return True
        return False

    def fits(self, query):
        query = str.lower(query)
        return query == str.lower(self.name) or query == str.lower(self.surname) or query == self.phone \
               or query == str.lower(self.city) or query == str.lower(self.email)

    @staticmethod
    def validateEmail(email):
        has_at = False
        for symbol in email:
            if symbol == '@':
                has_at = True
            elif symbol == '.' and has_at:
                return True
        return False

    @staticmethod
    def validatePhone(phone):
        return str.isdigit(phone)

    @staticmethod
    def validateField(field):
        return len(field) > 0
