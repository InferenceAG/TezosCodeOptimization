import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(store = sp.TNat).layout("store"))
    self.init(store = 0)

  @sp.entry_point
  def minTen(self, params):
    temp = sp.local("temp", sp.min(sp.min(params, 10) + 1, 10))
    temp.value = sp.min(sp.min(temp.value, 10) + 1, 10)
    self.data.store = temp.value

sp.add_compilation_target("test", Contract())