import smartpy as sp

tstorage = sp.TRecord(ledger = sp.TBigMap(sp.TAddress, sp.TNat)).layout("ledger")
tparameter = sp.TVariant(add = sp.TNat).layout("add")
tprivates = { }
tviews = { }
