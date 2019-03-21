// Create new map
let map;

function initBusinessListMap() {
    // default map location set to Glasgow
    const glasgow = {
        center: {lat: -34.397, lng: 150.644},
        zoom: 6,
    };

    // if there is geolocation:
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            const here = {
                center: {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                },
                zoom: 13,
            };
            map = new google.maps.Map(document.getElementById("googleMap"), here);
            addMarkers();
            document.getElementById("map_loading").style.display = "none";
        });

    } else {
        // if there isn't any geolocation let's center on Glasgow:
        map = new google.maps.Map(document.getElementById("googleMap"), glasgow);
        addMarkers();
        document.getElementById("map_loading").style.display = "none";
    }
}

// function for adding markers
function addMarker(coords, businessLink, businessAddress) {

    let marker = new google.maps.Marker({
        position: coords,
        map: map,
    });
    let infoWindow = new google.maps.InfoWindow({
        content: businessLink,
    });
    marker.addListener('click', function () {
        infoWindow.open(map, marker);
        document.getElementById("card-title").innerHTML = businessLink;
        document.getElementById("business-address").innerText = businessAddress;

    });
}


 function initBusinessMap() {

                let mapProp = {
                    center: {lat: lat, lng: lng},
                    zoom: 14,
                };
                // Create new map
                let businessMap = new google.maps.Map(document.getElementById("googleMap"), mapProp);
                // Add marker
                let marker = new google.maps.Marker({
                    position: {lat: lat, lng: lng},
                    map: businessMap
                });

                let infoWindow = new google.maps.InfoWindow({
                    content: businessName
                });
                marker.addListener('click', function () {
                    infoWindow.open(map, marker);
                });
                console.log();
            }

