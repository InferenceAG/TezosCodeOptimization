# Code optimizsation example: Local variable
## Notes
Both contracts are doing the same.

## Commands
- SmartPy.sh test lambda.py ./out --mockup --protocol ithaca
- SmartPy.sh test lambda-opt.py ./out-opt --mockup --protocol ithaca

## Storage and gas comparison
contract origination:
| Variant       | storage size | consumed gas | trx costs           |
| ------------- | ------------ | ------------ | ------------------- |
| not optimized | 209          | 1445.374     | ꜩ0.05225 + ꜩ0.06425 |
| optimized     | 182          | 1438.725     | ꜩ0.0455  + ꜩ0.06425 |

calling entrypoint:
| Variant       | consumed gas | trx costs |
| ------------- | ------------ | --------- |
| not optimized | 2092.841     | ꜩ0.000379 |
| optimized     | 2086.042     | ꜩ0.000378 |