# Code optimizsation example: Local variable
## Notes
Both contracts are doing the same:
- Do any calculation. The example does a very simple comparision of two values and returns the lower of both values.
- Then an if statment is checking the returned value from the caculation.
- The returned value is then stored in the storage.

The not optimized contract is not using sp.local to define a variable. Thus, as soon as the variable "minVal" is used the values is also "consumed". After consumption of the value, the value has to be generated/calculated again. Thus, the calculation will be done again.

## Commands
- SmartPy.sh test local-variable.py ./out --mockup --protocol ithaca
- SmartPy.sh test local-variable-opt.py ./out-opt --mockup --protocol ithaca

## Storage and gas comparison
contract origination:
| Variant       | storage size | consumed gas | trx costs           |
| ------------- | ------------ | ------------ | ------------------- |
| not optimized | 227          | 1461.461     | ꜩ0.05675 + ꜩ0.06425 |
| optimized     | 185          | 1443.686     | ꜩ0.04625 + ꜩ0.06425 |

calling entrypoint:
| Variant       | consumed gas | trx costs |
| ------------- | ------------ | --------- |
| not optimized | 2147.762     | ꜩ0.000388 |
| optimized     | 2134.744     | ꜩ0.000387 |