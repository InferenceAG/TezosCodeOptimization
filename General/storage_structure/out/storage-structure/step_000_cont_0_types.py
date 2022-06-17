import smartpy as sp

tstorage = sp.TRecord(value1 = sp.TIntOrNat, value10 = sp.TIntOrNat, value11 = sp.TIntOrNat, value12 = sp.TIntOrNat, value13 = sp.TIntOrNat, value14 = sp.TIntOrNat, value15 = sp.TIntOrNat, value16 = sp.TIntOrNat, value2 = sp.TIntOrNat, value3 = sp.TIntOrNat, value4 = sp.TIntOrNat, value5 = sp.TIntOrNat, value6 = sp.TIntOrNat, value7 = sp.TIntOrNat, value8 = sp.TIntOrNat, value9 = sp.TIntOrNat).layout((((("value1", "value10"), ("value11", "value12")), (("value13", "value14"), ("value15", "value16"))), ((("value2", "value3"), ("value4", "value5")), (("value6", "value7"), ("value8", "value9")))))
tparameter = sp.TVariant(increaseCounter = sp.TUnit).layout("increaseCounter")
tprivates = { }
tviews = { }
