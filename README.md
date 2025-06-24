# MLflow Exploration

A comprehensive project demonstrating MLflow capabilities for machine learning model tracking, experimentation, and deployment. This project focuses on apple demand forecasting using synthetic data, showcasing how to log experiments, manage models, and serve predictions via a REST API.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Tutorial & Presentation](#tutorial--presentation)
- [Model Details](#model-details)
- [Contributing](#contributing)

## 🎯 Overview

This project explores MLflow's core functionalities through a practical example of apple demand forecasting. It demonstrates:

- **Experiment Tracking**: Logging parameters, metrics, and artifacts
- **Model Management**: Versioning and organizing ML models
- **Model Deployment**: Serving models via REST API
- **MLflow UI**: Interactive experiment management interface

The project uses a RandomForest model to predict apple demand based on various features like temperature, rainfall, pricing, and promotional activities.

## 📁 Project Structure

```
MLflow-exploration/
├── README.md                          # Project documentation
├── .gitignore                         # Git ignore rules
├── logging-first-model.ipynb          # Jupyter notebook for model training
├── app.py                             # Flask API for model serving
├── request.py                         # Test script for API requests
└── MLflow-exploration.pdf             # Tutorial presentation
```

## ✨ Features

- **Synthetic Data Generation**: Creates realistic apple sales data with seasonality
- **Model Training**: RandomForest regressor with hyperparameter logging
- **Experiment Management**: Organized experiments with tags and metadata
- **Model Serving**: REST API endpoint for real-time predictions
- **Comprehensive Testing**: Multiple ways to test the deployed model

## 🔧 Prerequisites

- Python 3.8+
- MLflow
- Flask
- Scikit-learn
- Pandas
- NumPy
- Requests

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/novelxv/MLflow-exploration.git
   cd MLflow-exploration
   ```

2. **Install dependencies**:
   ```bash
   pip install mlflow flask scikit-learn pandas numpy requests
   ```

3. **Start MLflow tracking server**:
   ```bash
   mlflow server --host 127.0.0.1 --port 8080
   ```

## 📖 Usage

### 1. Model Training

Run the Jupyter notebook to train and log your first model:

```bash
jupyter notebook logging-first-model.ipynb
```

The notebook will:
- Generate synthetic apple sales data
- Train a RandomForest model
- Log parameters, metrics, and the model to MLflow
- Create experiments with proper tagging

### 2. Model Deployment

Start the Flask API server:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### 3. Making Predictions

Test the API using the provided script:

```bash
python request.py
```

Or use PowerShell:

```powershell
$body = @{
    "average_temperature" = @(25.5, 30.2)
    "rainfall" = @(2.1, 0.5)
    "weekend" = @(1, 0)
    "holiday" = @(0, 0)
    "price_per_kg" = @(1.5, 2.0)
    "promo" = @(1, 0)
    "previous_days_demand" = @(1200, 1100)
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/predict" -Method POST -Body $body -ContentType "application/json"
```

## 🔌 API Documentation

### POST /predict

Predicts apple demand based on input features.

**Request Body**:
```json
{
    "average_temperature": [25.5, 30.2],
    "rainfall": [2.1, 0.5],
    "weekend": [1, 0],
    "holiday": [0, 0],
    "price_per_kg": [1.5, 2.0],
    "promo": [1, 0],
    "previous_days_demand": [1200, 1100]
}
```

**Response**:
```json
{
    'predictions': [1496.0293853175344, 947.1538219929763, 1473.669462202623]
}
```

**Features Description**:
- `average_temperature`: Average daily temperature (°C)
- `rainfall`: Daily rainfall amount (mm)
- `weekend`: Binary flag (1 = weekend, 0 = weekday)
- `holiday`: Binary flag (1 = holiday, 0 = regular day)
- `price_per_kg`: Apple price per kilogram
- `promo`: Binary flag (1 = promotional period, 0 = regular)
- `previous_days_demand`: Previous day's demand quantity

## 📊 Tutorial & Presentation

For a comprehensive tutorial and explanation of MLflow concepts, refer to the presentation file:

📎 **[Tutorial Presentation](./MLflow-exploration.pdf)**

The presentation covers:
- MLflow fundamentals and architecture
- Step-by-step implementation guide
- Best practices for ML experiment tracking
- Deployment strategies

## 🤖 Model Details

- **Algorithm**: Random Forest Regressor
- **Framework**: Scikit-learn
- **Target**: Apple demand prediction
- **Features**: 7 input features (temperature, rainfall, pricing, etc.)
- **Metrics**: MAE, MSE, RMSE, R²

### Model Parameters

```python
{
    "n_estimators": 100,
    "max_depth": 6,
    "min_samples_split": 10,
    "min_samples_leaf": 4,
    "bootstrap": True,
    "random_state": 888
}
```

## 🔍 MLflow UI

Access the MLflow tracking UI at `http://127.0.0.1:8080` to:

- View experiment runs and compare metrics
- Examine logged parameters and artifacts
- Download or deploy registered models
- Analyze model performance over time

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Notes

- Ensure MLflow server is running before executing the notebook or API
- The synthetic data is for demonstration purposes only
- Model performance metrics are artificially good due to the synthetic nature of the data
- For production use, replace with real-world data and implement proper validation

## 🔗 Useful Links

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

---

**Happy MLflow Exploration! 🚀**