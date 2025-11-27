def train_with_lr_schedule(
    X: np.ndarray,
    y: np.ndarray,
    initial_lr: float = 0.1,
    schedule: str = 'exponential',
    n_iterations: int = 1000,
    decay_constant: float = 0.0001,
) -> tuple:

    n_samples, n_features = X.shape
    w = np.random.randn(n_features) * 0.01
    b = 0.0

    learning_rate = initial_lr
    loss_history = []

    for t in range(n_iterations):

        if schedule == 'step':
            learning_rate = initial_lr * (0.9 ** (t // 100))

        elif schedule == 'exponential':
            learning_rate = initial_lr * np.exp(-decay_constant * t)

        elif schedule == 'inverse':
            learning_rate = initial_lr / (1 + decay_constant * t)

        else:
            raise ValueError("Unknown schedule type.")

        y_pred = predict(X, w, b)
        loss = compute_mse(y, y_pred)
        loss_history.append(loss)

        dw, db = compute_gradients(X, y, y_pred)

        w -= learning_rate * dw
        b -= learning_rate * db

    return w, b, loss_history
