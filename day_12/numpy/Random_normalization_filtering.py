#12. Random Dataset Normalization + Filtering
#Scenario:
#● Generate 8 random float values between 0 and 1.
#Task:
#1. Normalize by multiplying with 100
#2. Filter values greater than 50
#3. Sort the filtered values

import numpy as np

values = np.random.rand(8)          # 8 random floats between 0 and 1
normalized = values * 100            # scale to 0–100
filtered = normalized[normalized > 50]
sorted_values = np.sort(filtered)

print("Normalized:", normalized)
print("Values greater than 50, sorted:", sorted_values)
