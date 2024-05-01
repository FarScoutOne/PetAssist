// index.js
document.getElementById('load').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/')
        .then(response => response.json())
        .then(data => {
            console.log(data);

            // If data is an array, you can use forEach here
            if (Array.isArray(data)) {
                data.forEach(item => {
                    // Do something with each item
            });
        }
    });
});