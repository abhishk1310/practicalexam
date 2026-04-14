from sklearn.preprocessing import MinMaxScaler
import numpy as np 
arr = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
normalizer = MinMaxScaler()
normalized_arr = normalizer.fit_transform(arr)
print("original array:",arr)
print("normalized array:",normalized_arr)
