
#%%
class Test:
    def __init__(self):
        self.text = "Hello world"

    def __str__(self):
        return self.text

    def __repr__(self) -> str:
        return "repr text"

t = Test()
# %%
t
# %%
