import re

class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
        
class Employee:
    def __init__(self, row):
        self.first_name, self.last_name = parse_name(row)
        self.address = parse_address(row)
        self.email = parse_email(row)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.email}, {self.address.street}, {self.address.city}, {self.address.state}'

def parse_name(text):
    name_pattern = re.compile(r'(\w+)\s(\w+)')
    return name_pattern.search(text).groups()

def parse_address(text):
    address_pattern = re.compile(r'(\d+\s\w+\s\w+),\s(\w+),\s(\w{2})')
    match = address_pattern.search(text)
    if match:
        street, city, state = match.groups()
        return Address(street, city, state)
    else:
        # Return a default Address object if no match is found
        return Address("Unknown Street", "Unknown City", "Unknown State")

def parse_email(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    return email_pattern.search(text).group()

def main(path):
    employee_list = []
    with open(path, 'r') as file:
        for line in file:
            employee_list.append(Employee(line))
    return employee_list

employee_list = main("people.txt")
print(employee_list)