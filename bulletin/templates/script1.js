document.addEventListener('DOMContentLoaded', function() {
    fetchPlacements();
});

async function fetchPlacements() {
    try {
        const response = await fetch('/api/placements/');  // Replace with your Django API endpoint
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const placements = await response.json();
        displayPlacements(placements);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function displayPlacements(placements) {
    const tableBody = document.getElementById('placementTableBody');
    placements.forEach(placement => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${placement.company_name}</td>
            <td>${placement.job_title}</td>
            <td>${placement.description}</td>
            <td>${new Date(placement.created_at).toLocaleString()}</td>
            <td>${new Date(placement.updated_at).toLocaleString()}</td>
        `;
        tableBody.appendChild(row);
    });
}
