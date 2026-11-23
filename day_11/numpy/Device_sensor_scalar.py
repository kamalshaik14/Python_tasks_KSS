#2. Device Sensor Value (Scalar Array)
#An IoT device records a single sensor reading = 75.
#Task:
#● Create a 0-D NumPy array with this value.
#● Print the value and check its number of dimensions.

import numpy as np


sensor_reading = np.array(75)


print(sensor_reading)
print("dimension:",sensor_reading.ndim)
