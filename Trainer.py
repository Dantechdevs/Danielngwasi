from Parent import User


class Trainer(User):
    def viewSchedule(self):
        return self.schedule

    def printSchedule(self):
        print(f'trainer schedule -> {self.schedule}')

    def printInfo(self):
        print(f"""
            name -> {self.fullname}
            age ->  {self.age}
            address ->  {self.address}
            email -> {self.email}
            role   -> {self.user_type}
        """)
