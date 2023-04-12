from faker import Faker

class BaseContact():
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}"

    def label_length(self):
        return f"First name lenght: {len(self.first_name)}\nLast name lenght: {len(self.last_name)}"

        
class BusinessContact(BaseContact):
    def __init__(self, job, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_number = business_number

    def contact(self):
        return f"Wybieram numer {self.business_number} i dzwonię do {self.first_name} {self.last_name}"

def create_contacts(contact_type, quantity):
    fake = Faker()
    contacts = []
    if contact_type == "base":
        for x in range(int(quantity)):
            contacts.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email()))
    elif contact_type == "business":
        for x in range(quantity):
            contacts.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email(), job=fake.job(), company=fake.company(), business_number=fake.phone_number()))
    return contacts







