import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # for reproducibility

# Number of samples per cluster
n_per_cluster = 25

# Cluster 0 (around [2, 2])
cluster_0 = np.random.randn(n_per_cluster, 2) * 1.5 + [3, 3]
labels_0 = np.zeros(n_per_cluster, dtype=int)

# Cluster 1 (around [8, 8])
cluster_1 = np.random.randn(n_per_cluster, 2) * 1.5 + [7, 7]
labels_1 = np.ones(n_per_cluster, dtype=int)

# Combine clusters
X_train = np.vstack([cluster_0, cluster_1])
y_train = np.concatenate([labels_0, labels_1])

# Query point and k (same as before)
x_query = [7, 3]    # The point you want to predict.
k = 5               # Specifying the neighbours. 


def knn_predict(X_train, y_train, x_query, k):
    distances = np.sqrt(np.sum((X_train - x_query) ** 2, axis=1))
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = y_train[nearest_indices]

    labels, counts = np.unique(nearest_labels, return_counts=True)
    return labels[np.argmax(counts)]


def plot_knn(X_train, y_train, x_query, k):
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    x_query = np.array(x_query)

    # -------- Decision Boundary --------
    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300)
    )

    grid_points = np.c_[xx.ravel(), yy.ravel()]
    grid_predictions = np.array([
        knn_predict(X_train, y_train, point, k)
        for point in grid_points
    ])

    Z = grid_predictions.reshape(xx.shape)

    plt.figure(figsize=(8, 6))

    # Plot decision regions
    plt.contourf(xx, yy, Z, alpha=0.3)

    # -------- Training points --------
    classes = np.unique(y_train)
    for cls in classes:
        plt.scatter(
            X_train[y_train == cls][:, 0],
            X_train[y_train == cls][:, 1],
            label=f"Class {cls}"
        )

    # -------- Query point --------
    plt.scatter(
        x_query[0],
        x_query[1],
        marker="X",
        s=150,
        label="Query Point"
    )

    # -------- Nearest neighbors --------
    distances = np.sqrt(np.sum((X_train - x_query) ** 2, axis=1))
    nearest_indices = np.argsort(distances)[:k]

    # -------- Prediction --------
    pred = knn_predict(X_train, y_train, x_query, k)

    plt.text(
        x_query[0] + 0.3,
        x_query[1] - 0.3,
        f"Predicted: Class {pred}",
        fontsize=8,
        fontweight="bold",
        bbox=dict(facecolor="white", alpha=0.8, edgecolor="black")
        )

    plt.scatter(
        X_train[nearest_indices][:, 0],
        X_train[nearest_indices][:, 1],
        facecolors="none",
        edgecolors="black",
        s=200,
        label=f"{k} Nearest Neighbors"
    )

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"KNN Decision Boundary (k = {k})")
    plt.legend()
    plt.grid(True)
    plt.show()


prediction = knn_predict(X_train, y_train, x_query, k)
print(f"Predicted class for query point {x_query} with k={k}: {prediction}")

plot_knn(X_train, y_train, x_query, k)



