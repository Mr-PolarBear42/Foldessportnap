from flask import Flask, render_template, request, jsonify
import openpyxl
from openpyxl import load_workbook
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
    
    data_list = list(data.values())
    
    
    data_list[5] = str(data_list[5]) 
    data_list[5].removeprefix("{")
    data_list[5].removesuffix("}")
    
    print("Converted data to list:", data_list)
    wb=load_workbook("C:/Users/szori/OneDrive/Asztali gép/Zalán mappa/Coding/Foldessportnap/Jelentkezők.xlsx")
    print(wb.sheetnames)
    ws=wb.active
    ws.append(data_list)
    wb.save("Jelentkezők.xlsx")
    
    
    return jsonify({"status": "success", "message": "Data received"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)