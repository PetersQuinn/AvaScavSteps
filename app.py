from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Map of valid passwords to their corresponding page route names
PAGES = {
    "memorylane": "page1",
    "anchorpoint": "page2",
    "trustfall": "page3",
    "foreverpromise": "page4",
    "returngift": "page5"
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pw = request.form.get('password', '').lower().strip()
        if pw in PAGES:
            return redirect(url_for(PAGES[pw]))
        else:
            return render_template("index.html", error="Incorrect password. Try again.")
    return render_template("index.html", error=None)

@app.route('/page1')
def page1():
    return render_template("page1.html")

@app.route('/page2')
def page2():
    return render_template("page2.html")

@app.route('/page3')
def page3():
    return render_template("page3.html")

@app.route('/page4')
def page4():
    return render_template("page4.html")

@app.route('/page5')
def page5():
    return render_template("page5.html")

if __name__ == '__main__':
    app.run(debug=True)
