from flask import Flask, jsonify, request
import gspread  # To interact with Google Sheets
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets setup
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
client = gspread.authorize(CREDS)
sheet = client.open("Sportnapteszt").sheet1  # Replace with your sheet name

# Example route to fetch data from Google Sheets
@app.route('/api/data', methods=['GET'])
def get_data():
    records = sheet.get_all_records()  # Fetch all data from the sheet
    return jsonify(records)

# Example route to add data to Google Sheets
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json  # Get data from the frontend
    sheet.append_row([new_data['name'], new_data['age']])  # Add data to the sheet
    return jsonify({"message": "Data added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)