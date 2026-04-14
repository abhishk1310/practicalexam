from sklearn.preprocessing import LabelEncoder
import numpy as np
arr = np.array(['red', 'green', 'blue', 'yellow', 'red', 'green'])
label_encoder = LabelEncoder()
encoded_arr = label_encoder.fit_transform(arr)
print("original array:", arr)
print("encoded array:", encoded_arr)