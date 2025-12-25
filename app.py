from flask import Flask, render_template, request
import pickle
import os

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
        
    ans="✅ Not-Spam"
    if(result!="ham"):
        ans="🚨 Spam"
    
    
    return render_template("index.html", result=result, ans=ans)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
