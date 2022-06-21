# Example for illustrative purposes only.
import smartpy as sp

class Demo(sp.Contract):
    def __init__(self, ):
        self.init(
            store=0,
        )

    @sp.private_lambda(with_storage="read-write", wrap_call=True)
    def myfunc(self, myvalue):
        tempF = sp.min(myvalue,sp.nat(10))
        tempF = sp.min(tempF+1, 10)
        sp.result(tempF)

    @sp.entry_point
    def minTen(self, value):
        temp = sp.local("temp", self.myfunc(value))
        temp.value =self.myfunc(temp.value)
        self.data.store=temp.value

if "templates" not in __name__:
    
    @sp.add_test(name = "lambda") 
    def test():
        
        scenario = sp.test_scenario()
        alice = sp.test_account('Alice')
        demoContract = Demo()
        scenario += demoContract

        scenario += demoContract.minTen(sp.nat(5)).run(alice)
        scenario.verify(demoContract.data.store==7)
