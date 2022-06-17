import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(ledger = sp.TBigMap(sp.TAddress, sp.TNat), result = sp.TNat).layout(("ledger", "result")))
    self.init(ledger = {sp.address('tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi') : 10},
              result = 0)

  @sp.entry_point
  def division(self, params):
    denominator = sp.local("denominator", self.data.ledger[sp.sender])
    sp.if denominator.value != 0:
      self.data.result = params // denominator.value

sp.add_compilation_target("test", Contract())