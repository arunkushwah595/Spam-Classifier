from flask import Flask, render_template, request
import pickle
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        vector = vectorizer.transform([message])
        result = model.predict(vector)[0]
    return render_template("index.html", result=result)

# Vercel entry point
def handler(request, *args, **kwargs):
    return app(request, *args, **kwargs)
