import smartpy as sp

tstorage = sp.TRecord(store = sp.TNat).layout("store")
tparameter = sp.TVariant(one = sp.TNat, two = sp.TNat).layout(("one", "two"))
tprivates = { }
tviews = { }
