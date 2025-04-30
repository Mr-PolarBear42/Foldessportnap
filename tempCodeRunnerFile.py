@app.route('/download/<filename>')
def download_file(filename):
    file_path = f"C:/Users/szori/OneDrive/Asztali gép/Zalán mappa/Coding/Foldessportnap/docs{filename}"
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})