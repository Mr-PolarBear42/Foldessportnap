from flask import Flask, render_template, request, jsonify
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

# === Google Sheets Setup ===
SERVICE_ACCOUNT_FILE = 'service_account.json'  # Your downloaded key
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SHEET_ID = '16zdMIdAF2ZmdYHge7pY905BSBjxgjN35RNRIX48cSRY'         # <-- Replace with your Google Sheet ID
SHEET_RANGE = 'Jelentkezők!A2'                      # Adjust as needed

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
sheets_service = build('sheets', 'v4', credentials=credentials)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/<page>')
def show_page(page):
    return render_template(f'{page}.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received data:", data)

    # Prepare data row for Sheets
    data_list = list(data.values())
    data_list[5] = str(data_list[5]).removeprefix("{").removesuffix("}")
    print("Converted data to list:", data_list)

    # Append to Google Sheet
    body = {
        'values': [data_list]
    }
    sheets_service.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range=SHEET_RANGE,
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()

    print("Data appended to Google Sheet.")
    return jsonify({"status": "success", "message": "Data stored in Google Sheet"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)