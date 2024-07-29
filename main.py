from collections import UserDict 

 
class Field: 
    def __init__(self, value): 
        self.value = value 
 
    def __str__(self): 
        return str(self.value) 
 
class Name(Field): 
    def __init__(self, value):
        if not value:
            raise ValueError("Name is required field.")
        super().__init__(value) 
 
class Phone(Field): 
    def __init__(self, value): 
        if not self._validate_phone(value): 
            raise ValueError("Phone number must contain exactly 10 digits.") 
        super().__init__(value) 

    @staticmethod
    def _validate_phone(phone):
        return phone.isdigit() and len(phone) == 10
 
class Record: 
    def __init__(self, name): 
        self.name = Name(name) 
        self.phones = [] 
 
    def add_phone(self, phone): 
        self.phones.append(Phone(phone)) 
 
    def remove_phone(self, phone): 
        self.phones = [p for p in self.phones if p.value != phone] 
 
    def edit_phone(self, old_phone, new_phone): 
        for phone in self.phones: 
            if phone.value == old_phone:
                phone.value = new_phone 
                return True
            return False
             
    def find_phone(self, phone): 
        for p in self.phones: 
            if p.value == phone: 
                return p 
        return None 
 
    def __str__(self): 
        phones = ";".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}" 
 
class AddressBook(UserDict): 
    def add_record(self, record): 
        self.data[record.name.value] = record 
 
    def find(self, name): 
        return self.data.get(name, None) 
 
    def delete(self, name): 
        if name in self.data: 
            del self.data[name] 
 
 
if __name__ == "__main__":   
    
    book = AddressBook() 
     
    john_record = Record("John") 
    john_record.add_phone("1234567890") 
    john_record.add_phone("5555555555") 
 
     
    book.add_record(john_record) 
 
     
    jane_record = Record("Jane") 
    jane_record.add_phone("9876543210") 
    book.add_record(jane_record) 
 
     
    for name, record in book.data.items(): 
        print(record) 
 
     
    john = book.find("John") 
    if john: 
        john.edit_phone("1234567890", "1112223333") 
        print(john)   
 
    found_phone = john.find_phone("5555555555") 
    if found_phone: 
        print(f"{john.name}: {found_phone}")  
 
     
    book.delete("Jane") 
 
     
    for name, record in book.data.items(): 
        print(record)