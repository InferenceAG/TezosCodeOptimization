import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(value1 = sp.TNat, value10 = sp.TNat, value11 = sp.TNat, value12 = sp.TNat, value13 = sp.TNat, value14 = sp.TNat, value15 = sp.TNat, value16 = sp.TNat, value2 = sp.TNat, value3 = sp.TNat, value4 = sp.TNat, value5 = sp.TNat, value6 = sp.TNat, value7 = sp.TNat, value8 = sp.TNat, value9 = sp.TNat).layout(("value1", ("value2", ("value3", ("value4", ("value5", ("value6", ("value7", ("value8", ("value9", ("value10", ("value11", ("value12", ("value13", ("value14", ("value15", "value16")))))))))))))))))
    self.init(value1 = 0,
              value10 = 10,
              value11 = 11,
              value12 = 12,
              value13 = 13,
              value14 = 14,
              value15 = 15,
              value16 = 16,
              value2 = 2,
              value3 = 3,
              value4 = 4,
              value5 = 5,
              value6 = 6,
              value7 = 7,
              value8 = 8,
              value9 = 9)

  @sp.entry_point
  def increaseCounter(self):
    self.data.value1 += 1

sp.add_compilation_target("test", Contract())