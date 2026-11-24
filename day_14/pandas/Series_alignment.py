#7. Data Alignment Issue in Series Addition
#Two Series:
#S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
#S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
#Task:
#● Add both Series
#● Explain why some values become NaN
#● Replace NaN with 0 and compute final result

import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

result = S1.add(S2, fill_value=0)

print(result)


#NaN appears because Pandas aligns Series by index, and indexes missing from either Series have no matching value.
