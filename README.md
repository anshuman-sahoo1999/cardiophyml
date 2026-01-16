# CardioPhyML

> **Physics-Informed Machine Learning for Dynamic Cardiovascular Risk Assessment from ECG Time-Series Data**

`CardioPhyML` is an open-source Python package that combines **physiological signal processing** and **interpretable risk modeling** to estimate cardiovascular health from standard ECG recordings. Designed for researchers in digital health, cardiology, computational physiology, and biomedical engineering.

![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-pytest-success)

## 🌟 Features

- Processes ECG CSV files with columns `time` and `lead_II` (or `ecg`)
- Cleans signal and detects R-peaks using state-of-the-art algorithms (`neurokit2`)
- Computes clinically relevant metrics:
  - Heart Rate (BPM)
  - HRV (RMSSD in milliseconds)
  - Personalized cardiovascular risk score (0–100)
- Provides both **command-line interface (CLI)** and **Python API**
- Fully open-source, reproducible, and research-ready

## 📦 Installation

```bash
git clone https://github.com/yourname/cardiophyml.git
cd cardiophyml
pip install -e .
```

## 📝 Usage

```python
cardiophyml
# Then enter path when prompted
```
