# %%
from datetime import date
# pip install python-dateutil
from dateutil.relativedelta import relativedelta


# %%
class Address:
    def __init__(self, street, tumbon, amphur, province, zipcode):
        self.street = street
        self.tumbon = tumbon
        self.amphur = amphur
        self.province = province
        self.zipcode = zipcode

    def __str__(self):
        return "{}\n{} {}\n{} {}".format(self.street, self.tumbon,
                                            self.amphur, self.province, self.zipcode)


# %%
class Employee:
    def __init__(self, fname, lname, sex, dob: date, regis_addr: Address,
                 contact_addr: Address):
        self.fname = fname
        self.lname = lname
        self.sex = sex
        self.dob = dob
        self.regis_addr = regis_addr
        self.contact_addr = contact_addr

    def age_ymd(self):
        a = relativedelta(date.today(), self.dob)
        return a.years, a.months, a.days

    def age(self):
        return date.today().year - self.dob.year


# %%
class Customer:
    def __init__(self, fname, lname, sex, dob: date, regis_addr: Address,
                 contact_addr: Address):
        self.fname = fname
        self.lname = lname
        self.sex = sex
        self.dob = dob
        self.address = {"regis": regis_addr, "contact": contact_addr}


# %%
if __name__ == '__main__':
    p = Customer("Peter", "Parker", "M", date(1996,10,25), Address("254", ""))
