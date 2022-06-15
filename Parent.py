class Person:
    def __init__(self, fullname, age, address):
        self.fullname = fullname
        self.age = age
        self.address = address


class User(Person):
    def __init__(self, fullname, age, address, account_id, password,email,phoneNo, schedule, user_type):
        super().__init__(fullname, age, address)
        self.account_id = account_id
        self.password = password
        self.email = email
        self.phoneNo = phoneNo
        self.schedule = schedule
        self.user_type = user_type