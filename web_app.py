### Setting up Flask App 
from flask import Flask, render_template, request
from pip._vendor import requests

app = Flask(__name__)

#ok gonna try to set up the logic for the recommendationmodel class here :-)
class RecommendationModel:
    def evaluate_food_item(self, user_profile, food_nutriments, display_sodium=True):
        has_hypertension = user_profile.get("hypertension", False)
        explanation = []
        recommended = True

        sodium_mg = food_nutriments.get('sodium_serving', 0) * 1000  # convert g to mg

        # Check for hypertension
        if display_sodium:
            print("\nSodium per serving: " + str(round(sodium_mg, 2)) + " mg")

        if has_hypertension and sodium_mg > 500:
            recommended = False
            explanation.append("⚠️  Warning: High sodium content. Not recommended for those with hypertension.")
        elif sodium_mg == 0:
            print("\nSodium per serving data not available for this product.")

        # === Saturated Fat Logic Added ===
        saturated_fat = food_nutriments.get('saturated-fat_serving', 0)
        print("Saturated fat per serving: " + str(round(saturated_fat, 2)) + " g")
        print("Tip: Try to keep your total saturated fat intake under 13g per day.")

        if saturated_fat > 5:
            recommended = False
            explanation.append("⚠️  Warning: High saturated fat content.")

        if recommended:
            return {
                "recommended": True,
                "message": "Great choice! You can eat this product. It's aligned with your health needs."
            }
        else:
            return {
                "recommended": False,
                "message": " and" .join(explanation) + " \nIt would be best to find an alternative option.\nWhat to look for: when looking at nutriment content, look for items that contain less sodium and less saturated fat."
            }

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
                nutriments = product.get('nutriments', {})
                #ok for the protoype i want to hardcode a user_profile so itll populate the hyptertension rec model
                user_profile ={
                    'name': 'Dr. Thomas', #lol
                    'age': 30,
                    'gender': 'Male',
                    'hypertension': True
                }
                evaluator = RecommendationModel()
                evaluation = evaluator.evaluate_food_item(user_profile,nutriments)
                result = {
                    'product_name': product.get("product_name", "Unknown"),
                    'ingredients': product.get("ingredients_text", "No ingredients listed."),
                    'evaluation': evaluation.get("message"),
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

### for running our test for presentation here at the following bacodes to use:
# Ramen Noodle Soup, Chicken Flavor: 041789002113
# Nutty Super Wholefood Salad: 00961035
# Apple Slices (Dried): 29088645