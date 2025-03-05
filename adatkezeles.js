// Replace with your Google Sheets API credentials
const CLIENT_ID = '797961482887-a6ccsi8odgpqep441j78eijkcl9j5ie0.apps.googleusercontent.com';
const API_KEY = 'AIzaSyDsyjebdNUwGeEkGxZ1FAcDEdyw4ir4Byc';
const SHEET_ID = '1bnKewpKMiUJCScWPDOhoMnDGNbHe-uzXH1J_PDFaS34';
const DISCOVERY_DOC = 'https://sheets.googleapis.com/$discovery/rest?version=v4';
const SCOPES = 'https://www.googleapis.com/auth/spreadsheets';

let tokenClient;
let gapiInited = false;
let gisInited = false;

function gapiLoaded() {
    gapi.load('client', initializeGapiClient);
}

async function initializeGapiClient() {
    await gapi.client.init({
        apiKey: API_KEY,
        discoveryDocs: [DISCOVERY_DOC],
    });
    gapiInited = true;
    maybeEnableButtons();
}

function gisLoaded() {
    tokenClient = google.accounts.oauth2.initTokenClient({
        client_id: CLIENT_ID,
        scope: SCOPES,
        callback: '', // Defined later
    });
    gisInited = true;
    maybeEnableButtons();
}

function maybeEnableButtons() {
    if (gapiInited && gisInited) {
        document.getElementById('sheetForm').addEventListener('submit', handleFormSubmit);
    }
}

async function handleFormSubmit(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    tokenClient.callback = async (resp) => {
        if (resp.error !== undefined) {
            throw resp;
        }
        await appendData([[name, email]]);
    };

    if (gapi.client.getToken() === null) {
        tokenClient.requestAccessToken({ prompt: 'consent' });
    } else {
        tokenClient.requestAccessToken({ prompt: '' });
    }
}

async function appendData(data) {
    try {
        const response = await gapi.client.sheets.spreadsheets.values.append({
            spreadsheetId: SHEET_ID,
            range: 'Munkalap1', // Adjust the range as needed
            valueInputOption: 'RAW',
            insertDataOption: 'INSERT_ROWS',
            resource: {
                values: data,
            },
        });
        console.log('Data appended:', response);
        alert('Data submitted successfully!');
    } catch (err) {
        console.error('Error appending data:', err);
        alert('Error submitting data.');
    }
}

// Load the Google API client and OAuth2 library
(function () {
    const gapiScript = document.createElement('script');
    gapiScript.src = 'https://apis.google.com/js/api.js';
    gapiScript.onload = gapiLoaded;
    document.head.appendChild(gapiScript);

    const gisScript = document.createElement('script');
    gisScript.src = 'https://accounts.google.com/gsi/client';
    gisScript.onload = gisLoaded;
    document.head.appendChild(gisScript);
})();