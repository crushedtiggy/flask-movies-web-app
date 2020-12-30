from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__) 

app.config["DEBUG"] = True

@app.route("/")
def render_landing_page():
    try:
        return render_template("landing-page.html", user_account = "Heicoders", account_type = "Premium")
    except:
        return render_template("error404.html")

@app.route("/search", methods = ["POST"])
def form_submit():
    user_query = request.form['search_query'] # matches name attribute of query string input (HTML)
    return redirect(url_for('.search_imdb', query_string = user_query))

@app.route("/search/<query_string>", methods = ["GET"])
def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
        
    querystring = {"q": query_string} # change the fixed string to video_title variable
        
    headers = {
        'x-rapidapi-key': "c403d25882mshd4c054b7b7572ebp115fa9jsn69f49911e2c5",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
	}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        data = response.json()
        
        return render_template("search-result.html", data = data)
    except:
        return render_template("error404.html")

# Define your app.route before the following

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")