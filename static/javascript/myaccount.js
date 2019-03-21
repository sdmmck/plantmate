let businessSlug = "";
let businessLat;
let businessLong;
let businessName;
let localBusinesses = [];


//get the location
function UserLocation(position) {
    NearestBusiness(position.coords.latitude, position.coords.longitude);
}

// Convert degrees to something mysterious and mathematical and maybe relating to the shape of the earth
function Deg2Rad(deg) {
    return deg * Math.PI / 180;
}

// yet more maths - best not to think too hard about this stuff
function PythagorasEquirectangular(lat1, lon1, lat2, lon2) {
    lat1 = Deg2Rad(lat1);
    lat2 = Deg2Rad(lat2);
    lon1 = Deg2Rad(lon1);
    lon2 = Deg2Rad(lon2);
    const R = 6371; // km
    const x = (lon2 - lon1) * Math.cos((lat1 + lat2) / 2);
    const y = (lat2 - lat1);
    const d = Math.sqrt(x * x + y * y) * R;
    return d;
}

// now let's find those plant shops
function NearestBusiness(latitude, longitude) {
    let minDif = 99999;
    let closest;
    for (let index = 0; index < localBusinesses.length; ++index) {
        let dif = PythagorasEquirectangular(latitude, longitude, localBusinesses[index][1], localBusinesses[index][2]);
        if (dif < minDif) {
            closest = index;
            minDif = dif;
        }
    }
    businessSlug = localBusinesses[closest][0];
    businessLat = localBusinesses[closest][1];
    businessLong = localBusinesses[closest][2];
    businessName = localBusinesses[closest][3];

    businessDetails(localBusinesses[closest][0]);
    initMap();
}

function initMap() {
    const lat = Number(businessLat);
    const lng = Number(businessLong);
    let mapProp = {
        center: {lat: lat, lng: lng},
        zoom: 15,
    };
    // Create new map
    let map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    document.getElementById("loading_map").style.display = "none";
    // Add marker
    let marker = new google.maps.Marker({
        position: {lat: lat, lng: lng},
        map: map
    });
    let infoWindow = new google.maps.InfoWindow({
        content: businessName
    });
    marker.addListener('click', function () {
        infoWindow.open(map, marker);
    });
}