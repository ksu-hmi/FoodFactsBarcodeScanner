### Setting up Flask App 
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        inputname = request.form.get('myName', 'Guest')
        ip = request.remote_addr
        greeting = inputname.upper() + " Hi there! Welcome to ThoughtforFood. You are visiting from " + str(ip)
        return render_template('welcome.html', myName=greeting)
    return render_template("welcome.html", myName="Welcome to ThoughtForFood!")

#gonna figure out how to write out an "about us" page 
# or I will fork a repo into our main hmi org/team portal
@app.route('/about/') 
def about():
    return render_template("about.html")

@app.route('/barcode', methods=['GET', 'POST']) #create a request to call the external API
def barcode():
    result = None
    if request.method == 'POST':
        barcode = request.form.get('barcode')
        try:
            response = requests.get(f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json")
            data = response.json()
            if data.get("status") == 1:
                product = data["product"]
                result = {
                    'product_name': product.get("product_name", "Unknown"),
                    'ingredients': product.get("ingredients_text", "No ingredients listed."),
                    'error': None
                }
            else:
                result = {'error': "Product not found."}
        except Exception as e:
            result = {'error': f"Error fetching product: {str(e)}"}

    return render_template("barcode.html", result=result)

@app.route('/submit-profile', methods=['GET','POST']) #making a profile submission portal
def submit_profile():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        age = int(request.form.get('age', 0))
        gender = request.form.get('gender', 'unspecified')
        hypertension_input = request.form.get('hypertension', 'no').lower()
        has_hypertension = hypertension_input in ['yes', 'y']
        profile = {
            'name': name,
            'age' : age,
            'gender': gender,
            'hypertension': has_hypertension
    } 
        return render_template("submit_profile.html", profile=profile)
    return render_template("profile_form.html")

if __name__ == "__main__":
    print("Starting up....give me a second....visit http://127.0.0.1:5000/ on your local browser.")
    app.run(debug=True) 
