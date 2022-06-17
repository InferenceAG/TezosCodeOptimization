# Example for illustrative purposes only.
import smartpy as sp


class Demo(sp.Contract):
    def __init__(self, ):
        self.init(
            store = 0,
            bool = False,
        )

    @sp.entry_point
    def minimum(self, valA, valB):
        self.data.bool=False
        
        minVal = sp.local("minVal", sp.min(valA, valB))
        with sp.if_ (minVal.value == 3):
            self.data.bool=True

        self.data.store=minVal.value
        
if "templates" not in __name__:
    
    @sp.add_test(name = "local-variable") 
    def test():
        
        scenario = sp.test_scenario()
        alice = sp.test_account('Alice')
        demoContract = Demo()
        scenario += demoContract

        scenario += demoContract.minimum(valA=3, valB=5).run(alice)
        scenario.verify(demoContract.data.store==3)

        scenario += demoContract.minimum(valA=5, valB=4).run(alice)
        scenario.verify(demoContract.data.store==4)
