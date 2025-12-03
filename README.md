# 🚆 Train Ticket Price Prediction — MLOps Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Production--Ready-success)

## 📌 Project Overview

This project builds an end-to-end machine learning solution to predict **train ticket prices** based on multiple features including train type, class, source, destination, departure time, and more. The pipeline implements best practices in MLOps with automated preprocessing, feature engineering, model training, hyperparameter tuning, and deployment-ready artifacts.

---

## 🎯 Key Highlights

- ✅ **Automated Pipeline**: End-to-end ML workflow from raw data to trained model
- ✅ **Production Ready**: Modular structure with saved transformers for inference
- ✅ **Multiple Models**: Comparison of various ML algorithms with hyperparameter tuning
- ✅ **Reproducible**: Complete artifact storage for model versioning
- ✅ **Scalable Architecture**: Easy to extend and deploy

---

## 🏗️ Architecture Flow

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Hyperparameter Tuning → Evaluation → Artifacts
```

---

## 📂 Project Structure

```
train-ticket-prediction/
│
├── Training/
│   ├── app.py                    # Application entry point
│   ├── train.py                  # Model training orchestrator
│   ├── pre_processing.py         # Data cleaning & preprocessing
│   ├── feature_operation.py      # Feature engineering logic
│   ├── data_upload.py            # Data loading utilities
│   └── requirements.txt          # Python dependencies
│
├── artifacts/
│   ├── models/                   # Trained model files (.pkl)
│   ├── transformers/             # Encoders, scalers (.pkl)
│   ├── metrics/                  # Performance metrics (.json)
│   └── images/                   # Evaluation plots (.png)
│
├── data_set/                     # Training data
│
├── README.md
└── .gitignore
```

---

## ⚙️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **ML Framework** | Scikit-Learn |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Model Persistence** | Joblib |
| **Logging** | Python Logging |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

**1. Clone the Repository**
```bash
git clone https://github.com/yourusername/train-ticket-prediction.git
cd train-ticket-prediction
```

**2. Create Virtual Environment**
```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r Training/requirements.txt
```

---

## 🎬 Usage

### Training the Model

Run the complete training pipeline:

```bash
python Training/train.py
```

This will:
- Load and preprocess the data
- Engineer features
- Train multiple models
- Perform hyperparameter tuning
- Save the best model and transformers
- Generate evaluation metrics

### Output Artifacts

After training, the following artifacts are generated in the `artifacts/` directory:

```
artifacts/
├── models/
│   └── best_model.pkl              # Best performing model
├── transformers/
│   ├── label_encoder.pkl           # Categorical encoders
│   └── scaler.pkl                  # Feature scalers
├── metrics/
│   └── model_performance.json      # Metrics (RMSE, MAE, R²)
└── images/
    ├── residual_plot.png           # Residual analysis
    └── feature_importance.png      # Feature importance chart
```

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **RMSE** | TBD |
| **MAE** | TBD |
| **R² Score** | TBD |

> *Update these values after training completion*

---

## 🔮 Features Used

The model predicts ticket prices based on:

- 🚂 **Train Type** (Express, Superfast, etc.)
- 🎫 **Class** (Sleeper, AC, General)
- 📍 **Source & Destination** stations
- ⏰ **Departure & Arrival Time**
- 📅 **Travel Date** (day, month, seasonality)
- 🛤️ **Distance** between stations
- 📈 **Demand Indicators**

---

## 🛣️ Roadmap

- [ ] REST API for real-time predictions (FastAPI/Flask)
- [ ] Docker containerization
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] MLflow integration for experiment tracking
- [ ] Cloud deployment (AWS SageMaker / Azure ML)
- [ ] Interactive web dashboard
- [ ] Model monitoring & retraining automation

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**

- 📧 Email: your.email@example.com
- 🌐 Portfolio: [yourportfolio.com](https://yourportfolio.com)
- 💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- Dataset source: [Add source]
- Inspired by real-world MLOps practices
- Built with open-source tools

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

Made with ❤️ and Python

</div>
