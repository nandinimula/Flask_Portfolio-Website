from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        flash(f"Thanks {name}, your message has been sent!", "success")
        return redirect(url_for("contact"))
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
