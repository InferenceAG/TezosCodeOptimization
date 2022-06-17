import smartpy as sp

tstorage = sp.TRecord(ledger = sp.TBigMap(sp.TAddress, sp.TNat), result = sp.TNat).layout(("ledger", "result"))
tparameter = sp.TVariant(division = sp.TNat).layout("division")
tprivates = { }
tviews = { }
