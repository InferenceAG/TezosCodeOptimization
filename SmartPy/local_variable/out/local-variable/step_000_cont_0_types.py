import smartpy as sp

tstorage = sp.TRecord(bool = sp.TBool, store = sp.TIntOrNat).layout(("bool", "store"))
tparameter = sp.TVariant(minimum = sp.TRecord(valA = sp.TIntOrNat, valB = sp.TIntOrNat).layout(("valA", "valB"))).layout("minimum")
tprivates = { }
tviews = { }
