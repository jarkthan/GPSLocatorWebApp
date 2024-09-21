function handleButtonClick(hole_id) {
    // const button = document.querySelector(`button[data-hole="${hole_id}"]`);
    // button.classList.add('clicked');

    if (navigator.geolocation) {
        let latestPosition = null;

        function getPosition() {
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    latestPosition = position;

                    console.log("Latitude: " + position.coords.latitude);
                    console.log("Longitude: " + position.coords.longitude);
                },
                function(error) {
                    console.error("Geolocation error:", error);
                },
                {
                    enableHighAccuracy: true,
                    maximumAge: 0
                }
            );
        }

        const intervalId = setInterval(getPosition, 5000); // Call getPosition every 5 seconds
        setTimeout(function() {
            clearInterval(intervalId); // Stop after 30 seconds

            if (latestPosition) {
                const latitude = latestPosition.coords.latitude;
                const longitude = latestPosition.coords.longitude;

                alert(`Hole ID: ${hole_id}\nLatitude: ${latitude}\nLongitude: ${longitude}\n`);

                document.getElementById('hole_id_input').value = hole_id;
                document.getElementById('latitude_input').value = latitude;
                document.getElementById('longitude_input').value = longitude;

                document.getElementById('holeForm').submit();
            } else {
                alert("Unable to retrieve GPS data.");
            }


        }, 30000); // Wait for 30 seconds before submitting the form
    } else {
        alert("Geolocation is not supported by this browser");
    }
    // button.classList.remove('clicked');
}
