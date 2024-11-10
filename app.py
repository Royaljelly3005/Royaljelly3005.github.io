from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():  # put application's code here
    return render_template('index.html')

@app.route('/resume')
def resume_page():
    return render_template('resume.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/aboutme')
def aboutme_page():
    return render_template('aboutme.html')

if __name__ == '__main__':
    app.run(debug=True)
