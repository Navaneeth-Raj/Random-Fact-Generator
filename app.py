from flask import Flask, redirect, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/index")

@app.route("/index")
def home_display():
    return render_template("index.html")

@app.route("/about")
def about_display():
    return render_template("about.html")

@app.route("/generated-fact") 
def random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            fact = data.get("text")  
            return jsonify(fact=fact) 
        return jsonify(fact="Failed to Retrieve Data. Try Again :("), 500
    except requests.exceptions.RequestException as e:
        return jsonify(fact=f"An error occurred: {str(e)}"), 500  

def get_ftw():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("text","No Fact Available this Week.")
    except requests.exceptions.RequestException as e:
        return "Error : No Fact for this Week :("

ftw = get_ftw()

@app.route("/highlights")
def highlight_display():
    return render_template("highlight.html", ftw=ftw)

if __name__ == "__main__":
    app.run(debug=True)
