def make_composite_observation(df, ignore_cols=None):
    ignore_cols = ignore_cols or ["t", "x_true", "intervention", "event"]
    signal_cols = [c for c in df.columns if c not in ignore_cols]
    out = df.copy()
    out["composite_obs"] = out[signal_cols].mean(axis=1)
    return out

def add_rolling_features(df, signal_cols, window=20):
    out = df.copy()
    for col in signal_cols:
        out[f"{col}_roll_mean"] = out[col].rolling(window, min_periods=1).mean()
        out[f"{col}_roll_std"] = out[col].rolling(window, min_periods=1).std().fillna(0.0)
    return out
