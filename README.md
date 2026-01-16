CardioPhyML
===========

Physics-Inspired Machine Learning for Cardiovascular Signal Analysis

Overview
--------

CardioPhyML is an open-source Python package for **file-driven cardiovascular signal analysis and interpretable risk modeling** using physiological time-series data such as ECG signals.

The package enables researchers to upload structured signal datasets and automatically obtain **cleaned signals, extracted cardiac features, analytical visualizations, and reproducible summaries**, supporting experimental and methodological research in biomedical signal processing.

Key Features
------------

*   CSV-based ECG and physiological data ingestion
    
*   Automated signal preprocessing and noise reduction
    
*   R-peak detection and heart rate variability (HRV) feature extraction
    
*   Feature-based cardiovascular risk modeling
    
*   Interpretable analytical outputs and visualizations
    
*   Python API and command-line interface (CLI)
    
*   Modular and extensible architecture for research workflows
    

Intended Use
------------

CardioPhyML is intended for:

*   Biomedical signal processing research
    
*   Cardiovascular data analytics and experimentation
    
*   Machine learning studies on physiological signals
    
*   Educational and reproducible research workflows
    

**Disclaimer:**This software is **not a medical device** and must not be used for clinical diagnosis or treatment.All outputs are intended strictly for **research and academic purposes**.

Installation
------------

### Requirements

*   Python 3.8 or higher
    
*   pip package manager
    

### Install from source

`   git clone https://github.com/anshuman-sahoo1999/cardiophyml.git  cd cardiophyml  pip install -r requirements.txt  pip install .   `

Input Data Format
-----------------

CardioPhyML accepts CSV files containing physiological time-series data.

Example ECG CSV structure:

timesignal0.000.0210.010.0340.020.029

*   time: time index in seconds
    
*   signal: ECG amplitude values
    

Additional metadata columns may be included depending on the analysis pipeline.

Usage
-----

### Python API

`   from cardiophyml import CardioAnalyzer  analyzer = CardioAnalyzer(      input_file="sample_ecg.csv",      sampling_rate=250  )  results = analyzer.run_analysis()  results.summary()   `

### Command Line Interface

`   cardiophyml analyze --input sample_ecg.csv --sampling-rate 250   `

Output
------

After execution, CardioPhyML generates:

*   Cleaned ECG signals
    
*   Detected R-peaks
    
*   Heart rate variability (HRV) metrics
    
*   Feature summaries
    
*   Risk score estimations
    
*   Publication-ready plots and reports
    

All outputs are stored in a structured results directory to ensure reproducibility.

Project Structure
-----------------

`   cardiophyml/  ├── cardiophyml/  │   ├── preprocessing/  │   ├── feature_extraction/  │   ├── modeling/  │   ├── visualization/  │   └── utils/  ├── tests/  ├── examples/  ├── docs/  ├── requirements.txt  ├── setup.py  └── README.md   `

Testing
-------

Run the test suite using:

`   pytest tests/   `

Tests validate:

*   Signal preprocessing consistency
    
*   Feature extraction correctness
    
*   End-to-end analysis pipelines
    

Documentation
-------------

*   Inline docstrings follow NumPy documentation standards
    
*   Example workflows are provided in the examples directory
    
*   Designed for integration with documentation generators
    

Citation
--------

If you use CardioPhyML in academic work, please cite:

`   @software{cardiophyml,    author = {Sahoo, Anshuman},    title  = {CardioPhyML: A Python Package for Cardiovascular Signal Analysis and Interpretable Risk Modeling},    year   = {2026},    url    = {https://github.com/anshuman-sahoo1999/cardiophyml}  }   `

License
-------

This project is licensed under the MIT License.See the LICENSE file for details.

Contributing
------------

Contributions are welcome.Please open an issue or submit a pull request for bug fixes, enhancements, or documentation improvements.

Acknowledgements
----------------

This package builds upon established research in:

*   Biomedical signal processing
    
*   Heart rate variability analysis
    
*   Interpretable machine learning
    

Scientific references will be provided in the accompanying JOSS manuscript.

Contact
-------

Anshuman SahooDepartment of Computer Science and EngineeringDRIEMS University, IndiaEmail: anshuman.sahoo@driems.ac.in
