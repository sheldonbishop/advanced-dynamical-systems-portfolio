from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, classification_report
from sklearn.model_selection import train_test_split
import numpy as np

def train_hybrid_model(df):
    feature_set = ["x_kf", "intervention"] + [c for c in df.columns if c.endswith("_roll_mean") or c.endswith("_roll_std")]
    X = df[feature_set].values
    y = df["event"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = GradientBoostingClassifier(random_state=42)
    model.fit(X_train, y_train)

    p = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, p) if len(np.unique(y_test)) > 1 else float("nan")
    report = classification_report(y_test, (p > 0.5).astype(int), zero_division=0)
    return model, feature_set, auc, report

def score_dataframe(model, df, feature_set):
    out = df.copy()
    out["p_event_ml"] = model.predict_proba(out[feature_set].values)[:, 1]
    return out
