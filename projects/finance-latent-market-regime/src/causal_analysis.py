import networkx as nx
import statsmodels.api as sm
import numpy as np

def build_causal_graph():
    G = nx.DiGraph()
    G.add_edges_from([
        ("intervention", "x_kf"),
        ("x_kf", "event"),
        ("composite_obs", "x_kf"),
        ("composite_obs", "event"),
    ])
    return G

def estimate_intervention_effect(df):
    out = df.copy()
    out["intercept"] = 1.0
    adj = ["intercept", "intervention", "x_kf", "composite_obs"]
    logit = sm.Logit(out["event"], out[adj])
    res = logit.fit(disp=False)

    X0 = out[adj].copy()
    X1 = out[adj].copy()
    X0["intervention"] = 0
    X1["intervention"] = 1
    ate = float(np.mean(res.predict(X1) - res.predict(X0)))
    return res, ate
