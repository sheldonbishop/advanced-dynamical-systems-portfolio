import numpy as np
import pandas as pd

def simulate_system(observable_signals, T=800, a=0.992, b=0.01, q=0.03, intervention_prob=0.06, seed=42):
    rng = np.random.default_rng(seed)
    x = np.zeros(T)
    intervention = np.zeros(T, dtype=int)
    event = np.zeros(T, dtype=int)

    base_c = np.array([0.8, 1.0, 0.6, 0.9, 0.7], dtype=float)
    base_r = np.array([0.20, 0.35, 0.15, 0.25, 0.30], dtype=float)

    C = base_c[:len(observable_signals)]
    R = base_r[:len(observable_signals)]
    Y = np.zeros((T, len(C)))

    for t in range(1, T):
        if rng.random() < intervention_prob:
            intervention[t] = 1
            x[t - 1] = max(0.0, x[t - 1] - rng.uniform(0.15, 0.6))

        x[t] = a * x[t - 1] + b + rng.normal(0.0, np.sqrt(q))
        for j in range(len(C)):
            Y[t, j] = C[j] * x[t] + rng.normal(0.0, np.sqrt(R[j]))

        p_event = 1.0 / (1.0 + np.exp(-(x[t] - 2.4)))
        event[t] = int(rng.random() < p_event * 0.05)

    df = pd.DataFrame(Y, columns=observable_signals)
    df["t"] = np.arange(T)
    df["x_true"] = x
    df["intervention"] = intervention
    df["event"] = event
    return df
