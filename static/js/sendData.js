async function sendData(sportofstudent, teammatesofstudent, miscofstudent) {
    
    const data = JSON.parse(sessionStorage.getItem("userData"));

   
    const tdata = {
        sport: sportofstudent,
        teammates: teammatesofstudent,
        misc: miscofstudent
    };

    
    const mergedData = { ...data, ...tdata };
    console.log(mergedData);
    
    try {
        const response = await fetch('http://127.0.0.1:5000/api/data', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(mergedData), // Send the merged data
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
        
    } catch (error) {
        console.error('Error:', error);
    }
    try {
        const response = await fetch('https://foldessportnap.onrender.com/api/data', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(mergedData), // Send the merged data
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
    }
        catch (error) 
        {
            console.error('Error:', error);
        }
}