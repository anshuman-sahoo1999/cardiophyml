---
title: "CardioPhyML: A Python Package for File-Driven Cardiovascular Signal Analysis and Interpretable Risk Modeling"
tags:
  - Python
  - ECG analysis
  - cardiovascular signal processing
  - heart rate variability
  - research software
authors:
  - name: Anshuman Sahoo
    affiliation: 1
affiliations:
  - name: Department of Computer Science and Engineering, DRIEMS University, India
    index: 1
date: 2026-01-16
bibliography: paper.bib
---

## Abstract

CardioPhyML is an open-source Python software package developed to support reproducible research in cardiovascular signal processing through a file-driven analytical workflow. The package enables researchers to ingest physiological time-series data, particularly electrocardiogram (ECG) signals, and perform standardized preprocessing, feature extraction, and interpretable risk-oriented analysis. By integrating classical signal processing techniques with modular analytical components, CardioPhyML provides a transparent and extensible framework for experimental and methodological studies. The software emphasizes reproducibility, interpretability, and accessibility, making it suitable for academic research, education, and comparative analysis across datasets. CardioPhyML is intended strictly for non-clinical research use and does not perform diagnostic or therapeutic functions.

---

## 1. Introduction

Cardiovascular signal analysis is a foundational area in biomedical engineering and physiological research. Electrocardiogram (ECG) signals, in particular, are widely studied due to their ability to capture cardiac electrical activity and enable the derivation of meaningful physiological indicators such as heart rate variability (HRV). These indicators are frequently used in experimental studies exploring autonomic regulation, stress response, and methodological evaluation of signal processing techniques.

Despite the availability of numerous ECG analysis tools, researchers often encounter challenges related to reproducibility, transparency, and accessibility. Many existing solutions are embedded in proprietary environments, emphasize clinical deployment, or rely on opaque modeling pipelines that limit interpretability. Furthermore, workflows that tightly couple data acquisition with analysis can hinder reproducible experimentation when working with archived or shared datasets.

CardioPhyML addresses these challenges by offering a lightweight, open-source Python package that emphasizes file-based data ingestion, modular processing, and interpretable analytical outputs. The software is designed to facilitate reproducible research workflows, allowing users to apply consistent analysis pipelines across multiple datasets and experimental settings.

---

## 2. Motivation and Statement of Need

Reproducibility is a central concern in computational and biomedical research. File-driven analysis pipelines provide a practical mechanism for ensuring that analyses can be repeated, verified, and extended by independent researchers. In the context of cardiovascular signal processing, such pipelines are particularly valuable due to the variability of data sources, sampling rates, and preprocessing requirements.

While comprehensive toolkits exist for physiological signal analysis, many focus on end-user clinical applications or black-box predictive performance. Researchers conducting methodological studies, algorithm comparisons, or educational demonstrations require software that exposes intermediate steps, supports customization, and avoids unnecessary abstraction.

CardioPhyML was developed to meet this need by providing:
- A transparent pipeline for ECG preprocessing and feature extraction
- Modular components that can be independently evaluated or replaced
- Explicit input-output relationships to support reproducibility
- Minimal assumptions about data provenance or acquisition systems

By focusing on research-oriented functionality rather than clinical deployment, CardioPhyML fills a gap between low-level signal processing libraries and application-specific platforms.

---

## 3. Software Architecture and Design

CardioPhyML follows a modular architecture that separates data ingestion, signal processing, feature extraction, and analytical modeling into distinct components. This design facilitates extensibility and supports independent evaluation of each stage.

### 3.1 Data Ingestion

The software accepts structured CSV files containing time-series physiological signals. Users specify key parameters such as sampling frequency, enabling the package to accommodate datasets from diverse sources. This file-driven approach decouples data acquisition from analysis and supports batch processing of archived datasets.

### 3.2 Signal Preprocessing

Preprocessing modules implement noise reduction, normalization, and baseline correction steps commonly used in ECG analysis. These steps are configurable and explicitly documented, allowing researchers to understand and modify preprocessing behavior as required.

### 3.3 Feature Extraction

CardioPhyML implements classical R-peak detection algorithms and derives time-domain HRV features from detected inter-beat intervals. Feature extraction is performed in a transparent manner, exposing intermediate outputs that can be inspected or exported for further analysis.

### 3.4 Analytical Modeling

Rather than emphasizing predictive optimization, the modeling components focus on feature-based analytical summaries and interpretable risk-oriented indicators. This approach aligns with the needs of methodological research and avoids reliance on opaque machine learning models.

---

## 4. Usage Workflow

A typical CardioPhyML workflow consists of the following steps:

1. Upload a physiological signal file in CSV format
2. Configure analysis parameters such as sampling rate
3. Execute preprocessing and feature extraction
4. Generate structured outputs and visualizations
5. Export results for reporting or comparative analysis

The package provides both a Python API and a command-line interface, enabling integration into scripted experiments, notebooks, and automated pipelines.

---

## 5. Reproducibility and Extensibility

Reproducibility is achieved through deterministic processing, explicit parameter specification, and structured output generation. All intermediate and final outputs can be saved and shared, enabling independent verification of results.

Extensibility is supported through:
- Modular code organization
- Clear separation of concerns
- Minimal external dependencies
- Documentation and example workflows

Researchers can extend CardioPhyML by implementing alternative preprocessing methods, feature sets, or analytical modules without modifying the core architecture.

---

## 6. Related Work

Numerous frameworks and toolkits exist for ECG and physiological signal analysis. Many provide advanced functionality but prioritize clinical deployment, proprietary integration, or black-box modeling. CardioPhyML complements these efforts by focusing on open research workflows, interpretability, and file-based reproducibility. The package draws upon established principles in signal processing and heart rate variability analysis [@malik1996hrv; @pan1985qrs; @acharya2006ecg].

---

## 7. Limitations and Scope

CardioPhyML is not intended for real-time signal processing, clinical diagnosis, or medical decision support. The software does not implement regulatory-compliant algorithms and should not be used in clinical environments. Its scope is limited to offline analysis of physiological time-series data for research, educational, and methodological purposes.

---

## 8. Availability and Maintenance

The source code for CardioPhyML is publicly available under the MIT License. Versioned releases are archived with persistent identifiers to support citation and long-term access.

- Source code: https://github.com/anshuman-sahoo1999/cardiophyml  
- DOI: https://doi.org/10.5281/zenodo.18265663  

The project follows open-source development practices, and contributions from the research community are encouraged.

---

## 9. Conclusion

CardioPhyML provides a transparent, reproducible, and extensible framework for cardiovascular signal analysis in research settings. By emphasizing file-driven workflows and interpretable analytical components, the software supports methodological experimentation, educational use, and comparative studies across datasets. The package contributes to open scientific practice by lowering barriers to reproducible cardiovascular signal analysis using widely adopted Python tools.

---

## Acknowledgements

The development of CardioPhyML was informed by established research in biomedical signal processing and heart rate variability analysis, as well as the contributions of the open-source scientific Python community.

---

## References
