# Code optimizsation example: Optimized Map/BigMap interaction
## Notes
Both contracts are doing the same:
- Create a new ledger entry, if not yet existing
- Interpret a sender's balance as "0", if the sender had not a ledger entry.
- Adding value in input parameter to sender's ledger entry.

The optimized example just has two BigMap interactions in, whereas the not optimized has 4.

## Commands
- SmartPy.sh test map-interaction.py ./out --mockup --protocol ithaca
- SmartPy.sh test map-interaction-opt.py ./out-opt --mockup --protocol ithaca

## Storage and gas comparison
contract origination:
| Variant       | storage size | consumed gas | trx costs           |
| ------------- | ------------ | ------------ | ------------------- |
| not optimized | 171          | 1442.406     | ꜩ0.04275 + ꜩ0.06425 |
| optimized     | 127          | 1426.518     | ꜩ0.03175 + ꜩ0.06425 |

calling entrypoint:
| Variant       | consumed gas | trx costs |
| ------------- | ------------ | --------- |
| not optimized | 2700.589     | ꜩ0.000439 |
| optimized     | 2686.156     | ꜩ0.000438 |