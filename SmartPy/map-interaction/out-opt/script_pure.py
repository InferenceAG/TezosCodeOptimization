# Example for illustrative purposes only.
import smartpy as sp

class Demo(sp.Contract):
    def __init__(self, ):
        self.init(
            ledger = sp.big_map(
            l={},
            tkey=sp.TAddress,
            tvalue=sp.TNat,
        ),
        )

    @sp.entry_point
    def add(self, value):
        balance = self.data.ledger.get(sp.sender, 0)
        self.data.ledger[sp.sender] = balance + value       

if "templates" not in __name__:
    
    @sp.add_test(name = "map-interaction") 
    def test():
        
        scenario = sp.test_scenario()
        alice = sp.test_account('Alice')
        demoContract = Demo()
        scenario += demoContract

        scenario += demoContract.add(5).run(alice)
        scenario.verify(demoContract.data.ledger[alice.address]==5)

        scenario += demoContract.add(3).run(alice)
        scenario.verify(demoContract.data.ledger[alice.address]==8)
