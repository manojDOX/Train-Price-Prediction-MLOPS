# 🚆 Train Ticket Price Prediction — MLOps Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Flask](https://img.shields.io/badge/Flask-API-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900)
![Status](https://img.shields.io/badge/Status-Production-success)

## 📌 Project Overview

This project builds an end-to-end machine learning solution to predict **train ticket prices** based on multiple features including train type, class, source, destination, departure time, and more. The pipeline implements best practices in MLOps with automated preprocessing, feature engineering, model training, hyperparameter tuning, and deployment via Flask API on AWS EC2.

---

## 🎯 Key Highlights

- ✅ **Automated ML Pipeline**: End-to-end workflow from raw data to trained model
- ✅ **REST API**: Flask-based prediction service with routing
- ✅ **Containerized**: Docker image available on Docker Hub
- ✅ **Cloud Deployed**: Running on AWS EC2 with SSH & HTTPS enabled
- ✅ **Production Ready**: Modular structure with saved transformers for inference
- ✅ **Multiple Models**: Comparison of various ML algorithms with hyperparameter tuning
- ✅ **Reproducible**: Complete artifact storage for model versioning
- ✅ **Scalable Architecture**: Easy to extend and deploy

---

## 🏗️ Architecture Flow

```
Raw Data → Preprocessing → Feature Engineering → Model Training → 
Hyperparameter Tuning → Evaluation → Flask API → Docker Container → 
AWS EC2 (Linux) → Production Service
```

---

## 📂 Project Structure

```
train-ticket-prediction/
│
├── Training/
│   ├── app.py                    # Training workflow entry point
│   ├── train.py                  # Model training orchestrator
│   ├── pre_processing.py         # Data cleaning & preprocessing
│   ├── feature_operation.py      # Feature engineering logic
│   ├── data_upload.py            # Data loading utilities
│   └── requirements.txt          # Training dependencies
│
├── api_flask/
│   ├── app.py                    # Flask API application
│   ├── predict_operation.py      # Prediction logic & routing
│   ├── Dockerfile                # Container configuration
│   └── requirements.txt          # API dependencies
│
├── artifacts/
│   ├── models/                   # Trained model files (.pkl)
│   ├── transformers/             # Encoders, scalers (.pkl)
│   ├── metrics/                  # Performance metrics (.json)
│   └── images/                   # Evaluation plots (.png)
│
├── data_set/
│   └── data1.csv                 # Training dataset
│
├── env/                          # Virtual environment
├── README.md
└── .gitignore
```

---

## ⚙️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **ML Framework** | Scikit-Learn |
| **API Framework** | Flask |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Containerization** | Docker |
| **Cloud Platform** | AWS EC2 (Linux OS) |
| **Model Persistence** | Joblib |
| **Logging** | Python Logging |
| **Security** | SSH, HTTPS |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker (for containerization)
- AWS Account (for cloud deployment)
- Git

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
# For training
pip install -r Training/requirements.txt

# For API
pip install -r api_flask/requirements.txt
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

### Running the Flask API Locally

Start the Flask prediction service:

```bash
cd api_flask
python app.py
```

The API will be available at `http://localhost:5000`

#### API Endpoints

**Prediction Endpoint**
```bash
POST /predict
Content-Type: application/json

{
  "train_type": "Express",
  "class": "Sleeper",
  "source": "Delhi",
  "destination": "Mumbai",
  "departure_time": "08:00",
  "arrival_time": "14:30",
  "travel_date": "2024-06-15"
}
```

**Response**
```json
{
  "predicted_price": 1250.50,
  "currency": "INR",
  "status": "success"
}
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
cd api_flask
docker build -t train-price-api:latest .
```

### Run Container Locally

```bash
docker run -p 5000:5000 train-price-api:latest
```

### Pull from Docker Hub

The pre-built image is available on Docker Hub:

```bash
docker pull yourusername/train-price-api:latest
docker run -p 5000:5000 yourusername/train-price-api:latest
```

---

## ☁️ AWS EC2 Deployment

### Current Deployment Configuration

- **Platform**: AWS EC2
- **Operating System**: Linux
- **Instance Type**: t2.medium (recommended)
- **Security Group**: 
  - SSH (Port 22) - Enabled
  - HTTPS (Port 443) - Enabled
  - HTTP (Port 80) - Enabled
  - Custom TCP (Port 5000) - For Flask API

### Deployment Steps

**1. Launch EC2 Instance**
```bash
# Connect via SSH
ssh -i your-key.pem ec2-user@your-ec2-public-ip
```

**2. Install Docker on EC2**
```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
```

**3. Pull and Run Docker Container**
```bash
docker pull yourusername/train-price-api:latest
docker run -d -p 80:5000 --name train-api train-price-api:latest
```

**4. Access the API**
```
http://your-ec2-public-ip/predict
```

### Security Configuration

- ✅ SSH access enabled for remote management
- ✅ HTTPS enabled for secure communication
- ✅ Security groups configured for necessary ports
- ✅ IAM roles for EC2 service permissions

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

## 🛠️ API Documentation

### Flask Routing Structure

```python
# Main routes in api_flask/app.py
@app.route('/')              # Health check
@app.route('/predict')       # Prediction endpoint
@app.route('/batch')         # Batch predictions
```

The `predict_operation.py` module handles all prediction logic including:
- Input validation
- Feature transformation
- Model inference
- Response formatting

---

## 🛣️ Roadmap

- [x] Flask REST API for real-time predictions
- [x] Docker containerization
- [x] Docker Hub image publishing
- [x] AWS EC2 deployment with Linux OS
- [x] SSH & HTTPS security configuration
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] MLflow integration for experiment tracking
- [ ] Load balancer & auto-scaling
- [ ] Model monitoring & retraining automation
- [ ] Interactive web dashboard
- [ ] Kubernetes orchestration

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `api_flask/` directory:

```env
FLASK_ENV=production
MODEL_PATH=../artifacts/models/best_model.pkl
TRANSFORMER_PATH=../artifacts/transformers/
PORT=5000
HOST=0.0.0.0
```

---

## 📈 Monitoring & Logs

- Application logs: `/var/log/train-api.log`
- Docker logs: `docker logs train-api`
- CloudWatch integration for AWS monitoring

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
- Deployed on AWS infrastructure

---

## 🐛 Troubleshooting

### Common Issues

**Docker Container Not Starting**
```bash
docker logs train-api
# Check for port conflicts
sudo lsof -i :5000
```

**EC2 Connection Issues**
```bash
# Check security group rules
# Ensure SSH (22), HTTP (80), HTTPS (443) are allowed
# Verify key pair permissions: chmod 400 your-key.pem
```

**Flask API Errors**
```bash
# Check logs
tail -f /var/log/train-api.log
# Verify model artifacts exist
ls -la artifacts/models/
```

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

**🚀 Live API**: `http://your-ec2-ip/predict`

Made with ❤️ and Python | Deployed on AWS

</div>