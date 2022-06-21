import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(store = sp.TNat).layout("store"))
    self.init(store = 0)

  @sp.entry_point
  def minTen(self, params):
    compute_lambda-opt_18 = sp.local("compute_lambda-opt_18", self.myfunc(params))
    temp = sp.local("temp", compute_lambda-opt_18.value)
    compute_lambda-opt_19 = sp.local("compute_lambda-opt_19", self.myfunc(temp.value))
    temp.value = compute_lambda-opt_19.value
    self.data.store = temp.value

  @sp.private_lambda()
  def myfunc(_x0):
    sp.result(sp.min(sp.min(_x0, 10) + 1, 10))

sp.add_compilation_target("test", Contract())