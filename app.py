from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import os

app = Flask(__name__)

# Database Configuration - Support both PostgreSQL (Render) and SQLite (Local)
database_url = os.getenv('DATABASE_URL')
if database_url:
    # For Render PostgreSQL
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # For local development with SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spamguard.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    result = ""
    ans = ""
    if request.method == "POST":
        message = request.form["message"]
        vector = vectorizer.transform([message])
        result = model.predict(vector)[0]
        
        ans = "✅ Not-Spam"
        if result != "ham":
            ans = "🚨 Spam"
    
    return render_template("index.html", result=result, ans=ans, username=current_user.username)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        # Validation
        if not username or not email or not password:
            return render_template("register.html", error="All fields are required")
        
        if password != confirm_password:
            return render_template("register.html", error="Passwords do not match")
        
        if User.query.filter_by(username=username).first():
            return render_template("register.html", error="Username already exists")
        
        if User.query.filter_by(email=email).first():
            return render_template("register.html", error="Email already exists")
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")
    
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
