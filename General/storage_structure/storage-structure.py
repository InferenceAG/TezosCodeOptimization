# Example for illustrative purposes only.
import smartpy as sp

class Demo(sp.Contract):
    def __init__(self, ):
        self.init(
            value1 = 1,
            value2 = 2,
            value3 = 3,
            value4 = 4,
            value5 = 5,
            value6 = 6,
            value7 = 7,
            value8 = 8,
            value9 = 9,
            value10 = 10,
            value11 = 11,
            value12 = 12,
            value13 = 13,
            value14 = 14,
            value15 = 15,
            value16 = 0,
        )

    @sp.entry_point
    def increaseCounter(self):
        self.data.value16 += 1
 
if "templates" not in __name__:
    
    @sp.add_test(name = "storage-structure") 
    def test():
        
        scenario = sp.test_scenario()
        alice = sp.test_account('Alice')
        demoContract = Demo()
        scenario += demoContract

        scenario += demoContract.increaseCounter().run(alice)
        scenario.verify(demoContract.data.value16==1)
