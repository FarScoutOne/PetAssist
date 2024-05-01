document.getElementById('load').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/owners')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Access the 'owners' property of the data
            const owners = data.owners;
            if (Array.isArray(owners)) {
                // Select the element where you want to display the data
                const displayElement = document.getElementById('display');

                // Create a string of HTML representing the owner data
                let ownerHTML = '';
                owners.forEach(owner => {
                    ownerHTML += `<p>Name: ${owner.name}, Age: ${owner.age}, Role: ${owner.role}</p>`;
                });

                // Update the display element's innerHTML with the owner data
                displayElement.innerHTML = ownerHTML;
            }
        });
});