import smartpy as sp

tstorage = sp.TRecord(store = sp.TNat).layout("store")
tparameter = sp.TVariant(minTen = sp.TNat).layout("minTen")
tprivates = { }
tviews = { }
