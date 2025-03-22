# Mental Health Prediction

This project uses machine learning to predict anxiety and depression scores based on various features including demographic information, lifestyle factors, and psychological indicators.

## Project Structure

```
Mental-Health-Prediction/
├── Datasets/                    # Data files
│   └── anxiety_depression_data.csv
├── notebooks/                   # Jupyter notebooks
│   └── Main.ipynb
├── src/                        # Source code
│   └── utils.py               # Utility functions
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                # Git ignore rules
```

## Features

- Data preprocessing and feature engineering
- Feature selection using correlation analysis and SelectKBest
- Multiple ML models (SVM, Random Forest)
- Hyperparameter tuning with cross-validation
- Model evaluation and visualization

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/Main.ipynb
   ```

## Data Description

The dataset contains various features including:

- Demographic information (Age, Gender, Education Level)
- Lifestyle factors (Sleep Hours, Physical Activity)
- Psychological indicators (Social Support, Self Esteem)
- Target variables (Anxiety Score, Depression Score)

## Links

- [Dataset](https://www.kaggle.com/datasets/ak0212/anxiety-and-depression-mental-health-factors)
- [GitHub Repository](https://github.com/chetakk/Mental-Health-Prediction)
- [Project Documentation](https://github.com/chetakk/Mental-Health-Prediction/wiki)
- [Word File](https://1drv.ms/w/s!AqXrHeGIsIV8eR7u04yYreSDSrc?e=FDwv3y)
- [Litrature Review (excel-sheet)](https://1drv.ms/x/s!AqXrHeGIsIV8dECFBNdRXKXbSSo?e=1tapvx)

  

