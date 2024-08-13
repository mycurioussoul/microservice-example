from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/containerhealth', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"})

@app.route('/containername')
def form():
    return render_template('container_name_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Container name is, {name}!"

@app.route('/containergreet', methods=['POST'])
def greet():
    data = request.get_json()
    print (data)
    name = data.get('name', 'World')
    return jsonify({"message": f"Container name is, {name}!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

