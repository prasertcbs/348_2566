# %%
class Contact:
    def __init__(self, first_name, last_name, gender, phones):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + "." + last_name[:1] + "@mycompany.com"
        self.gender = gender
        self.phones = phones

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return "name: {} {} ({})\nphone: {}\nemail: {}".format(self.first_name,
                                                               self.last_name,
                                                               self.gender, self.phones,
                                                               self.email)


# %%
if __name__ == '__main__':
    c1 = Contact("Peter", "Parker", "M", ["0882223344", "0991117788"])
    print(c1.email)
    print(c1.phones)
    print(c1)
