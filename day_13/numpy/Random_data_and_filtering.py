#8. Random Data & Filtering
#Generate random numbers:nums = np.random.randint(1, 100, 10)
#Task:
#● Filter values that are divisible by 5
#● Return sorted result


import numpy as np

nums = np.random.randint(1,100,10)



filtered = np.sort(nums[nums % 5 == 0])


print("random data:",nums)
print(filtered)

