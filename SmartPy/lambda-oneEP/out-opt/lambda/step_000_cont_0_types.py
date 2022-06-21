import smartpy as sp

tstorage = sp.TRecord(store = sp.TNat).layout("store")
tparameter = sp.TVariant(minTen = sp.TNat).layout("minTen")
tprivates = { "myfunc": sp.TLambda(sp.TNat, sp.TNat, with_storage="read-write") }
tviews = { }
