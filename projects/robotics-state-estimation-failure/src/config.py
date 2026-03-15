PROJECT = {
    "title": "Autonomous Robot State Estimation & Failure Prediction",
    "domain": "Robotics",
    "observable_signals": ['imu_signal', 'encoder_speed', 'lidar_proxy', 'motor_current', 'battery_load'],
    "latent_state": "robot state + motor wear",
    "outcome": "actuator failure probability",
    "intervention": "preventive calibration",
}
