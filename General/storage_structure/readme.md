# Code optimizsation example: Storage structure
## Notes
Consider storage layout, if you are using variables which are often accessed (e.g. several times in an EP(including lambda) and throught the contract).

## Commands
- SmartPy.sh test storage-structure.py ./out --mockup --protocol ithaca
- SmartPy.sh test storage-structure-opt.py ./out-opt --mockup --protocol ithaca

## Storage and gas comparison
contract origination:
| Variant       | storage size | consumed gas | trx costs           |
| ------------- | ------------ | ------------ | ------------------- |
| not optimized | 393          | 1459.965     | ꜩ0.09825 + ꜩ0.06425 |
| optimized     | 352          | 1451.629     | ꜩ0.088   + ꜩ0.06425 |

calling entrypoint:
| Variant       | consumed gas | trx costs |
| ------------- | ------------ | --------- |
| not optimized | 2152.821     | ꜩ0.000378 |
| optimized     | 2146.103     | ꜩ0.000377 |