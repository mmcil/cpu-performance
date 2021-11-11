import time

import numpy as np

s_time = time.time()

row_size = 10000
col_size = 10000

arr1 = np.random.rand(row_size, col_size)
arr2 = np.random.rand(row_size, col_size)
arr3 = np.random.rand(row_size, col_size)

print(np.matmul(arr1, arr2, arr3))
print("- %s seconds -" % (time.time() - s_time))
