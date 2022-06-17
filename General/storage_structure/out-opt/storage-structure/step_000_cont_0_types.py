import smartpy as sp

tstorage = sp.TRecord(value1 = sp.TNat, value10 = sp.TNat, value11 = sp.TNat, value12 = sp.TNat, value13 = sp.TNat, value14 = sp.TNat, value15 = sp.TNat, value16 = sp.TNat, value2 = sp.TNat, value3 = sp.TNat, value4 = sp.TNat, value5 = sp.TNat, value6 = sp.TNat, value7 = sp.TNat, value8 = sp.TNat, value9 = sp.TNat).layout(("value1", ("value2", ("value3", ("value4", ("value5", ("value6", ("value7", ("value8", ("value9", ("value10", ("value11", ("value12", ("value13", ("value14", ("value15", "value16"))))))))))))))))
tparameter = sp.TVariant(increaseCounter = sp.TUnit).layout("increaseCounter")
tprivates = { }
tviews = { }
