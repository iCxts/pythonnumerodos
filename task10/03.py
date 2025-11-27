import numpy as np

def calculate_ridge_loss(y_true: np.ndarray, y_pred: np.ndarray, w: np.ndarray, reg_lambda: float) -> float:
    mse = np.mean((y_pred - y_true) ** 2)
    reg_term = reg_lambda * np.sum(w ** 2)
    return mse + reg_term


def calculate_ridge_gradients(
    X: np.ndarray,
    y: np.ndarray,
    y_pred: np.ndarray,
    w: np.ndarray,
    reg_lambda: float
) -> tuple:
    n_samples = X.shape[0]
    error = y_pred - y

    dw_mse = (2.0 / n_samples) * X.T @ error
    db = (2.0 / n_samples) * np.sum(error)

    dw = dw_mse + 2.0 * reg_lambda * w

    return dw, db


def train_ridge_regression(
    X: np.ndarray,
    y: np.ndarray,
    learning_rate: float = 0.01,
    reg_lambda: float = 0.1,
    n_iterations: int = 1000
) -> tuple:
    n_samples, n_features = X.shape
    w = np.random.randn(n_features) * 0.01
    b = 0.0

    loss_history = []

    for _ in range(n_iterations):
        y_pred = X @ w + b

        loss = calculate_ridge_loss(y, y_pred, w, reg_lambda)
        loss_history.append(loss)

        dw, db = calculate_ridge_gradients(X, y, y_pred, w, reg_lambda)

        w -= learning_rate * dw
        b -= learning_rate * db

    return w, b, loss_history


_, _, _ = train_ridge_regression(
    X, y,
    learning_rate=0.01,
    reg_lambda=0.1,
    n_iterations=500
)
