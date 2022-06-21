import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(store = sp.TNat).layout("store"))
    self.init(store = 0)

  @sp.entry_point
  def one(self, params):
    compute_lambda-opt_22 = sp.local("compute_lambda-opt_22", self.myfunc(params))
    temp = sp.local("temp", compute_lambda-opt_22.value)
    self.data.store = temp.value

  @sp.entry_point
  def two(self, params):
    compute_lambda-opt_27 = sp.local("compute_lambda-opt_27", self.myfunc(params))
    temp = sp.local("temp", compute_lambda-opt_27.value)
    self.data.store = temp.value

  @sp.private_lambda()
  def myfunc(_x0):
    sp.result((((((((((_x0 + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1) + 1)

sp.add_compilation_target("test", Contract())