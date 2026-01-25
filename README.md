# 🛡️ SpamGuard - AI Spam Detection

A full-stack machine learning application for detecting spam and phishing messages in SMS and emails with **95.79% accuracy**.

## ✨ Features

- 🤖 **AI-Powered Detection** - Logistic Regression trained on 61,690+ real messages
- ⚡ **Instant Analysis** - Real-time spam classification in milliseconds  
- 🔐 **Secure Authentication** - User login/registration with password hashing
- 🎨 **Professional UI** - Responsive design with light/dark theme support
- 📱 **Mobile Friendly** - Works on desktop, tablet, and mobile devices
- 🔒 **Data Privacy** - Your messages stay completely private
- 🚀 **Production Ready** - Deployed on Render with PostgreSQL database

## 🛠️ Tech Stack

**Frontend:**
- HTML5, CSS3, JavaScript
- Responsive design with modern UI/UX

**Backend:**
- Python 3.x
- Flask web framework
- Flask-SQLAlchemy (ORM)
- Flask-Login (Authentication)

**Database:**
- SQLite (local development)
- PostgreSQL (production on Render)

**Machine Learning:**
- Scikit-learn
- TF-IDF Vectorization (7000 features, trigrams)
- Logistic Regression classifier

## 📊 Model Performance

- **Accuracy**: 95.79%
- **Precision**: 95.81%
- **Recall**: 95.79%
- **Training Samples**: 61,690 messages from 6 datasets

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Local Development

1. **Clone/Download the project:**
   ```bash
   cd SpamGuard
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   ```
   http://localhost:5000
   ```

5. **Create an account and start detecting spam!**

## 📁 Project Structure

```
SpamGuard/
├── app.py                      # Flask application
├── model.pkl                   # Pre-trained ML model
├── vectorizer.pkl              # TF-IDF vectorizer
├── spam.csv                    # Training dataset
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Main classifier page
│   ├── login.html             # Login page
│   └── register.html          # Registration page
├── static/
│   └── style.css              # Application styling
├── .env.example                # Environment variables template
└── README.md                   # This file
```


## 📝 Usage

1. **Register** - Create a new account
2. **Login** - Use your credentials to access the classifier
3. **Paste Message** - Enter SMS or email text
4. **Analyze** - Click "Analyze" to classify
5. **Results** - Get instant spam/legitimate classification with safety tips

## 🎨 Features Highlight

- **Light/Dark Theme** - Toggle between themes with persistent storage
- **Character Counter** - Real-time message length display
- **Security Badges** - Trust indicators on authentication pages
- **Responsive Layout** - Perfect on any device size
- **Professional Design** - Modern glassmorphism UI

## 🔐 Security Features

- 🔒 Password hashing with Werkzeug
- 🛡️ Session management with Flask-Login
- 📊 User authentication required
- 🔑 Secure SECRET_KEY configuration

## 📊 Dataset Information

- **Total Messages**: 61,690
- **Spam Messages**: ~13,000 (20%)
- **Ham Messages**: ~48,000 (80%)
- **Sources**: 6 CSV datasets combined (from Kaggle)


## 👨‍💼 Author

**Arun Kushwah**  
[LinkedIn Profile](https://linkedin.com/in/arunkushwah592005)

