from AdminManager import AdminManager
from Parent import User, Person
from Trainer import Trainer
from Customer import Customer

# customer class operations
print("------------------------customer info--------------------------------------")
customer = Customer("Aisha Alfalasig", "22", "333-556", "23", "aisha222",
                    "aisha@gmail.com", "07668333", "22/3/22", "customer", 400000.99, 2, "Gold")
customer.viewInformation()

customer.editInformation("Aisha Alfalasi", "23",
                         "444-333", "aishaalf@gmail.com")

print("after editing the information")
customer.viewInformation()

customer.printSchedule()
customer.topUpBalance(200.00)
customer.printPayments()


# trainer class operations
print("------------------------trainer info--------------------------------------")
trainer = Trainer("peter washington", "22", "333-556", "23",
                  "peter222", "peter@gmail.com", "076685533", "52/3/22", "trainer")
trainer.printInfo()
trainer.printSchedule()

# admin class operations
print("------------------------adminmanager info--------------------------------------")
admin = AdminManager("peter washington", "22", "333-556", "23",
                     "peter222", "peter@gmail.com", "076685533", "52/3/22", "trainer")
admin.addInfo("peter washington", "peter2ddd")
admin.searchingInfo("peter")
admin.viewInfo()
admin.addRecord("jane doe", "23", "4445-5555", "444", "janedoe222",
                "jane@gmail.com", "2235678888", "3/4/22", "custmer")

admin.searchRecord("444")
admin.printAllRecords()
admin.addPackage(1, "swimming", 400.00)
admin.searchPackage(1)
admin.printAllPackage()

# admin.deleteInfo("peter")
# admin.deleteRecord("444")
# admin.deletePackage("swimming")

admin.viewAllUsernames()
