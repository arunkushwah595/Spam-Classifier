from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
