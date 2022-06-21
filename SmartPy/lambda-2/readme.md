# Code optimizsation example: Lambda
## Notes
Both contracts are doing the same.

## Commands
- SmartPy.sh test lambda.py ./out --mockup --protocol ithaca
- SmartPy.sh test lambda-opt.py ./out-opt --mockup --protocol ithaca

## Storage and gas comparison
### 9 loops
contract origination:
| Variant       | storage size | consumed gas | trx costs           |
| ------------- | ------------ | ------------ | ------------------- |
| not optimized | 137          | 1434.183     | ꜩ0.03425 + ꜩ0.06425 |
| optimized     | 146          | 1432.387     | ꜩ0.0365  + ꜩ0.06425 |

calling entrypoint:
| Variant       | consumed gas | trx costs |
| ------------- | ------------ | --------- |
| not optimized | 2080.864     | ꜩ0.000378 |
| optimized     | 2079.566     | ꜩ0.000377 |

### 10 loops
contract origination:
| Variant       | storage size | consumed gas | trx costs           |
| ------------- | ------------ | ------------ | ------------------- |
| not optimized | 145          | 1437.104     | ꜩ0.03625 + ꜩ0.06425 |
| optimized     | 150          | 1433.848     | ꜩ0.0375  + ꜩ0.06425 |

calling entrypoint:
| Variant       | consumed gas | trx costs |
| ------------- | ------------ | --------- |
| not optimized | 2084.073     | ꜩ0.000378 |
| optimized     | 2081.243     | ꜩ0.000378 |