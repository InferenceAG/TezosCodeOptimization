import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(bool = sp.TBool, store = sp.TIntOrNat).layout(("bool", "store")))
    self.init(bool = False,
              store = 0)

  @sp.entry_point
  def minimum(self, params):
    self.data.bool = False
    sp.if sp.min(params.valA, params.valB) == 3:
      self.data.bool = True
    self.data.store = sp.min(params.valA, params.valB)

sp.add_compilation_target("test", Contract())