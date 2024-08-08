# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint
class Train():
    def book(self,train_no,fro,to):
        print(F"Train is booked in train no {train_no} from {fro} to {to}")

    def getStatus(self,train_no):
        print(F"Train is booked succesfully {train_no}")

    def getfare(self,train_no,fro,to):
        print(F"Tain is fare in train no {train_no} from {fro} to {to} is {randint(200,555)}")

obj=Train()
obj.book(12035,"Kopargaon","Delhi")
obj.getStatus(12035)
obj.getfare(12035,"Kopargaon","Delhi")