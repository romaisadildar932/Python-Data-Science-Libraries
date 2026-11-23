import numpy as np
prices = np.array([100,200,300])
discount = 10
final_price = prices -(prices * discount/100)
print(final_price)

'''broadcasting rules
-Mathematical Dimensions
-Expanding single elements
-Incompatible shapes'''
