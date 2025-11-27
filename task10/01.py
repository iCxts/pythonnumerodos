def train_minibatch_gd(
    X: np.ndarray,
    y: np.ndarray,
    batch_size: int = 32,
    learning_rate: float = 0.01,
    n_iterations: int = 1000,
    verbose: bool = True,
    log_every_n_step: int = 20,
) -> tuple:
    n_samples, n_features = X.shape
    
    w = np.random.randn(n_features) * 0.01
    b = 0.0
    
    loss_history = []
    
    for i in range(n_iterations):
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
        
        if verbose and (i % log_every_n_step == 0 or i == n_iterations - 1):
            print(f"Iteration {i:4d} | Loss: {loss:.6f}")
    
    return w, b, loss_history
