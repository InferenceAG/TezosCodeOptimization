import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(bool = sp.TBool, store = sp.TIntOrNat).layout(("bool", "store")))
    self.init(bool = False,
              store = 0)

  @sp.entry_point
  def minimum(self, params):
    self.data.bool = False
    minVal = sp.local("minVal", sp.min(params.valA, params.valB))
    sp.if minVal.value == 3:
      self.data.bool = True
    self.data.store = minVal.value

sp.add_compilation_target("test", Contract())