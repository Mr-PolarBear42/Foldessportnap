const { google } = require('googleapis');

const auth = new google.auth.GoogleAuth({
    keyFile: 'creditentials.json', // Path to your credentials file
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
});

// Initialize the Google Sheets API
const sheets = google.sheets({ version: 'v4', auth });
async function AppendToSheets(Name, Email) {
    const spreadsheetId = '1bnKewpKMiUJCScWPDOhoMnDGNbHe-uzXH1J_PDFaS34'; // Replace with your spreadsheet ID
    const range = 'Munkalap1';

    const values = [
        [Name, Email],
    ];



    const response2= await sheets.spreadsheets.values.append({
        spreadsheetId,
        range,
        valueInputOption: 'RAW', // Use 'USER_ENTERED' for formulas
        insertDataOption: 'INSERT_ROWS', // Add a new row
        resource: {
            values,
        },

    });

    console.log('Updated sheet:', response2.data);
}

AppendToSheets().catch(console.error);