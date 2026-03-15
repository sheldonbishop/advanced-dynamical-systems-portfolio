import numpy as np

def kalman_filter_1d(y, a=0.992, b=0.01, c=1.0, q=0.03, r=0.20, x0=0.0, p0=1.0):
    T = len(y)
    x_hat = np.zeros(T)
    P = np.zeros(T)
    x_hat[0], P[0] = x0, p0

    for t in range(1, T):
        x_pred = a * x_hat[t - 1] + b
        P_pred = a * P[t - 1] * a + q
        S = c * P_pred * c + r
        K = P_pred * c / S
        innovation = y[t] - c * x_pred
        x_hat[t] = x_pred + K * innovation
        P[t] = (1.0 - K * c) * P_pred

    return x_hat, P
