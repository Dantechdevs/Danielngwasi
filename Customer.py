from Parent import User


class Customer(User):
    def __init__(self, fullname, age, address, account_id,
                 password, email, phoneNo, schedule, user_type, balance, years, membership):
        super().__init__(fullname, age, address, account_id,
                         password, email, phoneNo, schedule, user_type)
        self.balance = balance
        self.years = years
        self.membership = membership

    def viewInformation(self):
        print(f"""
            name -> {self.fullname}
            age ->  {self.age}
            address ->  {self.address}
            email -> {self.email}
            role   -> {self.user_type}
        """)

    def editInformation(self, username, age, address, email):
        self.username = username
        self.age = age
        self.address = address
        self.email = email

    def viewSchedule(self):
        return self.schedule

    def printSchedule(self):
        print(f'your schedule -> {self.schedule}')

    def topUpBalance(self, topUp):
        self.balance = self.balance+float(topUp)

    def viewPayments(self):
        return self.balance

    def printPayments(self):
        print(f'your balance is -> {self.balance}')
