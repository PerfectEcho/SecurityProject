from flask import Flask, request, render_template, jsonify

website = Flask(__name__)

@website.route('/')
def form():
    return render_template('form.html')

@website.route('/', methods=['POST'])
def form_post():    
    text = request.form['text']
    processed_text = jsonify(text)
    return processed_text

if __name__ == "__main__":
    website.run(debug=True)