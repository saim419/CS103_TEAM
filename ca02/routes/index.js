async function generateClothingList() {
    // Get the user input from the form
    const input = document.getElementById('brand').value;

    // Make an HTTP request to the server to generate the shoe list
    const response = await fetch('/response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
    });

    // Parse the response as JSON
    const data = await response.json();

    // Update the HTML to display the generated shoe list
    const clothingList = data.clothingList;
    const clothingListElement = document.getElementById('clothingList');
    clothingListElement.innerHTML = clothingList;
}

