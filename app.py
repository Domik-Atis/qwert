from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    message = request.form.get('message')
    messages.append(message)
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)