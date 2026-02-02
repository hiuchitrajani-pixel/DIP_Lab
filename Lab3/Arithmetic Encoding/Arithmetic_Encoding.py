# Arithmetic Encoding

import numpy as np

# Inputs
alphabets = ["X", "Y", "Z", "W"]
probabs = [0.1, 0.4, 0.3, 0.2]
MESSAGE = "YZXWY"

# Cumulative Probabilities
cumProbs = np.concatenate(([0], np.cumsum(probabs)))

low = 0.0
high = 1.0

print("Initial range: [{:.6f} , {:.6f})\n".format(low, high))

# Encoding Loop
for k in range(len(MESSAGE)):

    idx = alphabets.index(MESSAGE[k])

    range_val = high - low

    low_new = low + range_val * cumProbs[idx]
    high_new = low + range_val * (cumProbs[idx] + probabs[idx])

    low = low_new
    high = high_new

    print("After {} : [{:.6f} , {:.6f})".format(MESSAGE[k], low, high))

# Result
print('\nEncoded range for "{}" is: [{:.6f} , {:.6f})'.format(MESSAGE, low, high))

res = (low + high) / 2
print("Final Tag Value = {:.6f}".format(res))
