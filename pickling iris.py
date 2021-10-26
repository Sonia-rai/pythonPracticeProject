# Pickling iris

import requests
import pickle

Iris_data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text

l1 = Iris_data.split("\n")
# print(l1)

l2=[item.split(',') for item in l1 if len(item)!=0]  # List comprehension
# print(l2)

with open("Iris_pkl_dataset.dat","wb") as f:
    pickle.dump(l2,f)

with open("Iris_pkl_dataset.dat","rb") as f:
    print(pickle.load(f))


