function initAddBusinessAutocomplete() {

    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 55.864237, lng: -4.251806},
        zoom: 13,
        mapTypeId: 'roadmap'
    });

    // Create the search box and link it to the UI element.
    var input = document.getElementById('search-box');
    var searchBox = new google.maps.places.SearchBox(input);

    // Bias the SearchBox results towards current map's viewport.
    map.addListener('bounds_changed', function () {
        searchBox.setBounds(map.getBounds());
    });

    var markers = [];
    // Listen for the event fired when the user selects a prediction and retrieve
    // more details for that place.
    searchBox.addListener('places_changed', function () {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
            return;
        }

        // Clear out the old markers.
        markers.forEach(function (marker) {
            marker.setMap(null);
        });
        markers = [];

        // For each place, get the icon, name and location.
        var bounds = new google.maps.LatLngBounds();
        places.forEach(function (place) {
            if (!place.geometry) {
                console.log("Returned place contains no geometry");
                return;
            }
            var icon = {
                url: place.icon,
                size: new google.maps.Size(71, 71),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(25, 25)
            };

            // Create a marker for each place.
            markers.push(new google.maps.Marker({
                map: map,
                icon: icon,
                title: place.name,
                position: place.geometry.location
            }));


            document.getElementById("lat").value = place.geometry.location.lat();
            document.getElementById("long").value = place.geometry.location.lng();
            document.getElementById("name").value = place.name;
            document.getElementById("phone").value = place.formatted_phone_number;
            document.getElementById("url").value = place.website;
            document.getElementById("business_details").style.display = "block";

            let addressAsString = "";
            let openinghoursAsString = "";

            addressAsString += place.address_components[0].long_name + " ";

            for (let i = 1; i < place.address_components.length; i++) {
                addressAsString += place.address_components[i].long_name + "\n";
            }

            for (let i = 0; i < place.opening_hours.weekday_text.length; i++) {
                openinghoursAsString += place.opening_hours.weekday_text[i] + "\n";
            }

            document.getElementById("address").value = addressAsString;
            document.getElementById("opening_hours").value = openinghoursAsString;


            if (place.geometry.viewport) {
                // Only geocodes have viewport.
                bounds.union(place.geometry.viewport);
            } else {
                bounds.extend(place.geometry.location);
            }
        });
        map.fitBounds(bounds);
    });
}

function filterSelection(value) {
            if (value === 'no') {
                document.getElementById(value).style.display = "block";
                document.getElementById('yes').style.display = "none";
            } else if (value === 'yes') {
                document.getElementById(value).style.display = "block";
                document.getElementById('no').style.display = "none";
            } else {
                document.getElementById('no').style.display = "block";
                document.getElementById('yes').style.display = "block";
            }
        }