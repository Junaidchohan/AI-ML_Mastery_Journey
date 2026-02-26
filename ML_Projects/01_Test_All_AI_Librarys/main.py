import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import torch
import torchvision
import tensorflow as tf
from transformers import pipeline
import plotly.express as px

print("All libraries are loaded successfully!")

# Test NumPy
arr = np.array([1, 2, 3, 4, 5])
print("NumPy array:", arr)

# Test Pandas
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print("Pandas DataFrame:\n", df)

# Test PyTorch
x = torch.tensor([1.0, 2.0, 3.0])
print("PyTorch tensor:", x)

# Test TensorFlow
tf_tensor = tf.constant([1, 2, 3])
print("TensorFlow tensor:", tf_tensor)