### Setting up Flask App 
# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
   # return render_template("welcome.html", myName="Welcome to ThoughtForFood!")

#@app.route('/greet', methods=['POST']) #welcome!!!page!!!
#def greet():
   # inputname = request.form.get('myName', 'Guest')
   # ip = request.remote_addr
   # inputname = inputname.upper() + "hi there! Welcome to ThoughtforFood. You are visiting from " + str(ip)
   # return render_template('welcome.html', myName=inputname)

#gonna figure out how to write out an "about us" page 
# or I will fork a repo into our main hmi org/team portal
# @app.route('/about/') 
# def about():
    #return render_template("about.html")


#@app.route('/barcode/')
#def barcode():
     #return render_template("barcode.html")

#@app.route('/submit-profile', methods=['POST']) #making a profile submission portal
#def submit_profile():
    #name = request.form.get('name', 'Guest')
    #age = int(request.form.get('age', 0))
    #gender = request.form.get('gender', 'unspecified')
    #hypertension_input = request.form.get('hypertension', 'no').lower()
    #has_hypertension = hypertension_input in ['yes', 'y']
    #profile = {
            #'name': name,
            #'age' : age,
            #'gender': gender,
            #'hypertension': has_hypertension
    #} 
    #return render_template("submit_profile.html", profile=profile)

#def run_this_page():
#print("starting up....give me a second....visit http://127.0.0.1:5000/welcome/ on your local browser.")
#app.run(debug=True, use_reloader=False)

#if __name__ == "__main__":
    #app.run() #broken on so many levels. just like me. (i hate u python)
    
print("This functionality is coming soon.....")