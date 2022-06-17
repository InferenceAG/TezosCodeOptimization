# Store Value - Example for illustrative purposes only.
import smartpy as sp

class Demo(sp.Contract):
    def __init__(self, alice ):
        self.init(
            ledger = sp.big_map(
            l={ alice: sp.nat(10)},
            tkey=sp.TAddress,
            tvalue=sp.TNat,
        ),
            result=0,
        )

    @sp.entry_point
    def division(self, value):
        with sp.if_ (self.data.ledger[sp.sender] != 0):
            self.data.result = value // self.data.ledger[sp.sender]

if "templates" not in __name__:
    
    @sp.add_test(name = "repeated-usage") 
    def test():
        
        scenario = sp.test_scenario()
        alice = sp.test_account('Alice')
        demoContract = Demo(alice.address)
        scenario += demoContract

        scenario += demoContract.division(22).run(alice)
        scenario.verify(demoContract.data.result==2)