# Is that cheating? One could argue that a knowledge of NumPy's technicalities is as valid as some
# clever solution. I'm not sure, to be honest, but I'm moving to the next one. The answer is 5537376230.
import numpy as np

nums = np.loadtxt('p13_numbers.txt', dtype=np.float64)  # the trick is to use float64
print(sum(nums))