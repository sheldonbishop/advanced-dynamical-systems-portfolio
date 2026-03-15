from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.config import PROJECT
from src.simulate import simulate_system
from src.features import add_rolling_features, make_composite_observation
from src.kalman import kalman_filter_1d
from src.hybrid_model import train_hybrid_model, score_dataframe
from src.causal_analysis import estimate_intervention_effect

def main():
    df = simulate_system(PROJECT["observable_signals"])
    df = make_composite_observation(df)
    x_kf, P = kalman_filter_1d(df["composite_obs"].values)
    df["x_kf"] = x_kf
    df["x_kf_std"] = P ** 0.5
    df = add_rolling_features(df, PROJECT["observable_signals"][:3])

    model, feature_set, auc, report = train_hybrid_model(df)
    df = score_dataframe(model, df, feature_set)
    _, ate = estimate_intervention_effect(df)

    print("Project:", PROJECT["title"])
    print("AUC:", auc)
    print("Estimated intervention effect:", ate)
    print(report)

    plt.figure(figsize=(10, 4))
    plt.plot(df["t"], df["x_true"], label="x_true")
    plt.plot(df["t"], df["x_kf"], label="x_kf")
    plt.legend()
    plt.title(PROJECT["title"])
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
