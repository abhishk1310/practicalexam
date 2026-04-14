from sklearn.preprocessing import Binarizer
import numpy as np
arr = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
binarizer = Binarizer(threshold=5)
binarized_arr = binarizer.fit_transform(arr)
print("original array:",arr)
print("binarized array:",binarized_arr)