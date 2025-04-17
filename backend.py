from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/<page>')
def show_page(page):
    
    return render_template(f'{page}.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()  # Get JSON data from request
    print("Received data:", data)
    
    # Process your data here
    
    return jsonify({"status": "success", "message": "Data received"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)