---
title: "CardioPhyML: A Python Package for File-Driven Cardiovascular Signal Analysis and Interpretable Risk Modeling"
tags:
  - Python
  - cardiovascular signal processing
  - ECG analysis
  - heart rate variability
  - research software
authors:
  - name: Anshuman Sahoo
    orcid: 0009-000X-XXXX-XXXX
    affiliation: 1
affiliations:
  - name: Department of Computer Science and Engineering, DRIEMS University, India
    index: 1
date: 2026-01-16
bibliography: paper.bib
---

## Summary

CardioPhyML is an open-source Python package designed for file-based cardiovascular signal analysis and interpretable risk modeling using physiological time-series data, particularly electrocardiogram (ECG) signals. The software enables researchers to upload structured signal datasets and obtain cleaned signals, extracted cardiac features, analytical summaries, and reproducible outputs through a unified workflow. CardioPhyML integrates signal preprocessing, heart rate variability (HRV) feature extraction, and feature-based modeling in a modular framework that supports experimental and methodological research in biomedical signal processing.

The package emphasizes transparency, reproducibility, and extensibility, allowing users to adapt the pipeline for diverse datasets and research objectives. CardioPhyML is intended strictly for research and educational use and does not perform clinical diagnosis or treatment.

---

## Statement of Need

Cardiovascular signal analysis plays a central role in biomedical research, with ECG-derived features such as heart rate variability widely used for physiological assessment and methodological studies. While several tools exist for ECG processing, many are either domain-specific, tightly coupled to proprietary environments, or lack reproducible, file-driven workflows suitable for open research.

Researchers often require lightweight, transparent software that allows them to ingest raw physiological data, apply standardized preprocessing, extract interpretable features, and evaluate analytical models without relying on opaque or monolithic systems. CardioPhyML addresses this need by providing a research-oriented Python package that emphasizes modular design, reproducible execution, and interpretability of outputs.

By focusing on file-based inputs and structured analytical outputs, CardioPhyML enables consistent experimentation, comparative studies, and educational use across datasets and research settings.

---

## Functionality

CardioPhyML provides an end-to-end workflow for cardiovascular signal analysis composed of the following components:

- **Data ingestion:** Loading of ECG and physiological time-series data from structured CSV files.
- **Signal preprocessing:** Noise reduction and normalization to prepare signals for analysis.
- **Feature extraction:** Detection of R-peaks and computation of time-domain HRV metrics.
- **Risk modeling:** Feature-based analytical modeling designed for interpretability rather than prediction optimization.
- **Output generation:** Structured summaries, visualizations, and intermediate artifacts to support reproducibility.

The software exposes both a Python application programming interface (API) and a command-line interface (CLI), enabling flexible integration into research pipelines and automated workflows.

---

## Design Principles

The design of CardioPhyML is guided by the following principles:

1. **Reproducibility:** All analyses operate on explicit input files and generate deterministic outputs.
2. **Modularity:** Each processing stage is implemented as an independent component, allowing customization and extension.
3. **Transparency:** Feature extraction and modeling steps are interpretable and traceable.
4. **Accessibility:** The package relies on widely adopted Python libraries and minimal dependencies.

These principles ensure that CardioPhyML can be readily adopted and adapted by researchers with varying levels of expertise.

---

## Related Work

Existing ECG analysis frameworks and signal processing toolkits provide valuable functionality but often emphasize clinical deployment, proprietary ecosystems, or black-box modeling approaches. CardioPhyML complements these tools by prioritizing open research workflows, interpretability, and file-based reproducibility. The package is designed to interoperate with existing scientific Python ecosystems while maintaining a focused scope aligned with research and educational use.

---

## Limitations and Scope

CardioPhyML is not intended for real-time monitoring, clinical diagnosis, or medical decision-making. The software does not implement regulatory-compliant medical algorithms and should not be used in clinical environments. Its scope is limited to offline analysis of physiological time-series data for research purposes.

---

## Availability

- **Source code:** https://github.com/anshuman-sahoo1999/cardiophyml  
- **License:** MIT  
- **Archive and DOI:** https://doi.org/10.5281/zenodo.18265663  

---

## Acknowledgements

The author acknowledges the contributions of the open-source scientific Python community and prior research in biomedical signal processing and heart rate variability analysis, which informed the development of this software.

---

## References
