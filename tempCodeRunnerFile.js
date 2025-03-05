async function updateSheet() {
    const spreadsheetId = '1bnKewpKMiUJCScWPDOhoMnDGNbHe-uzXH1J_PDFaS34'; // Replace with your spreadsheet ID
    const range = 'Sheet1!A1:B2'; // Specify the range to update

    const values = [
        ['Hello', 'World'],
        ['This', 'Works'],
    ];

    const response = await sheets.spreadsheets.values.update({
        spreadsheetId,
        range,
        valueInputOption: 'RAW',
        resource: { values },
    });

    console.log('Updated sheet:', response.data);