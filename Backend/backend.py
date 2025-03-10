from flask import Flask, jsonify, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

# Google Sheets setup
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\szori\\OneDrive\\Asztali gép\\Zalán mappa\\Coding\\Foldessportnap\\Backend\\credentials.json", SCOPE)
client = gspread.authorize(CREDS)
sheet = client.open("Sportnapteszt").sheet1 #Replace with sheets name

@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json 
    #print("Received data:", new_data)

    
    required_fields = ['name', 'email', 'grade', 'class', 'sport', 'teammates', 'misc']
    for field in required_fields:
        if field not in new_data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    
    new_data['teammates']=str(new_data['teammates'].values())
    
    new_data['teammates']=new_data['teammates'].removesuffix('])') 
    new_data['teammates']=new_data['teammates'].removeprefix('dict_values([')
    
    
    try:
      
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