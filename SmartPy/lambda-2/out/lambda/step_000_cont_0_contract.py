import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(store = sp.TNat).layout("store"))
    self.init(store = 0)

  @sp.entry_point
  def minTen(self, params):
    temp = sp.local("temp", (((((((((params + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1)
    temp.value = (((((((((temp.value + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1
    self.data.store = temp.value

sp.add_compilation_target("test", Contract())