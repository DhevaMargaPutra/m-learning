# import the necessary libraries
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
# Generate 2d classification dataset
X, y = make_blobs(n_samples=500, centers=3,
                  n_features=2, random_state=23)
# Plot the generated datasets
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
