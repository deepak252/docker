from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    # return "<h4>Hello, how is it going?</h4>"
    return render_template("index.html", name = name, tasks = ['Eat', 'Drink'])

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
