# Airline Passenger Analytics Project

## Objective
A comprehensive Business Intelligence and Machine Learning project analyzing airline passenger satisfaction. This project identifies key drivers of satisfaction, builds predictive models, and provides actionable business recommendations to improve the passenger experience.

## Project Structure
```text
airline-bi-project/
│
├── data/                      # Raw and processed datasets
│   ├── processed/             # Scaled and encoded data for ML
│
├── notebooks/                 # Detailed exploratory and modeling analysis
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb
│
├── src/                       # Modular Python codebase
│   ├── preprocess.py          # Data cleaning and feature engineering
│   ├── train.py               # ML model training (LR, DT, RF)
│   ├── evaluate.py            # Model performance and feature importance
│
├── dashboard/                 # BI design and visualization specs
│   ├── dashboard_spec.md
│
├── models/                    # Serialized ML models (.joblib)
│
├── outputs/                   # Performance metrics and plots
│   ├── plots/
│   ├── metrics.json
│   ├── feature_importance.csv
│
├── report/                    # Final business deliverables
│   ├── insights.md
│   ├── business_recommendations.md
│
├── requirements.txt           # Project dependencies
└── README.md                  # Project overview
```

## Key Findings
- **Top 3 Satisfaction Drivers**: Online Boarding (20.4%), In-flight Wifi (15.8%), and Travel Class (13.1%).
- **The Delay Paradox**: Passenger satisfaction is more influenced by service quality than by operational delays. High-quality service can significantly mitigate the negative impact of delays.
- **Model Performance**: Our Random Forest model achieves a **94.7% accuracy** in predicting passenger satisfaction.

## How to Run
1. **Setup Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r airline-bi-project/requirements.txt
   ```
2. **Execute Pipeline**:
   ```bash
   python3 airline-bi-project/src/preprocess.py
   python3 airline-bi-project/src/train.py
   python3 airline-bi-project/src/evaluate.py
   ```
3. **Explore Notebooks**:
   Open files in the `notebooks/` directory for detailed interactive analysis.

## Business Recommendations
- **Digital Transformation**: Prioritize investments in the online boarding experience and in-flight wifi connectivity.
- **Segmented Strategies**: Develop tailored service packages for personal and economy travelers to address their lower satisfaction levels.
- **Service-Centric Approach**: Focus on consistent high-quality service as a primary competitive advantage, even in the face of operational challenges like delays.
