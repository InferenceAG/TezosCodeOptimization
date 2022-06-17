import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(ledger = sp.TBigMap(sp.TAddress, sp.TNat)).layout("ledger"))
    self.init(ledger = {})

  @sp.entry_point
  def add(self, params):
    sp.if ~ (self.data.ledger.contains(sp.sender)):
      self.data.ledger[sp.sender] = 0
    self.data.ledger[sp.sender] += params

sp.add_compilation_target("test", Contract())