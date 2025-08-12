from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data here
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # For now, just print the data
        print(f"Received message from {name} ({email}): {message}")
        return 'Message sent successfully!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
