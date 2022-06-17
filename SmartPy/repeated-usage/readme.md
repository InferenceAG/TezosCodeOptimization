# Code optimizsation example: Repeated usage of a storage variable
## Notes
Both contracts are doing the same.

The optimized example only retrieves the denominator once from the storage, pushes on stack, and uses then in the remainder of the code the already pushed denominator on stack by duplicating it.

## Commands
- SmartPy.sh test repeated-usage.py ./out --mockup --protocol ithaca
- SmartPy.sh test repeated-usage-opt.py ./out-opt --mockup --protocol ithaca

## Storage and gas comparison
contract origination:
| Variant       | storage size | consumed gas | trx costs           |
| ------------- | ------------ | ------------ | ------------------- |
| not optimized | 301          | 1691.485     | ꜩ0.07525 + ꜩ0.06425 |
| optimized     | 285          | 1686.914     | ꜩ0.07125 + ꜩ0.06425 |

calling entrypoint:
| Variant       | consumed gas | trx costs |
| ------------- | ------------ | --------- |
| not optimized | 3164.441     | ꜩ0.000486 |
| optimized     | 2699.257     | ꜩ0.000439 |