from flask import Flask, jsonify, request
import gspread  # To interact with Google Sheets
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

# Google Sheets setup
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\szori\\OneDrive\\Asztali gép\\Zalán mappa\\Coding\\Foldessportnap\\Backend\\credentials.json", SCOPE)
client = gspread.authorize(CREDS)
sheet = client.open("Sportnapteszt").sheet1  # Replace with your sheet name

@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json  # Get data from the frontend
    print("Received data:", new_data)  # Log the received data

    # Ensure all required fields are present and valid
    required_fields = ['name', 'email', 'grade', 'class', 'sport', 'teammates', 'misc']
    for field in required_fields:
        if field not in new_data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Convert teammates array to a string (if it's an array)
    if isinstance(new_data['teammates'], list):
        new_data['teammates'] = ', '.join(new_data['teammates'])

    try:
        # Append the data to the sheet
        sheet.append_row([
            new_data['name'],
            new_data['email'],
            new_data['grade'],
            new_data['class'],
            new_data['sport'],
            new_data['teammates'],
            new_data['misc']
        ])
        return jsonify({"message": "Data added successfully!"}), 201
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Failed to add data to Google Sheets"}), 500

if __name__ == '__main__':
    app.run(debug=True)