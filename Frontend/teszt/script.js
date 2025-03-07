document.getElementById('fetchData').addEventListener('click', async () => {
    try {
        const response = await fetch('http://localhost:5000/api/data');
        const data = await response.json();
        document.getElementById('data').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});

// Example: Sending data to the backend
async function sendData() {
    const newData = { name: 'John', age: 30 };
    const response = await fetch('http://localhost:5000/api/data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newData),
    });
    const result = await response.json();
    console.log(result);
}