# %% [markdown]
# # __init__()

# %%
class Person:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.country = "Thailand"

    # def __init__(self, fname, lname, country):
    #     self.fname = fname
    #     self.lname = lname
    #     self.country = country


# %%
class Person2:
    def __init__(self, fname=None, lname=None, country="Thailand"):
        self.fname = fname
        self.lname = lname
        self.country = country

    def __str__(self):
        return "fname: {} lname: {} country: {}".format(self.fname, self.lname, self.country)


# %%
# p1 = Person()    # create new instance
# print(p1.fname)
# print(p1.country)
# p2 = Person("Prasert", "Kana", "Thailand")
# print(p2)

# %%
p1 = Person2()
print(p1.fname)
print(p1.country)

# %%
p2 = Person2(fname="Peter")
print(p2.fname, p2.country)

# %%
p3 = Person2("Peter", "Parker")
print(p3)

# %%
p4 = Person2(lname="Swift", fname="Taylor", country="USA")
print(p4)
