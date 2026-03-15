# Dynamic Patient Risk Forecasting System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Domain](https://img.shields.io/badge/Domain-Healthcare-informational)
![Modeling](https://img.shields.io/badge/Modeling-State%20Space%20%2B%20Kalman%20%2B%20Hybrid%20ML-success)

## Executive Summary

This project demonstrates a production-style portfolio workflow for **Healthcare** using:

- **State space modeling** for latent system dynamics
- **Kalman filtering** for denoising and hidden-state estimation
- **Hybrid machine learning** for event-risk prediction
- **Causal analysis** for intervention-effect estimation

The objective is to estimate hidden **patient severity** from noisy signals and predict **ICU transfer / adverse event risk**.

**Business value:** support early deterioration detection and intervention prioritization.

## Observable Signals

- `heart_rate`
- `systolic_bp`
- `spo2`
- `resp_rate`
- `lab_risk`

## Repository Layout

```text
healthcare-dynamic-patient-risk/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── assets/
│   └── architecture.svg
├── notebooks/
│   └── 01_healthcare_dynamic_patient_risk.ipynb
├── scripts/
│   └── run_demo.py
└── src/
    ├── __init__.py
    ├── config.py
    ├── simulate.py
    ├── kalman.py
    ├── features.py
    ├── hybrid_model.py
    └── causal_analysis.py
```

## Quick Start

```bash
pip install -r requirements.txt
jupyter lab
```

Or run the demo script:

```bash
python scripts/run_demo.py
```

## Extensions

- Replace synthetic data with a real dataset
- Upgrade to EKF/UKF or switching state-space models
- Add SHAP, calibration, threshold optimization, and cost-sensitive decisions

## Best-Fit Roles

Health-tech, payer analytics, hospital data science, clinical risk analytics
