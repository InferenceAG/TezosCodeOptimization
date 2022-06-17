import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(ledger = sp.TBigMap(sp.TAddress, sp.TNat)).layout("ledger"))
    self.init(ledger = {})

  @sp.entry_point
  def add(self, params):
    self.data.ledger[sp.sender] = self.data.ledger.get(sp.sender, default_value = 0) + params

sp.add_compilation_target("test", Contract())