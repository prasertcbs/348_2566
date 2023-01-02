# %% [markdown]
# # Example 1: Wallet
# %%
class Wallet:
    def __init__(self):
        self.amount = 0

    def earn(self, a):
        self.amount += a

    def spend(self, a):
        self.amount -= a

    def __str__(self):
        return f"amount = {self.amount}"


# %%
dad = Wallet()
dad.earn(100)
print("dad's wallet", dad)
mom = dad
print(mom is dad)
print("mom's wallet", mom)
mom.spend(20)
print("mom's wallet", mom)
print("dad's wallet", dad)
# print(hex(id(dad)), hex(id(mom)))
print(f"{id(dad):x} {id(mom):x}")

kid = Wallet()
kid.earn(500)
mom = kid
print(f"{id(dad):x} {id(mom):x} {id(kid):x}")

mom.earn(40)
print("kid's wallet", kid)  

# %% [markdown]
# # Example 2: List
# %%
def hero():
    peter = "peter parker"
    spiderman = peter
    print(peter is spiderman)
    print(id(peter),  id(spiderman))
    print(id(peter) == id(spiderman))

hero()
# %%
def demo_obj_ref():
    m = ["pikachu"] # list object (mutable)
    n = m
    m.append("bulbasaur")
    print(n)
    n.append("eevee")
    print(m)
    print(id(m), id(n))

demo_obj_ref()
