import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(value1 = sp.TIntOrNat, value10 = sp.TIntOrNat, value11 = sp.TIntOrNat, value12 = sp.TIntOrNat, value13 = sp.TIntOrNat, value14 = sp.TIntOrNat, value15 = sp.TIntOrNat, value16 = sp.TIntOrNat, value2 = sp.TIntOrNat, value3 = sp.TIntOrNat, value4 = sp.TIntOrNat, value5 = sp.TIntOrNat, value6 = sp.TIntOrNat, value7 = sp.TIntOrNat, value8 = sp.TIntOrNat, value9 = sp.TIntOrNat).layout((((("value1", "value10"), ("value11", "value12")), (("value13", "value14"), ("value15", "value16"))), ((("value2", "value3"), ("value4", "value5")), (("value6", "value7"), ("value8", "value9"))))))
    self.init(value1 = 1,
              value10 = 10,
              value11 = 11,
              value12 = 12,
              value13 = 13,
              value14 = 14,
              value15 = 15,
              value16 = 0,
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
    self.data.value16 += 1

sp.add_compilation_target("test", Contract())