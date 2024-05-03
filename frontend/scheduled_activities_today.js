document.getElementById('load').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/scheduled_activities_today')
        .then(response => response.json())
        .then(data => {
            const activities = data.scheduled_activities;
            if (Array.isArray(activities)) {
                const displayElement = document.getElementById('display');
                let activitiesHTML = '';
                activities.forEach(scheduled_activity => {
                    activitiesHTML += `<p>Activity: ${scheduled_activity.activity.activityName}, Pet: ${scheduled_activity.pet.name}, Deadline: ${scheduled_activity.deadline}</p>`;
                });
                displayElement.innerHTML = activitiesHTML;
            }
        });
});