# Example for illustrative purposes only.
import smartpy as sp
import sys

loops = 10

class Demo(sp.Contract):
    def __init__(self, ):
        self.init(
            store=0,
        )

    @sp.private_lambda(with_storage="read-write", wrap_call=True)
    def myfunc(self, myvalue):
        tempF = myvalue
        for i in range (1, loops+1):
            tempF = tempF + 1
        sp.result(tempF)

    @sp.entry_point
    def one(self, value):
        temp = sp.local("temp", self.myfunc(value))
        self.data.store=temp.value

    @sp.entry_point
    def two(self, value):
        temp = sp.local("temp", self.myfunc(value))
        self.data.store=temp.value

if "templates" not in __name__:
    
    @sp.add_test(name = "lambda") 
    def test():
        
        scenario = sp.test_scenario()
        alice = sp.test_account('Alice')
        demoContract = Demo()
        scenario += demoContract

        scenario += demoContract.one(sp.nat(5)).run(alice)
        scenario.verify(demoContract.data.store==5+loops)
