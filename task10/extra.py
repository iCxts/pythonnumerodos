import numpy as np
import matplotlib.pyplot as plt

def train_batch_gd(
    X: np.ndarray,
    y: np.ndarray,
    learning_rate: float = 0.01,
    n_iterations: int = 1000
) -> tuple:
    n_samples, n_features = X.shape
    w = np.random.randn(n_features) * 0.01
    b = 0.0
    loss_history = []
    for _ in range(n_iterations):
        y_pred = predict(X, w, b)
        loss = compute_mse(y, y_pred)
        loss_history.append(loss)
        dw, db = compute_gradients(X, y, y_pred)
        w -= learning_rate * dw
        b -= learning_rate * db
    return w, b, loss_history

def train_minibatch_gd(
    X: np.ndarray,
    y: np.ndarray,
    batch_size: int = 32,
    learning_rate: float = 0.01,
    n_iterations: int = 1000
) -> tuple:
    n_samples, n_features = X.shape
    w = np.random.randn(n_features) * 0.01
    b = 0.0
    loss_history = []
    for _ in range(n_iterations):
        current_batch_size = min(batch_size, n_samples)
        indices = np.random.choice(n_samples, size=current_batch_size, replace=False)
        X_batch = X[indices]
        y_batch = y[indices]
        y_pred_batch = predict(X_batch, w, b)
        loss = compute_mse(y_batch, y_pred_batch)
        loss_history.append(loss)
        dw, db = compute_gradients(X_batch, y_batch, y_pred_batch)
        w -= learning_rate * dw
        b -= learning_rate * db
    return w, b, loss_history

def train_sgd(
    X: np.ndarray,
    y: np.ndarray,
    learning_rate: float = 0.01,
    n_epochs: int = 100
) -> tuple:
    n_samples, n_features = X.shape
    w = np.random.randn(n_features) * 0.01
    b = 0.0
    loss_history = []
    for _ in range(n_epochs):
        indices = np.random.permutation(n_samples)
        for idx in indices:
            X_i = X[idx:idx+1]
            y_i = y[idx:idx+1]
            y_pred_i = predict(X_i, w, b)
            dw, db = compute_gradients(X_i, y_i, y_pred_i)
            w -= learning_rate * dw
            b -= learning_rate * db
        y_pred_full = predict(X, w, b)
        loss = compute_mse(y, y_pred_full)
        loss_history.append(loss)
    return w, b, loss_history

w_batch, b_batch, loss_batch = train_batch_gd(
    X, y,
    learning_rate=0.01,
    n_iterations=100
)

w_mini, b_mini, loss_mini = train_minibatch_gd(
    X, y,
    batch_size=32,
    learning_rate=0.01,
    n_iterations=100
)

w_sgd, b_sgd, loss_sgd = train_sgd(
    X, y,
    learning_rate=0.01,
    n_epochs=100
)

plt.plot(loss_batch, label="Batch GD")
plt.plot(loss_mini, label="Mini-batch GD")
plt.plot(loss_sgd, label="SGD")
plt.xlabel("Iteration / Epoch")
plt.ylabel("Loss")
plt.legend()
plt.title("Convergence of Batch GD, Mini-batch GD, and SGD")
plt.show()
