document.getElementById('load').addEventListener('click', function () {
    fetch('http://127.0.0.1:5000/scheduled_activities_today')
        .then(response => response.json())
        .then(data => {
            const scheduled_activities = data.scheduled_activities; // Changed scheduled_activities to activities
            if (Array.isArray(scheduled_activities)) {
                const displayElement = document.getElementById('display');
                let activitiesHTML = '';
                scheduled_activities.forEach(scheduled_activity => {
                    activitiesHTML += `<p>Activity: ${scheduled_activity.activity_name}, Pet: ${scheduled_activity.pet_name}, Deadline: ${scheduled_activity.deadline}</p>`;
                });
                displayElement.innerHTML = activitiesHTML;
            }
        });
});