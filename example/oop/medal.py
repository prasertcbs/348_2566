# %%
class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):  # instance method
        return self.gold + self.silver + self.bronze


# %%
class Athlete:
    def dummy(self):
        return "hello"


# %%
class Foo:
    def greeting(self):
        return "hello all"

if __name__ == "__main__":
    th=Medal('th', 9, 20, 30)
    print(th.gold)
    print(Medal.total(th))

# %%
