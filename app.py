from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # You can add any processing or validation of the form data here if needed

        # Redirect to a thank you page after form submission
        return redirect("/thank_you")

    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # You can add any processing or validation of the form data here if needed

        # Redirect to the thank you page after form submission
        return redirect("/thank_you")

    return render_template("contact.html")

# Your other routes here


@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
